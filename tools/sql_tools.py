from typing import Any, List, Tuple, Optional
from .database import Database

db = Database()


def run_query(sql: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any, ...]]:
    """
    Execute a SELECT query and return results.

    Args:
        sql: SQL query string (SELECT).
        params: Optional tuple of parameters for safe substitution.

    Returns:
        List of tuples containing query results.
    """
    return db.execute_query(sql, params)


def run_non_query(sql: str, params: Optional[Tuple[Any, ...]] = None) -> bool:
    """
    Execute an INSERT, UPDATE, or DELETE query.

    Args:
        sql: SQL query string (INSERT, UPDATE, DELETE).
        params: Optional tuple of parameters for safe substitution.

    Returns:
        True if successful, False otherwise.
    """
    return db.execute_non_query(sql, params)


def fetch_low_stock_products(threshold: int = 10) -> List[Tuple[Any, ...]]:
    """
    Convenience function to fetch products below a stock threshold.

    Args:
        threshold: Minimum stock level considered low.

    Returns:
        List of products with stock below threshold.
    """
    sql = "SELECT product_id, stock_level FROM products WHERE stock_level < ?"
    return run_query(sql, (threshold,))


def fetch_supplier_reliability(min_score: float = 0.8) -> List[Tuple[Any, ...]]:
    """
    Fetch suppliers with reliability above a minimum score.

    Args:
        min_score: Minimum reliability score.

    Returns:
        List of suppliers meeting the criteria.
    """
    sql = "SELECT supplier_id, name, reliability_score FROM suppliers WHERE reliability_score >= ?"
    return run_query(sql, (min_score,))
