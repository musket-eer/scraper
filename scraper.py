import re
from linkedin_scraper import Person, actions
from selenium import webdriver


# global vars
driver = webdriver.Chrome()
email = "elpmentor.russel@gmail.com"
password = "one+one=2"
fieldsOfInterest = ["name", "title_description", "location", "about", "experiences", "education", "recommendations"]
expectedBaseUrl = "https://linkedin.com/"


def writeCSV(filename, data):
    log_file = open(filename + ".csv", "a")
    log_file.write(data)
    log_file.close()

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
    while not isValidUrl(profileurl):
        profileurl = input("Ensure you enter a valid Linkedin url: ")
        
    print("You are about to scrape from " + profileurl)
    return profileurl


def login(email, password):
    try:
        actions.login(driver, email, password) 
        print("Login successful")
    except:
        print("Login failed")


def main():
    url = getUrl
    person = Person(url, driver=driver)
    data = scrape(person, fieldsOfInterest)
    destination = input("Enter destination file: ")
    writeCSV(destination, data)


if __name__ == "__main__":
    main()