from utils import query_duckdb

query_duckdb("""
    CREATE TABLE IF NOT EXISTS movies (
        title STRING,
        year INTEGER,
        genre TEXT,
        rating TINYINT
    );
    """)

if __name__=="__main":
    print(query_duckdb("DESC;"))