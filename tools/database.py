import sqlite3
from typing import Any, List, Tuple, Optional


class Database:
    """
    A lightweight SQLite database helper for supply chain intelligence.
    Provides connection management, query execution, and safe transactions.
    """

    def __init__(self, db_path: str = "data/supply_chain.db"):
        self.db_path = db_path

    def get_connection(self) -> sqlite3.Connection:
        """Create and return a new database connection."""
        return sqlite3.connect(self.db_path)

    def execute_query(
        self, query: str, params: Optional[Tuple[Any, ...]] = None
    ) -> List[Tuple[Any, ...]]:
        """
        Execute a SELECT query and return results.
        """
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute(query, params or ())
            results = cur.fetchall()
            conn.close()
            return results
        except sqlite3.Error as e:
            return [("Database error", str(e))]

    def execute_non_query(
        self, query: str, params: Optional[Tuple[Any, ...]] = None
    ) -> bool:
        """
        Execute an INSERT, UPDATE, or DELETE query.
        Returns True if successful, False otherwise.
        """
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute(query, params or ())
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def initialize_schema(self, schema_sql: str) -> None:
        """
        Initialize database schema from a SQL string.
        Useful for setting up tables at startup.
        """
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.executescript(schema_sql)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Schema initialization error: {e}")
