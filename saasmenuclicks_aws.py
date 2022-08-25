import time
import json
import random
#from selenium import webdriver
from aws_synthetics.selenium import synthetics_webdriver as webdriver
from aws_synthetics.selenium import synthetics_webdriver
from aws_synthetics.common import synthetics_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def saasmenuclicks():

  featureListbyLinkName = ["Form Layout", "Input", "Crud", "Float Label", "Invalid State", "Button", "Table", "List", "Tree", "Panel", "Overlay", "Media", "Menu", "Message", "File", "Chart", "Misc"]
  randomNumberOfFeaturesToClick = random.randint(1,10) # used for determining number of features to click, randomly select 1 through 10
  randomListOfFeatures = random.sample(featureListbyLinkName, randomNumberOfFeaturesToClick) # random select X number of features from the total list of features
  print(randomListOfFeatures) # print randomListOfFeatures
  synthetics_logger.info(randomListOfFeatures)

  driver = webdriver.Chrome()
  driver.get("https://heap-sandbox-saas.vercel.app/signin.html")
  driver.set_window_size(1024, 768)
  driver.find_element(By.ID, "signInButton").click()
  time.sleep(2)

  # cycle through randomListOfFeatures and click on each within the lefthand menu
  for x in randomListOfFeatures:
    print(x)
    driver.find_element(By.LINK_TEXT, x).click()
    time.sleep(2)
  driver.delete_all_cookies()
  driver.quit()

def handler(event, context): # used for canary runs wrapped in a function
  return saasmenuclicks()


  # reference for all of the clicks in the main top menu on the lefthand side
  # driver.find_element(By.LINK_TEXT, "Form Layout").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Input").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Float Label").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Invalid State").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Button").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Table").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "List").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Tree").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Panel").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Overlay").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Media").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Menu").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Message").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "File").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Chart").click()
  # time.sleep(2)
  # driver.find_element(By.LINK_TEXT, "Misc").click()
  # time.sleep(2)