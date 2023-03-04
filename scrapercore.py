import re
import json
import sys
import time
import json
import csv

sys.path.append('../scraper')

from linkedin_scraper.linkedin_scraper import Person, actions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# global vars
driver = webdriver.Chrome()
email = "elpmentor.russel@gmail.com"
password = "one+one=2"
fieldsOfInterest = ["name", "job_title", "location", "about", "experiences", "educations", "recommendations"]
expectedBaseUrl = "https://linkedin.com/in/"


def writeCSV(filename, data):
   
    data_file = open(filename + ".csv", 'w', newline='')
    
    header = "Scraping Results for " + data[0][1] + "\n"
    data_file.write(header)

    # datum is a list in the form [section, description]
    for datum in data:
       data_file.write(str(datum[0]) + "\n")
       data_file.write(str(datum[1]) + "\n \n \n")

    data_file.close()

# scrape information from given titles of what to scrape from the person object
def scrape(person, fields):
    aStr = ""
    for item in fields:
        aStr += person.item + "\n"

    return aStr


# gets the url of the profile from the terminal
def isValidUrl(url):
    return expectedBaseUrl in url
    

def getUrl():
    profileurl = input("Enter desired url: ")
    # while not isValidUrl(profileurl):
        # profileurl = input("Ensure you enter a valid Linkedin url: ")
        
    print("You are about to scrape from " + profileurl)
    return profileurl

def getPerson(url):
    psn = Person(url, driver=driver)
    time.sleep(5)
    attrs = []
    attrs.append(psn.name)
    attrs.append(psn.job_title)
    attrs.append(psn.location)
    attrs.append(psn.about)
    attrs.append(psn.experiences)
    attrs.append(psn.educations)
    attrs.append(psn.accomplishments)

    sections = []
    for i in range(len(fieldsOfInterest)):
        section = [fieldsOfInterest[i]]
        section.append(attrs[i])
        sections.append(section)
    
    return sections


def login(email, password):
    try:
        actions.login(driver, email, password) 
        print("Login successful")
    except:
        print("Login failed")


def main():
    login(email, password)
    url = getUrl()
    personData = getPerson(url)
    destination = input("Enter destination file: ")
    writeCSV(destination, personData)

def mainTest():
    login(email, password)
    url = getUrl()
    person = getPerson(url)
    print(person)


if __name__ == "__main__":
    main()
    # mainTest()