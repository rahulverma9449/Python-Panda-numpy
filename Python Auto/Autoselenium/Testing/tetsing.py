from selenium import webdriver



from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace with the path to your chromedriver executable
 

# Replace with your Amazon account credentials
username = "rahulverma9449@gmail.com"
password = "Rahul@123"

# Set up the Chrome WebDriver
driver=webdriver.Firefox()

# Navigate to the Amazon login page
driver.get("https://www.amazon.com")

# Click on the "Sign in" link
sign_in_link = driver.find_element(By.ID, "nav-link-accountList")
sign_in_link.click()

# Enter the username and click "Continue"
username_input = driver.find_element(By.ID, "ap_email")
username_input.send_keys(username)
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# Enter the password and click "Sign in"
password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys(password)
sign_in_button = driver.find_element(By.ID, "signInSubmit")
sign_in_button.click()

# Perform any additional interactions after logging in

# Close the browser
driver.quit()
