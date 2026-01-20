from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time

# Task 3 Step 1: Load the web page
URL = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get(URL)

# Task 3 Step 2: Find all li search result elements
RESULT_LI_CLASS = "cp-search-result-item"
TITLE_CLASS = "title-content"
AUTHOR_CLASS = "author-link"
FORMAT_CONTAINER_CLASS = "cp-format-info"

results = []

li_elements = driver.find_elements(By.TAG_NAME, "li")
book_items = [
    li for li in li_elements
    if RESULT_LI_CLASS in li.get_attribute("class")
]

print(f"Found {len(book_items)} book entries") 

# Task 3 Step 3: Main extraction loop
for item in book_items:
    try:
        # ---- Title ----
        title_element = item.find_element(By.CLASS_NAME, TITLE_CLASS)
        title = title_element.text.strip()

        # ---- Authors ----
        author_elements = item.find_elements(By.CLASS_NAME, AUTHOR_CLASS)
        authors = [author.text.strip() for author in author_elements]
        author_text = "; ".join(authors)

        # ---- Year ----
        format_container = item.find_element(By.CLASS_NAME, FORMAT_CONTAINER_CLASS)
        format_year = format_container.text.strip()

        # ---- Store results ----
        book_data = {
            "Title": title,
            "Author": author_text,
            "Format-Year": format_year
        }

        results.append(book_data)

        # Debug print
        print(f"Extracted: {title}")

    except Exception as e:
        print("Error processing item:", e)


# Task 3 Step 4: Create DataFrame and print
df = pd.DataFrame(results)
print("\nFinal DataFrame:")
print(df)
    
# Save to CSV and JSON
df.to_csv("assignment8/books.csv", index=False)

with open("assignment8/books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)


# Close browser
driver.quit()

# Task 4: Write out the data

# Write DataFrame to CSV
csv_filename = "assignment8/books.csv"
df.to_csv(csv_filename, index=False)
print(f"Data written to {csv_filename}")

# Write results list to JSON
json_filename = "assignment8/books.json"
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Data written to {json_filename}")