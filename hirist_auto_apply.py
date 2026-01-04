import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

TARGET_JOBS = 500

JOB_URLS = [
    "https://www.hirist.tech/search/net-jobs?loc=&minexp=2&maxexp=3&posting=&category=&searchType=&method=",
    "https://www.hirist.tech/search/backend?loc=Mumbai&minexp=2&maxexp=3&posting=7&category=&searchType=&method=&query=asp-net-jobs&sort=&page=0&industry=",
    "hhttps://www.hirist.tech/k/product-roadmap-jobs?page=3&ref=topnavigation&pref=jf",
    "https://www.hirist.tech/k/net-jobs?pref=jf",
    "https://www.hirist.tech/search/flutter-jobs?loc=&minexp=2&maxexp=3&posting=15&category=&searchType=&method=&pref=jf&query=flutter-jobs&sort=&page=0&industry=",
    "https://www.hirist.tech/search/flutter-jobs?loc=&minexp=0&maxexp=30&posting=15&category=&searchType=&method=&pref=jf&query=flutter-jobs&sort=&page=0&industry=",
    "https://www.hirist.tech/k/full-stack-jobs?pref=aj_rl_br&pref=jf",
    "https://www.hirist.tech/k/project-management-jobs?ref=topnavigation&pref=jf",
    "https://www.hirist.tech/k/product-roadmap-jobs?ref=topnavigation&pref=jf",
    "https://www.hirist.tech/k/user-story-jobs?ref=topnavigation&pref=jf",
    "https://www.hirist.tech/k/project-management-jobs?ref=topnavigation&pref=jf",
    "https://www.hirist.tech/k/business-analyst-jobs?ref=topnavigation&pref=jf",
    "https://www.hirist.tech/k/techno-functional-consultant-jobs?ref=topnavigation&pref=jf"
]

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=options)

applied = 0

for url in JOB_URLS:
    if applied >= TARGET_JOBS:
        break

    driver.get(url)
    time.sleep(5)

    while applied < TARGET_JOBS:
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input.PrivateSwitchBase-input[type='checkbox']")

        for cb in checkboxes:
            if applied >= TARGET_JOBS:
                break

            driver.execute_script("arguments[0].scrollIntoView(true);", cb)
            time.sleep(0.4)

            if not cb.is_selected():
                driver.execute_script("arguments[0].click();", cb)
                applied += 1
                print(f"Selected: {applied}")

                delay = random.uniform(0.3, 1.4)  # seconds
                time.sleep(delay)


        try:
            apply_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Apply All')]")
            driver.execute_script("arguments[0].scrollIntoView(true);", apply_btn)
            time.sleep(1)
            apply_btn.click()
            print("Applied successfully 🎯")
            time.sleep(3)
            break
        except:
            print("Apply button not found on this page.")
            break

print("Automation Finished.")
