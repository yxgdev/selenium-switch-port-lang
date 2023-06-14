from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_service = Service("./chromedriver")
chrome_opts = Options()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=driver_service, options=chrome_opts)

# Load the webpage
driver.get("https://yxgdev.github.io/")


# Find the dropdown button element
dropdown_button = driver.find_element(By.XPATH,"/html/body/nav/div[2]/ul/li[3]/a")  # Replace 'dropdown-button-id' with the actual ID or locator of the dropdown button

# Create an ActionChains object
actions = ActionChains(driver)

# Perform the hover action on the dropdown button
actions.move_to_element(dropdown_button).perform()

# Wait for the dropdown menu items to appear
menu_items = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/nav/div[2]/ul/li[3]/ul/li[3]/a')))

cn_button = driver.find_element(By.XPATH,"/html/body/nav/div[2]/ul/li[3]/ul/li[3]/a")
actions.move_to_element(cn_button).click().perform()

