import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Configure logging
logging.basicConfig(filename='script.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    try:
        # Initialize Selenium WebDriver for Microsoft Edge
        driver = webdriver.Edge(executable_path="path_to_msedgedriver.exe")
        
        # Navigate to the login page
        driver.get("https://fxonline.riaenvia.net/External/Login.aspx")

        # Fill in the login form fields
        username = "your_username"
        password = "your_password"
        agent = "your_agent"
        branch = "your_branch"
        
        username_field = driver.find_element_by_id("Username")
        username_field.send_keys(username)
        
        password_field = driver.find_element_by_id("Password")
        password_field.send_keys(password)

        agent_field = driver.find_element_by_id("Agent")
        agent_field.send_keys(agent)

        branch_field = driver.find_element_by_id("Branch")
        branch_field.send_keys(branch)

        # Find and click the login button
        login_button = driver.find_element_by_id("Login")
        login_button.click()

        # Wait for the page to load after login (assuming there's some element indicating successful login)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "some_element_after_login"))
        )

        # Extract data after login (if necessary)

        # Save data to JSON file
        # Example:
        data = {
            "Username": username,
            "Password": password,
            "Agent": agent,
            "Branch": branch
        }
        save_to_json(data, "data.json")
        logging.info("Data saved to data.json")

    except NoSuchElementException as e:
        logging.error(f"Element not found: {e}")
    except TimeoutException:
        logging.error("Timeout: Page did not load within expected time")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Close the browser window
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()

