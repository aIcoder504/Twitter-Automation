import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = Options()
options.headless = False  # Set to True if you do not want to open the browser window
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

# Automatically download and setup the ChromeDriver using webdriver_manager
# service = Service(ChromeDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Chrome()

# Path to your JSON cookie file
cookie_file_path = '/Users/sohanchoudhary/Desktop/Web Scrapping /amazon/cookie.json'

# URL of the Twitter login page
twitter_url = 'https://x.com/'

# Open Twitter home page
driver.get(twitter_url)
time.sleep(15)  # Wait for the page to load

# Load cookies from the file and add them to the browser
def load_cookies(driver, cookie_file_path):
    with open(cookie_file_path, 'r') as cookie_file:
        cookies = json.load(cookie_file)
        for cookie in cookies:
            if "expiry" in cookie:
                cookie["expiry"] = int(cookie["expiry"])
            driver.add_cookie(cookie)

load_cookies(driver, cookie_file_path)
driver.refresh()  # Refresh the page to apply cookies
time.sleep(5)  # Wait for the page to load with cookies applied
driver.get("https://twitter.com/compose/tweet")
time.sleep(10)

try:
    # Wait for the tweet modal to appear
    box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr"))
    )
    
    # Enter the tweet content
    tweet_content = "HI, good afternoon to all"
    print(tweet_content)
    box.send_keys(tweet_content)
    time.sleep(20)

    
    tweet_button_modal = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='tweetButton']"))
)

# Click the tweet button
    tweet_button_modal.click()
    time.sleep(60)
    print("Tweet posted successfully!")
except Exception as e:
    print("Login failed or tweet posting failed", str(e))

    # Scroll through the Twitter feed


