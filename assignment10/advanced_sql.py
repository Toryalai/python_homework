import sqlite3


# Task 1: Complex JOINs with Aggregation
print("\nTask 1: Complex JOINs with Aggregation")

def main():
    # Open database connection
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()

    # SQL query for Task 1
    query = """
    SELECT
        o.order_id,
        SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li
        ON o.order_id = li.order_id
    JOIN products p
        ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
    """

    # Execute query
    cursor.execute(query)
    results = cursor.fetchall()

    # Print results

    for order_id, total_price in results:
        print(f"{order_id} ---> {total_price:.2f}")

# Task 2: Subqueries and Average Order Price per Customer

    query_task2 = """
    SELECT
        c.customer_name,
        AVG(o.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (
        SELECT
            o.order_id,
            o.customer_id AS customer_id_b,
            SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li
            ON o.order_id = li.order_id
        JOIN products p
            ON li.product_id = p.product_id
        GROUP BY o.order_id, o.customer_id
    ) o
    ON c.customer_id = o.customer_id_b
    GROUP BY c.customer_id;
    """

    cursor.execute(query_task2)
    results = cursor.fetchall()

    print("\nTask 2: Average order price per customer")
    print("Customer Name | Average Order Price")
    for customer_name, avg_price in results:
        if avg_price is not None:
            print(f"{customer_name} =====> {avg_price:.2f}")
        else:
            print(f"{customer_name} | No orders")


    # ------------------------------------------------------
    # Task 3: Insert Transaction Based on Data

    # Enable foreign key
    conn.execute("PRAGMA foreign_keys = 1")

    try:
        # Start transaction
        conn.execute("BEGIN")

        # Get customer_id
        cursor.execute("""
            SELECT customer_id
            FROM customers
            WHERE customer_name = 'Perez and Sons';
        """)
        customer_id = cursor.fetchone()[0]

        # Get employee_id
        cursor.execute("""
            SELECT employee_id
            FROM employees
            WHERE first_name = 'Miranda'
              AND last_name = 'Harris';
        """)
        employee_id = cursor.fetchone()[0]

        # Get 5 least expensive product_ids
        cursor.execute("""
            SELECT product_id
            FROM products
            ORDER BY price
            LIMIT 5;
        """)
        product_ids = [row[0] for row in cursor.fetchall()]

        # Insert new order and get order_id
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id)
            VALUES (?, ?)
            RETURNING order_id;
        """, (customer_id, employee_id))

        order_id = cursor.fetchone()[0]

        # Insert line items (quantity = 10 each)
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, 10);
            """, (order_id, product_id))

        # Commit transaction
        conn.commit()

        print("\nTask 3: Insert Transaction Based on Data:")
        print("\nNew order created successfully")
        print(f"Order ID: {order_id}")

        # Verify inserts with JOIN
        cursor.execute("""
            SELECT
                li.line_item_id,
                li.quantity,
                p.product_name
            FROM line_items li
            JOIN products p
                ON li.product_id = p.product_id
            WHERE li.order_id = ?;
        """, (order_id,))

        results = cursor.fetchall()

        print("\nLine Items for New Order")
        print("Line Item ID | Quantity | Product Name")

        for line_item_id, quantity, product_name in results:
            print(f"{line_item_id} ----------> {quantity} ----------> {product_name}")

    except Exception as e:
        conn.rollback()
        print("Error occurred, transaction rolled back:")
        print(e)



    # Task 4: Aggregation with HAVING

    query_task4 = """
    SELECT
        e.employee_id,
        e.first_name,
        e.last_name,
        COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o
        ON e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5;
    """

    cursor.execute(query_task4)
    results = cursor.fetchall()

    print("\nTask 4: Employees with more than 5 orders")
    print("Employee ID | First Name | Last Name | Order Count")

    for employee_id, first_name, last_name, order_count in results:
        print(f"{employee_id} ------------> {first_name} ------------> {last_name} ------------> {order_count}")


    # Close database connection
    conn.close()


if __name__ == "__main__":
    main()
