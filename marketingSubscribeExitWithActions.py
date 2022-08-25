import time
import datetime
import json
import random
import http.client
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


scriptRunTimestamp = datetime.datetime.now()
print("scriptRunTimestamp = " + str(scriptRunTimestamp))

# set some initial variables
# Grab last digit of time since epoch, and use this to set UTM codes for beginning URL
todaysDate = str(date.today())
timeSinceEpochUtm = time.time()
timeSinceEpochUserAgent = time.time()
randomUTMSelector = str(timeSinceEpochUtm)  # used to select UTM codes
randomUserAgentSelector = str(timeSinceEpochUserAgent)
randomTrafficPatternSelection = random.randint(0, 9)  # used for selecting traffic pattern
randomTimeSleepInterval = random.randint(2, 4)  # used for time.sleep(randomTimeSleepInterval) between steps
# generate random user ID
randomUserSelector = str(random.randint(1, 1000))  # used for creating a customerxxxx@gmail address for entry into form
randomUserEmail = 'customer' + randomUserSelector + '@gmail.com'

randomPlanSelector = str(random.randint(1, 3))  # used for randomly selecting plans for users, free/pro/enterprise
if randomPlanSelector.endswith('1'):
    planRadioSelection = 'freePlanRadioSelection'
elif randomPlanSelector.endswith('2'):
    planRadioSelection = 'proPlanRadioSelection'
else:
    planRadioSelection = 'enterprisePlanRadioSelection'

