from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


# Step 1: Load the OWASP page

URL = "https://owasp.org/Top10/2025/"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get(URL)

# Step 2: Find Top 10 vulnerabilities using XPath

results = []

# XPath targets the Top 10 list links
vulnerability_elements = driver.find_elements(
    By.XPATH,
    "/html/body/div[3]/main/div/div[3]/article/ol/li/a"
)

print(f"Found {len(vulnerability_elements)} vulnerabilities")

for vuln in vulnerability_elements:
    title = vuln.text.strip()
    href = vuln.get_attribute("href")

    if title and href:
        vuln_data = {
            "Title": title,
            "Link": href
        }
        results.append(vuln_data)

# Step 3: Print results to verify

print("\nOWASP Top 10 Vulnerabilities:")
for item in results:
    print(item)

# Step 4: Write results to CSV

df = pd.DataFrame(results)
csv_filename = "assignment8/owasp_top_10.csv"
df.to_csv(csv_filename, index=False)

print(f"\nData written to {csv_filename}")

driver.quit()
