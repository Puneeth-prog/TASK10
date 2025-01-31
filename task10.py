from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to ChromeDriver
service_obj = Service("C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Open Instagram URL
url = "https://www.instagram.com/quvofficial/"
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Adjust based on your network speed

# Use XPath to locate the followers and following elements
followers_xpath = "//a[contains(@href, 'followers')]/span"
following_xpath = "//a[contains(@href, 'following')]/span"

# Extract followers and following counts
followers = driver.find_element(By.XPATH, followers_xpath).get_attribute("title")  # 'title' holds the count
following = driver.find_element(By.XPATH, following_xpath).text

print(f"Followers: {followers}")
print(f"Following: {following}")

# Close the browser
driver.quit()