# set UTL Codes for starting page, if randomTrafficPatternSelection is 0 through 9 set UTM code accordingly
if(randomUTMSelector.endswith("1")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
elif(randomUTMSelector.endswith("2")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
elif(randomUTMSelector.endswith("3")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Facebook&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew&sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
elif(randomUTMSelector.endswith("4")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Twitter&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew&sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
elif(randomUTMSelector.endswith("5")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Blog&utm_medium=referral&utm_campaign=NewArticles&utm_content=BeTheBestSaaS&sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
elif(randomUTMSelector.endswith("6")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=LinkedIn&utm_medium=display&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1&sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
elif(randomUTMSelector.endswith("7")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Google&utm_medium=cpc&utm_campaign=SponsortedContent&utm_content=NewProductFeatures&sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
elif(randomUTMSelector.endswith("8")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=EmailList1&utm_medium=email&utm_campaign=UpgradePath&utm_content=TryNewFeatures&sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
elif(randomUTMSelector.endswith("9")):
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Affiliate&utm_medium=referral&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1&sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"
else:
    startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html&sessionReplay=true&sessionReplayName=marketingSubscribeExitWithActions"

# set user agent string
userAgentString = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"

# start webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=' + userAgentString)
driver = webdriver.Chrome(options = options)

# set userAgent, and print results
user_agent = driver.execute_script("return navigator.userAgent;")
print("selected userAgentString = " + userAgentString)
print("returned user_agent from Chromedriver = " + user_agent)

# set more browser and session properties
driver.set_window_position(0, 0)
driver.set_window_size(1280, 1080)
#driver.maximize_window()
print(driver.get_window_size())
driver.implicitly_wait(10)
driver.get(startingUrlWithUtmCodes)  # request starting URL
time.sleep(1)

# set potentially useful console message for session replay
driver.execute_script("console.log('heapReplaySession')")
print("heapReplaySession Console Message Sent")
time.sleep(1)

#randomTrafficPatternSelection = 9 # to test specific traffic patterns, comment our if not in use for testing

# Start of traffic patterns,
# Homepage -> About -> Pricing -> Team -> SignUp Event -> Exit
if randomTrafficPatternSelection == 0:
    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> About -> Pricing -> Team -> SignUp Event -> Exit")
    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(randomTimeSleepInterval)

    mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
    webdriver.ActionChains(driver).move_to_element(mainAboutLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainAboutLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(randomTimeSleepInterval)
    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(randomTimeSleepInterval)
    mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
    webdriver.ActionChains(driver).move_to_element(mainTeamLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainTeamLink.click()
    time.sleep(randomTimeSleepInterval)

    # at homepage
    time.sleep(2)
    # find pages dropdown menu
    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(randomTimeSleepInterval)
    pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
    # click on pages dropdown menu to open it for next click
    webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
    time.sleep(3)
    # find features page from pages dropdown and click it.
    pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
    webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
    time.sleep(3)
    pagesFeaturesLink.click()
    time.sleep(2)

    # on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    #pricingTableText = driver.find_element(By.ID, 'pricingTableText')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro button
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(2)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    # on sign-up page
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

# Homepage -> Features -> Pricing -> Signup  Event -> Exit
elif randomTrafficPatternSelection == 1:
    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> Features -> Pricing -> Signup  Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(2)
    mainHomeLink.click()
    time.sleep(5)

    midFeaturesTop = driver.find_element(By.ID, 'midFeaturesTop')
    driver.execute_script("arguments[0].scrollIntoView()", midFeaturesTop)
    time.sleep(2)
    featuresLink1 = driver.find_element(By.ID, 'featuresLink1')
    webdriver.ActionChains(driver).move_to_element(featuresLink1).perform()
    time.sleep(2)
    featuresLink1.click()
    time.sleep(2)

    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(2)
    mainPricingLink.click()
    time.sleep(2)

    # at homepage
    time.sleep(2)
    # find pages dropdown menu
    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
    # click on pages dropdown menu to open it for next click
    webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
    time.sleep(3)
    # find features page from pages dropdown and click it.
    pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
    webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
    time.sleep(3)
    pagesFeaturesLink.click()

    #on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    #pricingTableText = driver.find_element(By.ID, 'pricingTableText')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(1)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(1)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(1)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    # on sign-up page
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

# Homepage -> Pricing -> About -> Contact -> Team -> SignUp Event -> Exit
elif randomTrafficPatternSelection == 2:
    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> Pricing -> About -> Contact -> Team -> SignUp Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(5)

    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
    webdriver.ActionChains(driver).move_to_element(mainAboutLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainAboutLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainContactLink = driver.find_element(By.ID, 'mainContactLink')
    webdriver.ActionChains(driver).move_to_element(mainContactLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainContactLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
    webdriver.ActionChains(driver).move_to_element(mainTeamLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainTeamLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
    webdriver.ActionChains(driver).move_to_element(mainSignUpLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainSignUpLink.click()
    time.sleep(5)

    # on signup page
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    driver.delete_all_cookies()
    driver.quit()

# Homepage -> Team -> About -> Pricing -> Contact -> Signup Event -> Exit
elif randomTrafficPatternSelection == 3:
    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> Team -> About -> Pricing -> Contact -> Signup Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(5)

    mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
    webdriver.ActionChains(driver).move_to_element(mainTeamLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainTeamLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
    webdriver.ActionChains(driver).move_to_element(mainAboutLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainAboutLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainContactLink = driver.find_element(By.ID, 'mainContactLink')
    webdriver.ActionChains(driver).move_to_element(mainContactLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainContactLink.click()
    time.sleep(randomTimeSleepInterval)

    # at homepage
    time.sleep(2)
    # find pages dropdown menu
    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
    # click on pages dropdown menu to open it for next click
    webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
    time.sleep(3)
    # find features page from pages dropdown and click it.
    pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
    webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
    time.sleep(3)
    pagesFeaturesLink.click()

    #on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    #pricingTableText = driver.find_element(By.ID, 'pricingTableText')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(1)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(1)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(1)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    # on signup page
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

# Homepage -> About -> Pricing -> Team -> Contact -> Signup Event -> Exit
elif randomTrafficPatternSelection == 4:
    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> About -> Pricing -> Team -> Contact -> Signup Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(5)

    mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
    webdriver.ActionChains(driver).move_to_element(mainAboutLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainAboutLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
    webdriver.ActionChains(driver).move_to_element(mainTeamLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainTeamLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainContactLink = driver.find_element(By.ID, 'mainContactLink')
    webdriver.ActionChains(driver).move_to_element(mainContactLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainContactLink.click()
    time.sleep(randomTimeSleepInterval)

    # at homepage
    time.sleep(2)
    # find pages dropdown menu
    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
    # click on pages dropdown menu to open it for next click
    webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
    time.sleep(3)
    # find features page from pages dropdown and click it.
    pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
    webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
    time.sleep(3)
    pagesFeaturesLink.click()

    #on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    #pricingTableText = driver.find_element(By.ID, 'pricingTableText')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(1)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(1)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(1)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    # on sign-up page
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

#Homepage -> About -> Pricing -> Contact -> Team -> Signup -> Features Page -> Pricing Page -> Signup Event -> Exit
elif randomTrafficPatternSelection == 5:

    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> About -> Pricing -> Contact -> Team -> Signup -> Features Page -> Pricing Page -> Signup Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(5)

    mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
    webdriver.ActionChains(driver).move_to_element(mainAboutLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainAboutLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainContactLink = driver.find_element(By.ID, 'mainContactLink')
    webdriver.ActionChains(driver).move_to_element(mainContactLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainContactLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
    webdriver.ActionChains(driver).move_to_element(mainTeamLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainTeamLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
    webdriver.ActionChains(driver).move_to_element(mainSignUpLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainSignUpLink.click()
    time.sleep(5)

    # at signup page
    time.sleep(2)
    pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
    # click on pages dropdown menu to open it for next click
    webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
    time.sleep(3)
    # find features page from pages dropdown and click it.
    pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
    webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
    time.sleep(3)
    pagesFeaturesLink.click()

    #on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(1)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(1)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(1)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    # on sigup page
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

#Homepage -> Contact -> Pricing -> Team -> About -> Pricing -> Features -> Pricing -> Signup Event -> Exit
elif randomTrafficPatternSelection == 6:

    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> Contact -> Pricing -> Team -> About -> Pricing -> Features -> Pricing -> Signup Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(5)

    mainContactLink = driver.find_element(By.ID, 'mainContactLink')
    webdriver.ActionChains(driver).move_to_element(mainContactLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainContactLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
    webdriver.ActionChains(driver).move_to_element(mainTeamLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainTeamLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(mainAboutLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainAboutLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(2)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    midFeaturesTop = driver.find_element(By.ID, 'midFeaturesTop')
    driver.execute_script("arguments[0].scrollIntoView()", midFeaturesTop)
    time.sleep(2)
    featuresLink1 = driver.find_element(By.ID, 'featuresLink1')
    webdriver.ActionChains(driver).move_to_element(featuresLink1).perform()
    time.sleep(2)
    featuresLink1.click()

    #on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    #pricingTableText = driver.find_element(By.ID, 'pricingTableText')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(1)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(1)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(1)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    # on signup page
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

# Homepage -> About -> Pricing -> Signup Event -> Exit
elif randomTrafficPatternSelection == 7:

    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> About -> Pricing -> Signup Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(5)

    mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
    webdriver.ActionChains(driver).move_to_element(mainAboutLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainAboutLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    midFeaturesTop = driver.find_element(By.ID, 'midFeaturesTop')
    driver.execute_script("arguments[0].scrollIntoView()", midFeaturesTop)
    time.sleep(2)
    featuresLink1 = driver.find_element(By.ID, 'featuresLink1')
    webdriver.ActionChains(driver).move_to_element(featuresLink1).perform()
    time.sleep(2)
    featuresLink1.click()

    #on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(1)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(1)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(1)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    # on signup page
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

# Homepage -> Pricing -> Signup Event -> Exit
elif randomTrafficPatternSelection == 8:

    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> Pricing -> Signup Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(5)

    mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
    webdriver.ActionChains(driver).move_to_element(mainPricingLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainPricingLink.click()
    time.sleep(randomTimeSleepInterval)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    midFeaturesTop = driver.find_element(By.ID, 'midFeaturesTop')
    driver.execute_script("arguments[0].scrollIntoView()", midFeaturesTop)
    time.sleep(2)
    featuresLink1 = driver.find_element(By.ID, 'featuresLink1')
    webdriver.ActionChains(driver).move_to_element(featuresLink1).perform()
    time.sleep(2)
    featuresLink1.click()

    #on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    #pricingTableText = driver.find_element(By.ID, 'pricingTableText')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(1)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(1)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(1)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

# Homepage -> Features -> SignUp Event -> Exit
else:

    print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
    print("Homepage -> Features -> SignUp Event -> Exit")

    mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
    webdriver.ActionChains(driver).move_to_element(mainHomeLink).perform()
    time.sleep(randomTimeSleepInterval)
    mainHomeLink.click()
    time.sleep(5)

    driver.execute_script("arguments[0].scrollIntoView()", mainHomeLink)
    time.sleep(2)
    midFeaturesTop = driver.find_element(By.ID, 'midFeaturesTop')
    driver.execute_script("arguments[0].scrollIntoView()", midFeaturesTop)
    time.sleep(2)
    featuresLink1 = driver.find_element(By.ID, 'featuresLink1')
    webdriver.ActionChains(driver).move_to_element(featuresLink1).perform()
    time.sleep(2)
    featuresLink1.click()

    #on features page, scroll down page, find pricing link and click it
    time.sleep(2)
    featuresDivText = driver.find_element(By.ID, 'featuresDivText')
    driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
    time.sleep(2)
    featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
    webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
    time.sleep(2)
    featuresPricingLink1.click()
    time.sleep(2)

    # on pricing page
    pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
    #pricingTableText = driver.find_element(By.ID, 'pricingTableText')
    driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
    time.sleep(2)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(1)
    # find and click free button
    pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
    time.sleep(1)
    # find and click enterprise button
    pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
    time.sleep(1)
    # find and click pro pbutton
    pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    # click on pro pricing button
    webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
    time.sleep(2)
    pricingProPurchaseNowButton.click()
    time.sleep(2) #15

    # on signup page
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
    time.sleep(2)
    driver.find_element(By.ID, "proPlanRadioSelection").click()
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys("Sally Smith")
    time.sleep(2)
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
    time.sleep(2)
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
    time.sleep(2)
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
    time.sleep(2)
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
    time.sleep(2)
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
    time.sleep(2)
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
    time.sleep(2)
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()

print("subscribeExitWIthActions Complete")
