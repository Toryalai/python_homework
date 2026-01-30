import os
import sqlite3

db_path = "./db/magazines.db"
os.makedirs(os.path.dirname(db_path), exist_ok=True)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    conn.execute("PRAGMA foreign_keys = 1")

    # Create tables 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        );
    """)

    # Insert functions 
    def add_publisher(name):
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO publishers (name) VALUES (?)",
                (name,)
            )
        except sqlite3.Error as e:
            print("Error adding publisher:", e)

    def add_magazine(name, publisher_id):
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)",
                (name, publisher_id)
            )
        except sqlite3.Error as e:
            print("Error adding magazine:", e)

    def add_subscriber(name, address):
        try:
            cursor.execute("""
                SELECT id FROM subscribers
                WHERE name = ? AND address = ?
            """, (name, address))

            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO subscribers (name, address) VALUES (?, ?)",
                    (name, address)
                )
        except sqlite3.Error as e:
            print("Error adding subscriber:", e)

    def add_subscription(subscriber_id, magazine_id, expiration_date):
        try:
            cursor.execute("""
                SELECT id FROM subscriptions
                WHERE subscriber_id = ? AND magazine_id = ?
            """, (subscriber_id, magazine_id))

            if cursor.fetchone() is None:
                cursor.execute("""
                    INSERT INTO subscriptions
                    (subscriber_id, magazine_id, expiration_date)
                    VALUES (?, ?, ?)
                """, (subscriber_id, magazine_id, expiration_date))
        except sqlite3.Error as e:
            print("Error adding subscription:", e)


    # Populate tables 
    add_publisher("Tech Media Group")
    add_publisher("Health Publications")
    add_publisher("Global News Corp")

    # Magazines
    add_magazine("Tech Today", 1)
    add_magazine("Healthy Living", 2)
    add_magazine("World Weekly", 3)

    # Subscribers
    add_subscriber("Alice Smith", "123 Main St")
    add_subscriber("Bob Johnson", "456 Oak Ave")
    add_subscriber("Alice Smith", "789 Pine Rd")

    # Subscriptions
    add_subscription(1, 1, "2026-01-01")
    add_subscription(1, 2, "2025-12-31")
    add_subscription(2, 3, "2026-06-30")

    # Commit changes
    conn.commit()
    print("Data inserted successfully.")

    print("\nAll Subscribers:")
    try:
        cursor.execute("SELECT * FROM subscribers;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Error retrieving subscribers:", e)

    print("\nAll Magazines (Sorted by Name):")
    try:
        cursor.execute("""
            SELECT * FROM magazines
            ORDER BY name;
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Error retrieving magazines:", e)

    print("\nMagazines Published by Tech Media Group:")
    try:
        cursor.execute("""
            SELECT magazines.name
            FROM magazines
            JOIN publishers
                ON magazines.publisher_id = publishers.id
            WHERE publishers.name = ?;
        """, ("Tech Media Group",))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Error retrieving magazines by publisher:", e)


except sqlite3.Error as e:
    print("An error occurred:")
    print(e)

finally:
    if 'conn' in locals():
        conn.close()
        print("Database connection closed.")
