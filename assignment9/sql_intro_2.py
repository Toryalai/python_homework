import sqlite3
import pandas as pd

# Step 1: Connect to the database
db_path = "./db/lesson.db"
conn = sqlite3.connect(db_path)

# Step 2: Read data into DataFrame
query = """
SELECT
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products
    ON line_items.product_id = products.product_id;
"""

df = pd.read_sql_query(query, conn)

print("\nFirst 5 rows of initial DataFrame:")
print(df.head())

# Step 3: Add total column
df["total"] = df["quantity"] * df["price"]

print("\nFirst 5 rows after adding total column:")
print(df.head())

# Step 4: Group by product_id
summary_df = (
    df
    .groupby("product_id")
    .agg(
        line_item_count=("line_item_id", "count"),
        total_sales=("total", "sum"),
        product_name=("product_name", "first")
    )
    .reset_index()
)

print("\nFirst 5 rows of grouped DataFrame:")
print(summary_df.head())

# Step 5: Sort by product_name
summary_df = summary_df.sort_values(by="product_name")

# Step 6: Write to CSV
output_file = "./assignment9/order_summary.csv"
summary_df.to_csv(output_file, index=False)

print(f"\nOrder summary written to {output_file}")

conn.close()
