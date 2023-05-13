#!bin/env/python3

# Module imports: os, requests, selenium, webdriver
import os
import requests as connect                  
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from screeninfo import get_monitors
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

class DetermineURL:
    defaultURL = "https://femalefreelancedevelopers.com/submit"
    def __init__(self, URL=defaultURL):
        self.URL = URL
    def get(self):
        return self.URL
    def set(self, newURL):
        self.URL = newURL
class SetupBrowser:
    def __init__(self):
        pass
    def Safari(self, URL):
        commandEnableSafari = "safaridriver --enable && echo 'Enabling Safari driver.'"
        os.system( commandEnableSafari )
        browser = webdriver.Safari()
        browser.get( URL )
        return browser
    def Brave(self):
        driverMethod = ChromeDriverManager( chrome_type=ChromeType.BRAVE ).install()
        driver = webdriver.Chrome( service=BraveService( driverMethod ) )
class SessionInformation:
    def __init__(self, browser):
        self.browser = browser
    def view(self):
        print("Session information\n")
        print("platform:", self.browser.capabilities['platformName'])
        print("session id:", self.browser.session_id)
        print("browser:", self.browser.name )
        print("browser @:", self.browser.title )
        print("current url:", self.browser.current_url )
        print("window handle:", self.browser.window_handles )
        print("cookies:", self.browser.get_cookies())
class NetworkInformation:
    def __init(self, browser):
        self.browser = browser
    def view(self):
        # Global Network 
        print("Network status:\n")
        print("airplane mode:", browser.mobile.ALL_NETWORK.airplane_mode )
        print("wifi active:", browser.mobile.ALL_NETWORK.wifi )
        print("data services:", browser.mobile.ALL_NETWORK.data )
class Display:
    def __init__(self):
        self.display = get_monitors()[0]
    def windowPosition( self, browser ):
        defaultWidth = self.display.width / 2
        defaultHeight = 0
        browser.set_window_position( defaultWidth, defaultHeight)
    def windowSize( self, browser, widthValue=1074, heightValue=1342 ):
        browser.set_window_size( widthValue, heightValue )

class FillForm:
    def __init__(self, firstName, lastName, email, website, location, expertise, socialURL):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.website = website
        self.location = location
        self.expertise = expertise
        self.socialURL = socialURL
    def run(self, browser):
        browser.find_element( By.ID, "firstName" ).send_keys( self.firstName + Keys.INSERT )
        browser.find_element( By.ID, "lastName" ).send_keys( self.lastName + Keys.INSERT )
        browser.find_element( By.ID, "email" ).send_keys( self.email + Keys.INSERT )
        browser.find_element( By.ID, "website" ).send_keys( self.website + Keys.INSERT )
        browser.find_element( By.ID, "location" ).send_keys( self.location + Keys.INSERT )
        browser.find_element( By.ID, "expertise" ).send_keys( self.expertise + Keys.INSERT )
        browser.find_element( By.ID, "socialUrl" ).send_keys( self.socialURL + Keys.INSERT )
        browser.implicitly_wait(0.5)
        # browser.find_element( By.CSS_SELECTOR, "button" ).send_keys( Keys.ENTER )
        # browser.refresh()

if __name__ == "__main__":
    url = DetermineURL()
    browserSetup = SetupBrowser()
    browser = browserSetup.Safari( url.get() )
    sessionInfo = SessionInformation( browser )
    sessionInfo.view()
    display = Display()
    display.windowPosition( browser )
    display.windowSize( browser )
    fillForm = FillForm("test", "test", "test", "test", "test", "test", "test" )
    pageSource = browser.page_source
    with open("test.html", "w") as file:
        file.write(pageSource) 
