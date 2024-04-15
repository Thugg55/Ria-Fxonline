from selenium import webdriver
import json
import requests

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    # Initialize Selenium WebDriver.
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

    # You might need to click the login button or submit the form here

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
    driver.quitg)

if __name__ == "__main__":
    main()

