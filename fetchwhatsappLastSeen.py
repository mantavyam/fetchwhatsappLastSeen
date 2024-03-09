# first install this: pip install selenium reportlab
# Download the Microsoft Edge WebDriver compatible with your Edge browser version.
# Replace: service = EdgeService('path_to_edgedriver')
# With: service = EdgeService('C:\\Users\\Mickeyfying Studios\\Downloads\\edgedriver_win64\\msedgedriver.exe')
# example inputs: #  +91-93xxxxxxxx // 18:55:00 - 09:03:24 // 19:10:00 - 09:03:24 // E:\clubhouse\trackwp

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import time

# Function to log into WhatsApp Web and retrieve last seen time
def get_last_seen_time(phone_number, duration_start, duration_end, output_location):
    # Start Microsoft Edge WebDriver
    service = EdgeService('C:\\Users\\Mickeyfying Studios\\Downloads\\edgedriver_win64\\msedgedriver.exe')

    driver = webdriver.Edge(service=service)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    time.sleep(60)  # Adjust this delay to ensure QR code is scanned

    # Search for the user by phone number
    search_box = driver.find_element(By.XPATH, '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(phone_number)
    search_box.send_keys(Keys.ENTER)

    # Wait for chat to load
    time.sleep(10)

    # Retrieve last seen time
    last_seen_element = driver.find_element(By.XPATH, '//span[contains(@title, "online")]/parent::div/preceding-sibling::div')
    last_seen_time = last_seen_element.get_attribute("title")

    # Create a PDF file to store activity timestamps
    pdf_file = output_location + "/activity_timestamps.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, "WhatsApp User Activity Tracker")
    c.drawString(100, 730, f"Phone Number: {phone_number}")
    c.drawString(100, 710, "Activity Duration:")
    c.drawString(150, 690, f"Start: {duration_start}")
    c.drawString(150, 670, f"End: {duration_end}")
    c.drawString(100, 650, "Last Seen Time:")
    c.drawString(150, 630, last_seen_time)
    c.save()

    print("Last seen time retrieved successfully.")
    print(f"Activity timestamps saved to: {pdf_file}")

    # Close WebDriver
    driver.quit()

if __name__ == "__main__":
    # Input from the user
    phone_number = input("Enter the phone number associated with the WhatsApp account: ")
    duration_start = input("Enter the start of the activity duration (HH:MM:SS - DD:MM:YY): ")
    duration_end = input("Enter the end of the activity duration (HH:MM:SS - DD:MM:YY): ")
    output_location = input("Enter the location to save the output file: ")

    # Get last seen time and generate PDF
    get_last_seen_time(phone_number, duration_start, duration_end, output_location)
