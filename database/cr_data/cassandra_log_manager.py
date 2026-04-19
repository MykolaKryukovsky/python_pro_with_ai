"""
This module provides a log management system using Apache Cassandra.
It handles creation of keyspaces, tables, and CRUD operations for logs.
"""
# pylint: disable=no-name-in-module
import uuid
from datetime import datetime, timedelta
from typing import Any, List, Optional
from cassandra.cluster import Cluster, NoHostAvailable
from cassandra import WriteTimeout, ReadTimeout, InvalidRequest


class CassandraLogManager:
    """
    Manages application logs in Cassandra with automatic setup and TTL support.
    """
    def __init__(self,contact_points: Optional[List[str]] = None) -> None:
        nodes = contact_points or ['127.0.0.1']
        try:
            self.cluster = Cluster(nodes, port=9042)
            self.session = self.cluster.connect()
            self._setup_db()
        except NoHostAvailable as e:
            print(f"Помилка з'єднання з Кассандрою: {e}")
            raise

    def _setup_db(self) -> None:
        """Creates keyspace and table if they do not exist."""
        self.session.execute("""
            CREATE KEYSPACE IF NOT EXISTS app_logs 
            WITH replication = {'class': 'SimpleStrategy', 
            'replication_factor': 1}
        """)
        self.session.set_keyspace('app_logs')

        self.session.execute("""
            CREATE TABLE IF NOT EXISTS app_logs (
                event_id uuid,
                user_id text,
                event_type text,
                event_timestamp timestamp,
                metadata text,
                PRIMARY KEY (event_type, event_timestamp, event_id)
            ) WITH CLUSTERING ORDER BY (event_timestamp DESC);
        """)

    def add_log(self, user_id: str, event_type: str, metadata: str) -> None:
        """Inserts a new log entry into the database."""
        query = """
            INSERT INTO event_logs (event_id, user_id, event_type, 
            event_timestamp, metadata) VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.session.execute(query, (uuid.uuid4(), user_id,
                          event_type, datetime.now(), metadata)
            )
            print(f"Лог {event_type} добавлено.")
        except (InvalidRequest, WriteTimeout) as e:
            print(f"Помилка при записі ллога: {e}")

    def get_logs_24h(self, event_type: str) -> List[Any]:
        """Retrieves logs for a specific type from the last 24 hours."""
        since = datetime.now() - timedelta(hours=24)
        query = ("SELECT * FROM event_logs WHERE event_type = %s "
                 "AND event_timestamp >= %s"
        )
        try:
            return self.session.execute(query, (event_type, since))
        except ReadTimeout as e:
            print(f"Сервер не відповів вчасно (таймаут читання) {e}")
            return []
        except InvalidRequest as e:
            print(f"Помилка запросу: {e}")
            return []

    def update_metadata(self, event_type: str, event_timestamp: datetime,
                        event_id: uuid.UUID, new_meta: str
    ) -> None:
        """Updates metadata for a specific log entry."""
        query = ("UPDATE event_logs SET metadata = %s WHERE event_type = %s "
                 "AND event_timestamp = %s AND event_id = %s"
        )
        self.session.execute(query, (new_meta, event_type, event_timestamp,
                                     event_id))
        print("Метаданные обновлены.")

    def delete_old_logs(self, event_type: str) -> None:
        """Deletes logs older than 7 days for a given event type."""
        seven_days_ago = datetime.now() - timedelta(days=7)
        query = "DELETE FROM event_logs WHERE event_type = %s AND event_timestamp < %s"
        self.session.execute(query, (event_type, seven_days_ago))
        print(f"Старые логи типа {event_type} удалены.")

    def close(self) -> None:
        """Closes the cluster connection."""
        self.cluster.shutdown()
        print("З'єднання з Кассандрою закрито.")
