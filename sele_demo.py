from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Setup WebDriver ---
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# --- Test 1: Login ---
def test_login():
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("✅ Test 1: Logged in successfully")
    time.sleep(2)

# --- Test 2: Add product to cart ---
def test_add_to_cart():
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    print("✅ Test 2: Product added to cart")
    time.sleep(2)

# --- Test 3: View Cart & Verify Item ---
def test_verify_cart():
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert "Sauce Labs Backpack" in item_name
    print("✅ Test 3: Cart contains the correct item")
    time.sleep(2)

# --- Test 4: Remove item from cart ---
def test_remove_item():
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    print("✅ Test 4: Item removed from cart")
    time.sleep(2)

# --- Test 5: Logout ---
def test_logout():
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    print("✅ Test 5: Logged out successfully")

# --- Run Tests ---
try:
    test_login()
    test_add_to_cart()
    test_verify_cart()
    test_remove_item()
    test_logout()
finally:
    driver.quit()
    print("🧹 Browser closed.")

