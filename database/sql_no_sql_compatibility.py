"""
Main integration module for the multi-database shop system.
Coordinates PostgreSQL, Redis, MongoDB, and Cassandra operations.
"""
import uuid
from typing import List, Dict, Any
from pymongo.errors import PyMongoError
from cassandra import DriverException
from database.rd_data.session_manager import SessionManager
from database.cr_data.cassandra_log_manager import CassandraLogManager
from database.mg_data.mongo_connector import MongoConnector
from database.mg_data.product_manager import ProductManager
from database.mg_data.order_manager import OrderManager
from database.postgre_sql import PostgresUserManager
import database.backup_copy as backup


def run_integrated_shop() -> None:
    """
    Executes a complete business flow: user creation, session management,
    product inventory update, order placement, and analytical logging.
    """
    try:
        pg_manager = PostgresUserManager()
        session_mgr = SessionManager()
        log_mgr = CassandraLogManager()

        mongo_connector = MongoConnector()
        mongo_client = mongo_connector.connect()

        if not mongo_client:
            raise PyMongoError("Не вдалося підключитися до MongoDB")

        db_mongo = mongo_client["internet_shop"]
        product_repo = ProductManager(db_mongo)
        order_repo = OrderManager(db_mongo, product_repo)

        print("Усі бази даних успішно підключені.")

    except PyMongoError as e:
        print(f"Ошибка базы данных: {e}")
        return

    try:
        user_name = "Sylvester"
        user_id = pg_manager.create_user(user_name, "sylvester@example.com")
        print(f"[PostgreSQL] Користувач зареєстрований. ID: {user_id}")

        session_token = str(uuid.uuid4())
        session_mgr.create_session(str(user_id), session_token)
        session_mgr.update_activity(session_token)

        product_repo.add_one_product("Smart watch", 12000, "Electronics", 10)

        basket: List[Dict[str, Any]] = [
            {"name": "Smart watch", "price": 12000, "quantity": 1}
        ]
        order_repo.create_dynamic_order(user_name, basket)
        print(f"[MongoDB] Замовлення для {user_name} успішно створено.")

        print("\n--- Запуск моніторингу та резервного копіювання ---")
        backup.analyze_data_pollution(order_repo)

        backup.backup_to_redis(order_repo, session_mgr, "orders")

        backup.backup_collection_to_json(
            mongo_connector,
            "internet_shop",
            "orders",
            "orders_backup.json"
        )
        print("--- Моніторинг завершено ---\n")

        log_mgr.add_log(
            user_id=str(user_id),
            event_type="PURCHASE_COMPLETED",
            metadata=f"Token: {session_token}, Order: Smart watch"
        )
        print("[Cassandra] Аналітичний лог записано.")

    except DriverException  as e:
        print(f"Критична помилка у процесі роботи: {e}")

    finally:
        print("--- Завершення роботи ---")
        log_mgr.close()
        pg_manager.conn.close()
        mongo_client.close()
        print("Усі з'єднання з базами даних закриті.")


if __name__ == "__main__":

    run_integrated_shop()
