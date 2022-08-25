import time
import json
import random
import http.client
import datetime
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

scriptRunTimestamp = datetime.datetime.now()
print("scriptRunTimestamp = " + str(scriptRunTimestamp))

heapEnv = "527942070"
print("Heap envID = " + heapEnv)

# open heapProspectPersonas.json file, randomly selected 1 out of 1000 personas, populate persona variables
randomPersonaSelector = random.randint(0,999) # used to select from the 1000 fake personas within heapProspectPersonas.json
with open('heapProspectPersonas.json', 'r') as f: # open file from same dir where script runs
  customerData = json.load(f)

# set customer variables based on data imported from heapProspectPersonas.json
customerName = customerData[randomPersonaSelector]['customerName']
print("customerName = " + customerName)
customerEmail = customerData[randomPersonaSelector]['customerEmail']
print("customerEmail = " + customerEmail)
customerPassword = customerData[randomPersonaSelector]['customerPassword']
print("customerPassword = " + customerPassword)
customerStreetAddress = customerData[randomPersonaSelector]['customerStreetAddress']
print("customerStreetAddress = " + customerStreetAddress)
customerPostalCode = str(customerData[randomPersonaSelector]['customerPostalCode'])
print("customerPostalCode = " + customerPostalCode)
customerMobileNumber = customerData[randomPersonaSelector]['customerMobileNumber']
print("customerMobileNumber = " + customerMobileNumber)
customerCreditCardNumber = customerData[randomPersonaSelector]['customerCreditCardNumber']
print("customerCreditCardNumber = " + customerCreditCardNumber)
customerCreditCardCode = str(customerData[randomPersonaSelector]['customerCreditCardCode'])
print("customerCreditCardCode = " + customerCreditCardCode)
customerAccountName = customerData[randomPersonaSelector]['customerAccountName']
print("customerAccountName = " + customerAccountName)

# Grab last digit of time since epoch, and use this to set UTM codes for beginning URL
todaysDate = str(date.today())
timeSinceEpochUtm = time.time()
timeSinceEpochUserAgent = time.time()
randomUTMSelector = str(timeSinceEpochUtm) # used to select UTM codes
randomUserAgentSelector = str(timeSinceEpochUserAgent)
# randomUserAgentSelector = 3
# randomTrafficPatternSelection = random.randint(0,9) # used for selecting UTMS
# print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))
randomEmailVersionSelector = str(random.randint(1, 2))  # used for randomly selecting plans for users, A or B
if randomEmailVersionSelector.endswith('1'):
    emailVersion = 'A'
else:
    emailVersion = 'B'
randomPlanSelector = str(random.randint(1,3)) # used for randomly selecting plans for users, free/pro/enterprise
if(randomPlanSelector.endswith("1")):
	planRadioSelection = "freePlanRadioSelection"
	offlineSubscriptionDescription = 'Free Plan'
elif(randomPlanSelector.endswith("2")):
	planRadioSelection = "proPlanRadioSelection"
	offlineSubscriptionDescription = 'Pro Plan'
else:
	planRadioSelection = "enterprisePlanRadioSelection"
	offlineSubscriptionDescription = 'Enterprise Plan'
print("randomPlanSelector = " + randomPlanSelector)
print("offlineSubscriptionDescription = " + offlineSubscriptionDescription)

