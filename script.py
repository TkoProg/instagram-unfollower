import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def unfollow_people(username, password, target_usernames):
    # Start the browser session
    driver = webdriver.Chrome()

    try:
        # Open Instagram login page
        driver.get('https://www.instagram.com/accounts/login/')

        # Wait for the login page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

        # Find the username and password input fields and enter your credentials
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)
        # Allow the website to process the request
        time.sleep(10)

        # Wait for the login to complete in order the previous statement failed to allow enough time
        WebDriverWait(driver, 10).until(EC.url_contains('https://www.instagram.com/'))
        # Variable to keep track of the number of people unfollowed
        counter = 1

        # Loop through target usernames and unfollow each one
        for target_username in target_usernames:
            # Go to the users profile
            driver.get(f'https://www.instagram.com/{target_username}/')

            # Simulate human behavior by waiting before executing the next action
            time.sleep(random.randint(3, 6))

            # Wait for the profile page to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button')))

            # Simulate human behavior by waiting before executing the next action
            time.sleep(random.randint(3, 6))

            # Find and click the "Following" button to unfollow
            follow_button = driver.find_element(By.XPATH, "//*[text()='Following']")
            follow_button.click()

            # Simulate human behavior by waiting before executing the next action
            time.sleep(random.randint(3, 6))

            # Find and click the "Unfollow" button to confirm unfollow
            confirm_button = driver.find_element(By.XPATH, "//*[text()='Unfollow']")
            confirm_button.click()

            # Keep track of people unfollowed, in case the program crashes
            print(f"Number of users unfollowed: {counter}. Successfully unfollowed: {target_username}")
            # Increase the value of the variable by 1 for each user that has been unfollowed successfully
            counter += 1

            # Simulate human behavior by waiting before executing the next action
            time.sleep(random.randint(3, 6))

    except Exception as e:
        # Display errors as they occur
        print(f"An error occurred: {e}")

    finally:
        # Close the browser session
        driver.quit()


def to_unfollow(usernames):
    # Open file
    file = open(usernames, "r")
    # Create list to store usernames
    everyone = []
    while True:
        # Read the file line-by-line
        row = file.readline()
        # Quit if faced with an empty line
        if row == "":
            break
        # Remove extra whitespaces at the end of the usernames
        row = row.rstrip('\n')
        # Add username to the total list
        everyone.append(row)
    # Close file to ensure secure data transfer
    file.close()
    return everyone


# Instagram username (Needs to be changed to your specific username)
user = 'username'
# Instagram password (Needs to be changed to your specific password)
passw = 'password'
# Call for function that reads the usernames of the people you want to unfollow and places them in a list
# There can only be one username per line in the document (There are example usernames in the document)
# Keep an empty line at the end of the document as well, it's a good practice
target_users = to_unfollow("to_be_unfollowed.txt")
# Call for the function to begin the unfollow process
unfollow_people(user, passw, target_users)
