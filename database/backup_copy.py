"""
Module for database monitoring and backup operations.
Provides functionality for MongoDB exports and Redis snapshots.
"""
from datetime import datetime
from typing import Any
from bson import json_util


def backup_collection_to_json(connector: Any, db_name: str,
                    collection_name: str, file_path: str) -> None:
    """Export data from Mongo to JSON (as Compass does)."""
    db = connector.client[db_name]
    collection = db[collection_name]

    data = list(collection.find())

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_util.dumps(data, indent=4))
    print(f"Резервна копія збережена в {file_path}")


def backup_to_redis(mongo_manager: Any, redis_manager: Any, collection_name: str) -> None:
    """Stores a timestamped slice of a Mongo collection in Redis."""
    data = list(mongo_manager.collection.find())
    backup_key = f"backup:{collection_name}:{datetime.now().strftime('%Y%m%d_%H%M')}"

    serialized_data = json_util.dumps(data)

    redis_manager.r.setex(backup_key, 86400, serialized_data)
    print(f"Резервна копія колекції {collection_name} "
          f"зберігається в Redis під ключем: {backup_key}"
    )

def analyze_data_pollution(mongo_manager: Any) -> None:
    """Collection analysis for anomalous data types."""
    pipeline = [
        {"$project": {"field_types": {"$type": "$total_sum"} }},
        {"$group": {"_id": "$field_types", "count": {"$sum": 1}}}
    ]
    analysis = list(mongo_manager.collection.aggregate(pipeline))
    print("Звіт про стан даних (Field: total_sum):")

    for item in analysis:
        print(f"Тип: {item['_id']}, Кількість: {item['count']}")
