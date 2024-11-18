import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Specify the path to ChromeDriver (make sure the path is correct)
driver_path = "C:\\Program Files\\chromedriver\\chromedriver.exe"  # Update this to your chromedriver path
service = Service(driver_path)  # Create a Service object with the driver path

# Initialize the WebDriver with the service object
driver = webdriver.Chrome(service=service)

# Function to read the Bee Movie script from a text file
def load_script(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        print("Script loaded successfully.")
        return lines
    except Exception as e:
        print(f"Error loading script: {e}")
        return []

# Function to upload a quote to the website
def upload_quote(driver, quote, context=" ", author=" ", who_said_it=" "):
    try:
        # Navigate to the website
        driver.get("https://ise-quoteboat.vercel.app/")
        print("Navigated to the website.")

        # Wait for the form fields to load
        wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds

        # Locate the fields and ensure they are visible
        quote_field = wait.until(EC.presence_of_element_located((By.ID, "quote")))
        context_field = wait.until(EC.presence_of_element_located((By.ID, "context")))
        author_field = wait.until(EC.presence_of_element_located((By.ID, "author")))
        who_said_it_field = wait.until(EC.presence_of_element_located((By.ID, "sayer")))

        # Locate the submit button using a simpler, more reliable selector
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

        print("Form fields located and ready to interact with.")

        # Fill in the fields with a small delay between each
        print(f"Filling in the quote: {quote}")
        quote_field.send_keys(quote)
        time.sleep(1)  # Wait 1 second after inputting the quote
        
        print(f"Filling in the context: {context}")
        context_field.send_keys(context)
        time.sleep(1)  # Wait 1 second after inputting the context

        print(f"Filling in the author: {author}")
        author_field.send_keys(author)
        time.sleep(1)  # Wait 1 second after inputting the author

        print(f"Filling in 'Who said it': {who_said_it}")
        who_said_it_field.send_keys(who_said_it)
        time.sleep(1)  # Wait 1 second after inputting the 'Who said it'

        # Submit the form
        print("Submitting the form...")
        submit_button.click()
        time.sleep(1)  # Wait for the submission to process
        print("Form submitted.")

        # Wait for submission to process
        time.sleep(random.uniform(1, 2))  # Random delay to simulate human behavior
        print("Waited for a few seconds to simulate human behavior.")

    except Exception as e:
        print(f"Error while uploading the quote: {e}")

# Task to upload the next line from the script
def scheduled_upload(lines, current_line_index, author, who_said_it):
    if current_line_index < len(lines):
        quote = lines[current_line_index].strip()  # Get the line and strip any extra whitespace
        print(f"Uploading quote: {quote}")  # Print the quote to be uploaded
        upload_quote(driver, quote, context="", author=author, who_said_it=who_said_it)  # Upload the quote
        print("Quote uploaded successfully!")

        # Update the current line index
        current_line_index += 1
        print(f"Next index will be: {current_line_index}")

        # Schedule the next upload after 2 seconds (without resetting the index)
        if current_line_index < len(lines):
            time.sleep(2)  # Wait 2 seconds before the next upload
            scheduled_upload(lines, current_line_index, author, who_said_it)

    else:
        print("All quotes have been uploaded!")
        return

# Main function
def main():
    # Load the Bee Movie script
    file_path = "C:\\Users\\tom\\Downloads\\ISEWebsitePranks\\ISEQuoteBookPrank\\Rust Version\\TextInput.txt"  # Replace with the correct path to your file
    lines = load_script(file_path)

    if not lines:
        print("No lines loaded from the script. Exiting.")
        return

    # Set the fixed "author" as "The Voices From Above"
    author = " "

    # Set the fixed "who_said_it" as "The voices from above"
    who_said_it = " "

    # Start the process by uploading the first quote
    current_line_index = 0
    scheduled_upload(lines, current_line_index, author, who_said_it)

    # Keep the script running
    print("Quote bot is running. Press Ctrl+C to stop.")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