# set UTM Codes for starting page
#if randomTrafficPatternSelection is 0 through 9 set UTM code accordingly
if(randomUTMSelector.endswith("1")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
elif(randomUTMSelector.endswith("2")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
elif(randomUTMSelector.endswith("3")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Facebook&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew&sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
elif(randomUTMSelector.endswith("4")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Twitter&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew&sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
elif(randomUTMSelector.endswith("5")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Blog&utm_medium=referral&utm_campaign=NewArticles&utm_content=BeTheBestSaaS&sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
elif(randomUTMSelector.endswith("6")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=LinkedIn&utm_medium=display&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1&sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
elif(randomUTMSelector.endswith("7")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Google&utm_medium=cpc&utm_campaign=SponsortedContent&utm_content=NewProductFeatures&sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
elif(randomUTMSelector.endswith("8")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=EmailList1&utm_medium=email&utm_campaign=UpgradePath&utm_content=TryNewFeatures&sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
elif(randomUTMSelector.endswith("9")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Affiliate&utm_medium=referral&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1&sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"
else:
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html&sessionReplay=true&sessionReplayName=marketingSubscribeFeaturesHesitation"

# set user agent string
userAgentString = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"

# set webdriver options for Selenium session
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=' + userAgentString)

# start webdriver
driver = webdriver.Chrome(options = options)

# set user agent
user_agent = driver.execute_script("return navigator.userAgent;")
print("selected userAgentString = " + userAgentString)
print("returned user_agent from Chromedriver = " + user_agent) # print user agent from browser

# set browser window position, size, wait time
driver.set_window_position(0, 0)
driver.set_window_size(1280, 1020)
#driver.maximize_window()
print(driver.get_window_size())
driver.implicitly_wait(10)
driver.get(startingUrlWithUtmCodes) # start session with starting URL
time.sleep(1)

#turn on session replay console message
driver.execute_script("console.log('heapReplaySession')") # run command in console to key off some value if necessary
print("heapReplaySession Console Message Sent")
time.sleep(1)

#grab and print heap.userid to script
heapUserId = driver.execute_script("var heapUserId = heap.userId; return heapUserId;") # run command in console to key off some value if necessary
print("heapUserId = " + heapUserId)
time.sleep(1)

#Start of traffic pattern at homepage
print("Step1: Go to Homepage: " + startingUrlWithUtmCodes)
time.sleep(2)
# find pages dropdown menu
pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
# click on pages dropdown menu to open it for next click
webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
time.sleep(2)
# find features page from pages dropdown and click it. This same pattern is used multiple times within this script
pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
time.sleep(2)
pagesFeaturesLink.click()
print("Step2: On Homepage, Click Features")

#on features page, scroll down page, find pricing link and click it
time.sleep(2)
featuresDivText = driver.find_element(By.ID, 'featuresDivText')
driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
time.sleep(2)
featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
time.sleep(2)
featuresPricingLink1.click()
print("Step3: On Features page, Click featuresPricingLink1")
time.sleep(2)

# on pricing page
pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
#pricingTableText = driver.find_element(By.ID, 'pricingTableText')
driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
time.sleep(2)
# find and move to  pro pbutton
pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
print("Step4: On Pricing page, Move to Pro Plan pricing")
time.sleep(1)
# find and move to free button
pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
print("Step5: On Pricing page, Move to Free Plan pricing")
time.sleep(1)
# find and move to enterprise button
pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
print("Step6: On Pricing page, Move to Enterprise Plan pricing")
time.sleep(1)
# find and pro button
pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
print("Step7: On Pricing page, Move to Pro Plan pricing")
time.sleep(2)
# click on pro pricing button
webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
time.sleep(2)
pricingProPurchaseNowButton.click()
print("Step8: On Pricing page, Click Pro Plan Purchase Now Button")
time.sleep(2) #15

# on sign-up page, click between pricing buttons
signUpNameField = driver.find_element(By.ID, 'signUpNameField')
driver.execute_script("arguments[0].scrollIntoView()", signUpNameField)
time.sleep(2)
# click free plan
freePlanRadioSelection = driver.find_element(By.ID, 'freePlanRadioSelection')
freePlanRadioSelection.click()
print("Step9: On Signup Page, Click Free Plan Radio Button")
time.sleep(1)
# click pro plan
proPlanRadioSelection = driver.find_element(By.ID, 'proPlanRadioSelection')
proPlanRadioSelection.click()
print("Step10: On Signup Page, Click Pro Plan Radio Button")
time.sleep(1)
# click enterprise plan
enterprisePlanRadioSelection = driver.find_element(By.ID, 'enterprisePlanRadioSelection')
enterprisePlanRadioSelection.click()
print("Step11: On Signup Page, Click Enterprise Plan Radio Button")
time.sleep(1)
# on sign-up page, find and go back to features page
pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
# click on pages dropdown menu to open it for next click
webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
time.sleep(2)
# find features page from pages dropdown and click it.
pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
time.sleep(2)
pagesFeaturesLink.click()
print("Step12: On Signup Page, Go back to Features Page")
time.sleep(2)

# on features page, move mouse across each feature div
# scroll down the page to make features more visible
featuresDivText = driver.find_element(By.ID, 'featuresDivText')
driver.execute_script("arguments[0].scrollIntoView()", featuresDivText)
time.sleep(2)
# move mouse to feature div 1
featureDiv1 = driver.find_element(By.ID, 'featureDiv1')
webdriver.ActionChains(driver).move_to_element(featureDiv1).perform()
print("Step13: On Features Page, move mouse to featureDiv1")
time.sleep(2)
# Move mouse across each feature div
featureDiv2 = driver.find_element(By.ID, 'featureDiv2')
webdriver.ActionChains(driver).move_to_element(featureDiv2).perform()
print("Step14: On Features Page, move mouse to featureDiv2")
time.sleep(2)
# Move mouse across each feature div
featureDiv3 = driver.find_element(By.ID, 'featureDiv3')
webdriver.ActionChains(driver).move_to_element(featureDiv3).perform()
print("Step15: On Features Page, move mouse to featureDiv3")
time.sleep(2)
# Move mouse across each feature div
featureDiv4 = driver.find_element(By.ID, 'featureDiv4')
webdriver.ActionChains(driver).move_to_element(featureDiv4).perform()
print("Step16: On Features Page, move mouse to featureDiv4")
time.sleep(2)
# click on first pricing link
featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
time.sleep(2)
featuresPricingLink1.click()
print("Step17: On Features Page, click featuresPricingLink1")
time.sleep(2)

# on pricing page, click on pro plan
pricingDiv = driver.find_element(By.CSS_SELECTOR, '#pricing > div > div.flex.flex-wrap.items-center.justify-center')
#pricingTableText = driver.find_element(By.ID, 'pricingTableText')
driver.execute_script("arguments[0].scrollIntoView()", pricingDiv)
time.sleep(2)
# find and click pro pbutton
pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
time.sleep(2)
pricingProPurchaseNowButton.click()
print("Step18: On Features Page, click pricingProPurchaseNowButton")
time.sleep(2)

# on sign-up page, select pro plan and subscribe
creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
time.sleep(2)
driver.find_element(By.ID, planRadioSelection).click()
print("Step19: On SignUp Page, click random planRadioSelection input value")
time.sleep(2)
signUpNameField = driver.find_element(By.ID, 'signUpNameField')
webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
driver.find_element(By.ID, "signUpNameField").send_keys(customerName)
print("Step20: On SignUp Page, enter Name Field")
time.sleep(2)
signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
driver.find_element(By.ID, "signUpEmailField").send_keys(customerEmail)
print("Step21: On SignUp Page, enter Email Field")
time.sleep(2)
signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
driver.find_element(By.ID, "signUpPasswordField").send_keys(customerPassword)
print("Step22: On SignUp Page, enter Password Field")
time.sleep(2)
signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
driver.find_element(By.ID, "signUpStreetAddressField").send_keys(customerStreetAddress)
print("Step23: On SignUp Page, enter Street Address Field")
time.sleep(2)
signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
driver.find_element(By.ID, "signUpZipCodeField").send_keys(customerPostalCode)
print("Step24: On SignUp Page, enter Postal Code")
time.sleep(2)
signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
driver.find_element(By.ID, "signUpMobileNumberField").send_keys(customerMobileNumber)
print("Step25: On SignUp Page, enter Mobile Number")
time.sleep(2)
creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
driver.find_element(By.ID, "creditCardNumberField").send_keys(customerCreditCardNumber)
print("Step26: On SignUp Page, enter Credit Card Number")
time.sleep(2)
creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
print("Step27: On SignUp Page, enter Expiration Date (hardcoded)")
time.sleep(2)
creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
driver.find_element(By.ID, "creditCardCodeField").send_keys(customerCreditCardCode)
print("Step28: On SignUp Page, enter Credit Card Code")
time.sleep(2)
connectWith = driver.find_element(By.ID, 'connectWith')
webdriver.ActionChains(driver).move_to_element(connectWith).perform()
print("Step29: On SignUp Page, move to connectWith")
signUpButton = driver.find_element(By.ID, 'signUpButton')
signUpButton.click()
print("Step30: On SignUp Page, click signUpButton")

# make API call back to Heap for custom offline subscription event
subscribeConn = http.client.HTTPSConnection('heapanalytics.com')
headers = {'Content-type': 'application/json'}
subscribeHeapTrackJson = {
    'app_id': heapEnv,
    'identity': customerEmail,
    'event': 'Subscription',
    'properties': {'Backend Subscription Date': '' + todaysDate + '', 'Backend Subscription Level': '' + offlineSubscriptionDescription + '', 'Backend AccountName': '' + customerAccountName + ''},
}
subscribe_json_data = json.dumps(subscribeHeapTrackJson)
subscribeConn.request('POST', '/api/track', subscribe_json_data, headers)
time.sleep(1)
print("Step31: Send Offline Subscription Event")

# make API call back to Heap for custom user properties, specifically Account - Account Name
addUserPropConn = http.client.HTTPSConnection('heapanalytics.com')
headers = {'Content-type': 'application/json'}
addUserPropsHeapTrackJson = {
    'app_id': heapEnv,
    'identity': customerEmail,
    'properties': {'Account - Account Name': '' + customerAccountName + ''},
}
addUserProps_json_data = json.dumps(addUserPropsHeapTrackJson)
addUserPropConn.request('POST', '/api/add_user_properties', addUserProps_json_data, headers)
time.sleep(1)
print("Step32: Send Offline User Property: Account - Account Name")

# make API call to show transactional email sent
emailConn = http.client.HTTPSConnection('heapanalytics.com')
headers = {'Content-type': 'application/json'}
emailHeapTrackJson = {
    'app_id': heapEnv,
    'identity': customerEmail,
    'event': 'Send Transactional Email',
    'properties': {'Transactional Email Subject': 'This Month with Play!', 'Transactional Email Variation': '' + emailVersion + ''},
}
email_json_data = json.dumps(emailHeapTrackJson)
emailConn.request('POST', '/api/track', email_json_data, headers)
time.sleep(1)
print("Step33: Send Offline Email Event")
time.sleep(5)

# delete all cookies and quit chrome session
driver.delete_all_cookies()
driver.quit()
