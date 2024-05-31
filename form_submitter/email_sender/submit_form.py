from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def submit_form():
    # Taking user input
    full_name = input('Enter Full Name: ')
    contact_number = input("Enter Contact Number (10 digits): ")
    email_id = input("Enter Email ID: ")
    full_address = input("Enter Full Address: ")
    pin_code = input("Enter Pin Code: ")
    date_of_birth = input("Enter Date of Birth (DD-MM-YYYY): ")
    gender = input("Enter Gender (Male/Female): ")
    verification_code = input("Enter Verification code (GNFPYC): ")


    #Example
    # full_name = "Test"
    # contact_number = "1111111111"
    # email_id = "Test@gmail.com"
    # full_address = "Test 123A"
    # pin_code = "110011"
    # date_of_birth = "11-11-1111"
    # gender = 'Female'
    # verification_code = "GNFPYC"



    # Initialize the WebDriver 
    driver = webdriver.Chrome()
    driver.get('https://forms.gle/WT68aV5UnPajeoSc8')

    try:
        # Full Name
        full_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        full_name_field.send_keys(full_name)

        # Contact Number
        contact_number_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        contact_number_field.send_keys(contact_number)

        # Email ID
        email_id_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        email_id_field.send_keys(email_id)

        # Full Address
        full_address_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'))
        )
        full_address_field.send_keys(full_address)

        # Pin Code
        pin_code_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        pin_code_field.send_keys(pin_code)

        # Date of Birth
        dob_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'))
        )
        dob_field.send_keys(date_of_birth)

        # Gender
        
        gender_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        gender_field.send_keys(gender)
        

        # Verification Code
        verification_code_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        verification_code_field.send_keys(verification_code)

        # Submit the form
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'))
        )
        submit_button.click()

        # Wait for confirmation page and take screenshot
        time.sleep(5)
        driver.save_screenshot('confirmation.png')

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    submit_form()
