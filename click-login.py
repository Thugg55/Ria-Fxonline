from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    # Initialize Selenium WebDriver (make sure to install appropriate driver for your browser)
    driver = webdriver.Chrome()
    
    # Navigate to the login page
    driver.get("https://fxonline.riaenvia.net/External/Login.aspx")

    # Fill in the login form fields
    username_field = driver.find_element_by_id("User Name")
    username_field.send_keys("your_username")
    
    password_field = driver.find_element_by_id("Password")
    password_field.send_keys("your_password")

    agent_field = driver.find_element_by_id("Agent")
    agent_field.send_keys("your_agent")

    branch_field = driver.find_element_by_id("Branch")
    branch_field.send_keys("your_branch")

    # Find and click the login button
    login_button = driver.find_element_by_id("Login")
    login_button.click()

    # Wait for the page to load after login (assuming there's some element indicating successful login)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "some_element_after_login"))
        )
    except TimeoutException:
        print("Login failed or page didn't load after login.")
        driver.quit()
        return

    # Extract data after login

    # Save data to JSON file
    data = {
        "User Name": username_field.get_attribute("value"),
        "Password": password_field.get_attribute("value"),
        "Agent": agent_field.get_attribute("value"),
        "Branch": branch_field.get_attribute("value")
    }
    save_to_json(data, "data.json")
    print("Data saved to data.json")

    # Close the browser window
    driver.quit()

if __name__ == "__main__":
    main()

