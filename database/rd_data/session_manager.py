"""
This module manages user sessions using Redis.
It handles session creation, retrieval, activity updates, and deletion.
"""
import time
from datetime import datetime
from typing import Optional, Dict, Any
import redis
from redis.exceptions import RedisError


class SessionManager:
    """
    A class to manage user sessions in Redis with expiration.
    Attributes:
        r (Optional[redis.Redis]): Redis client instance.
        session_timeout (int): Session TTL in seconds.
    """
    def __init__(self, host: str='localhost', port: int=6379, db: int=0) -> None:
        try:
            self.r = redis.Redis(host=host, port=port, db=db,
                    decode_responses=True, socket_connect_timeout=2
            )
            self.r.ping()
            print(f"Session initialized for user {host}:{port}")
        except ConnectionError:
            print(f"Connection error for user {host}:{port}")
            self.r = None
        self.session_timeout = 1800

    def create_session(self, user_id: str, session_token: str) -> None:
        """
        Creates a new session in Redis using a hash map and sets expiration.
        """
        if not self.r:
            return
        try:
            key = f"session:{session_token}"
            session_data = {
                "user_id": user_id,
                "session_token": session_token,
                "login_time": datetime.now().isoformat(),
                "last_activity": time.time()
            }
            with self.r.pipeline() as pipe:
                pipe.hset(key, mapping=session_data)
                pipe.expire(key, self.session_timeout)
                pipe.execute()
            print(f"Session created for user {user_id}. Token: {session_token}")
        except RedisError as e:
            print(f"Session creation failed for user {user_id}. Error: {e}")

    def get_session(self, session_token: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves session data by token.
        """
        try:
            key = f"session:{session_token}"
            data = self.r.hgetall(key)
            if not data:
                print(f"Session not found for user {session_token}")
                return None
            return data
        except RedisError as e:
            print(f"Session retrieval failed for user {session_token}. Error: {e}")
            return None

    def update_activity(self, session_token: str) -> None:
        """
        Updates the last activity timestamp and refreshes session TTL.
        """
        if not self.r:
            return
        try:
            key = f"session:{session_token}"
            if self.r.exists(key):
                self.r.hset(key, "last_activity", time.time())
                self.r.expire(key, self.session_timeout)
                print(f"Session updated for user {session_token}")
            else:
                print(f"Session not found for user {session_token}")
        except RedisError as e:
            print(f"Session update failed for user {session_token}. Error: {e}")

    def delete_session(self, session_token: str) -> None:
        """
        Deletes the session from Redis.
        """
        if not self.r:
            return
        try:
            key = f"session:{session_token}"
            result = self.r.delete(key)
            if result:
                print(f"Session deleted for user {session_token}")
            else:
                print(f"Session {session_token} already gone")
        except RedisError as e:
            print(f"Session deletion failed for user {session_token}. Error: {e}")
