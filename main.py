#!/opt/anaconda3/bin/python3
import getpass
import smtplib
import time
import os
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

gmailMsg= "*** APPOINTMENT IS AVAILABLE ***"

print(""" 

 /$$    /$$ /$$                           /$$$$$$              /$$                 /$$                         /$$
| $$   | $$|__/                          /$$__  $$            | $$                | $$                        | $$
| $$   | $$ /$$  /$$$$$$$ /$$$$$$       | $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ | $$
|  $$ / $$/| $$ /$$_____/|____  $$      | $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$| $$
 \  $$ $$/ | $$|  $$$$$$  /$$$$$$$      | $$__  $$| $$  | $$  | $$    | $$  \ $$  | $$    | $$  \ $$| $$  \ $$| $$
  \  $$$/  | $$ \____  $$/$$__  $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$
   \  $/   | $$ /$$$$$$$/  $$$$$$$      | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/  |  $$$$/|  $$$$$$/|  $$$$$$/| $$
    \_/    |__/|_______/ \_______/      |__/  |__/ \______/    \___/   \______/    \___/   \______/  \______/ |__/

                                            CREATED BY ALPHARAOH


DISCLAIMER: Please use this tool reasonably and within the law.
""")

print("Please insert your Gmail credentials")

while True:
    fromaddr = input("\nEmail: ")
    password = getpass.getpass("Password: ")

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        print("\nLogin Successful!")
        break
    except:
        print("\nERROR: Credentials are incorrect. Please try again...")

print("\nScanning time intervals (e.g. 20) = 20 Minutes")

while True:
    try:
        timeInput = float(input(">>>"))
        break
    except:
        print("ERROR: Please ensure you are typing a correct input")

timeInput *= 60

print("""
Choose application category:

1:  Certificate of life (attestatie de vita)
2:  Copy conform original (NL passport, ID card or driving license)
3:  DigID
4:  Identity card, first time application for a minor
5:  Identity card, first time application for an adult
6:  Identity card, renewal for a minor
7:  Identity card, renewal for an adult
8:  Legalisation of a signature
9:  Legalisation of documents
10: MVV – visa for long stay (>90 days)
11: Option request
12: Passport, first time application for a minor
13: Passport, first time application for an adult
14: Passport, renewal for a minor
15: Passport, renewal for an adult
""")
catNumber = int(input("Category number: "))

while catNumber not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    print("ERROR: Please ensure you are typing a correct input (It is the number to the left of the category)")
    catNumber = int(input("Category number: "))


def loopFunction():
    checkAvailability()


def startTimer():
    threading.Timer(timeInput, startTimer).start()
    loopFunction()


def sendEmail():
    toaddrs = fromaddr
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(fromaddr, password)
        print("Sending mail...")
        server.sendmail(fromaddr, toaddrs, gmailMsg)
        print("Mail sent.")
        time.sleep(3)
        startTimer()
    except:
        print("\nLogin unsuccessful, try again.")


def checkAvailability():
    print("\nChecking Availability...")
    site = "https://www.vfsvisaonline.com/Netherlands-Global-Online-Appointment_Zone2/AppScheduling/AppWelcome.aspx?P=b0KsiJlv+LIdjKDvIvW+nLNY7GnUFdfuwQj4DXbs4vo="
    path = "/Users/AkaamMAC/Documents/Appointment_checker_na/chromedriver"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(path, options=chrome_options)
    driver.get(site)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "plhMain_lnkSchApp")))
        driver.find_element_by_id("plhMain_lnkSchApp").click()
        Select(driver.find_element_by_id(
            "plhMain_cboVisaCategory")).select_by_index(catNumber)
        driver.find_element_by_id("plhMain_btnSubmit").click()

        if ("No date(s) available for appointment." in driver.page_source):
            print(
                f"\nNO APPOINTMENTS - trying again in {timeInput} seconds...")
        else:
            print(
                "\n********************** APPOINTMENT AVAILABLE **********************\n")
            sendEmail()
    finally:
        driver.quit()


startTimer()
