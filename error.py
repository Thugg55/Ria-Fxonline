from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def save_to_json(data, filename):
	with open(filename, 'w') as json_file:
		json.dump(data, json_file, indent=4)

def main():
	try:
		# intialize selenium for Edge
		driver = Webdriver.Egde(executable_path="path_to_msedgedriver.exe")
		
		# Navigate login
		driver.get("https://fxonline.riaenvia.net/External/Login.aspx"

		# Fill login
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
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Login Successful"))
        )

        # Extract data after login (if necessary)

        # Save data to JSON file
        # Example:
        data = {
            "username": username_field.get_attribute("value"),
            "password": password_field.get_attribute("value"),
            "agent": agent_field.get_attribute("value"),
            "branch": branch_field.get_attribute("value")
        }
        save_to_json(data, "data.json")
        print("Data saved to data.json")

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except TimeoutException:
        print("Timeout: Page did not load within expected time")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser window
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()
