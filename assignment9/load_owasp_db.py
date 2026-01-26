import pandas as pd
import sqlite3
from pathlib import Path

# Step 1: Load CSV into Pandas
csv_path = "./assignment8/owasp_top_10.csv"
df = pd.read_csv(csv_path)

print("Original DataFrame:")
print(df)


# Step 2: Clean Data

# Drop rows with missing values
df_clean = df.dropna()

# Remove duplicate vulnerabilities (by Title)
df_clean = df_clean.drop_duplicates(subset=["Title"])

print("\nCleaned DataFrame:")
print(df_clean)

# Step 3: Create SQLite DB
# -----------------------------

db_path = "./db/owasp.db"
Path("./db").mkdir(exist_ok=True)

with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = 1")

    # Create table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS owasp_top_10 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            link TEXT NOT NULL
        )
    """)

    df_clean.to_sql(
        "owasp_top_10",
        conn,
        if_exists="append",
        index=False
    )

    conn.commit()

print("\nData successfully saved to SQLite database.")
