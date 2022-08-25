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

# set customer variables based on data imported from heapProspectPersonas.jsom
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

#set some variables
# Grab last digit of time since epoch, and use this to set UTM codes for beginning URL
todaysDate = str(date.today())
timeSinceEpochUtm = time.time()
randomUTMSelector = str(timeSinceEpochUtm) # used to select UTM codes
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

# set UTL Codes for starting page
#if randomTrafficPatternSelection is 0 through 9 set UTM code accordingly
if(randomUTMSelector.endswith("1")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
elif(randomUTMSelector.endswith("2")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
elif(randomUTMSelector.endswith("3")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Facebook&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew&sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
elif(randomUTMSelector.endswith("4")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Twitter&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew&sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
elif(randomUTMSelector.endswith("5")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Blog&utm_medium=referral&utm_campaign=NewArticles&utm_content=BeTheBestSaaS&sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
elif(randomUTMSelector.endswith("6")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=LinkedIn&utm_medium=display&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1&sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
elif(randomUTMSelector.endswith("7")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Google&utm_medium=cpc&utm_campaign=SponsortedContent&utm_content=NewProductFeatures&sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
elif(randomUTMSelector.endswith("8")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=EmailList1&utm_medium=email&utm_campaign=UpgradePath&utm_content=TryNewFeatures&sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
elif(randomUTMSelector.endswith("9")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Affiliate&utm_medium=referral&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1&sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"
else:
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html&sessionReplay=true&sessionReplayName=marketingSubscribe_lessClicks"

userAgentString = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"

#print and logging statements for script variables prior to browser instantiation
print("randomPlanSelector value = " + str(randomPlanSelector))
print("planRadioSelection = " + planRadioSelection)

# start webdriver for Selenium session
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=' + userAgentString)

driver = webdriver.Chrome(options = options)

user_agent = driver.execute_script("return navigator.userAgent;")
print("selected userAgentString = " + userAgentString)
print("returned user_agent from Chromedriver = " + user_agent)

driver.set_window_position(0, 0)
driver.set_window_size(1280, 1080)
#driver.maximize_window()
print(driver.get_window_size())
driver.implicitly_wait(10)
driver.get(startingUrlWithUtmCodes)
time.sleep(1)
print("Homepage: " + startingUrlWithUtmCodes)
driver.execute_script("console.log('heapReplaySession')")
print("heapReplaySession Console Message Sent")
time.sleep(1)

#grab and print heap.userid to script
heapUserId = driver.execute_script("var heapUserId = heap.userId; return heapUserId;") # run command in console to key off some value if necessary
print("heapUserId = " + heapUserId)
time.sleep(1)

#Start of traffic pattern
# at homepage
# define homepage elements
midFeaturesTop = driver.find_element(By.ID, 'midFeaturesTop')
featuresLink1 = driver.find_element(By.ID, 'featuresLink1')
featuresLink2 = driver.find_element(By.ID, 'featuresLink2')
featuresLink3 = driver.find_element(By.ID, 'featuresLink3')
featuresLink4 = driver.find_element(By.ID, 'featuresLink4')
midAboutUsTop = driver.find_element(By.ID, 'midAboutUsTop')
aboutUsLearnMoreButton = driver.find_element(By.ID, 'aboutUsLearnMoreButton')
midPricingTop = driver.find_element(By.ID, 'midPricingTop')
pricingFreePurchaseNowButton = driver.find_element(By.ID, 'pricingFreePurchaseNowButton')
pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
pricingEnterprisePurchaseNowButton = driver.find_element(By.ID, 'pricingEnterprisePurchaseNowButton')
midFaqTop = driver.find_element(By.ID, 'midFaqTop')
faqQuestion4 = driver.find_element(By.ID, 'faqQuestion4')
midTestimonialsTop = driver.find_element(By.ID, 'midTestimonialsTop')
midOurTeamTop = driver.find_element(By.ID, 'midOurTeamTop')
midContactTop = driver.find_element(By.ID, 'midContactTop')

#homepage actions
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView()", midFeaturesTop)
print("Step1: On Homepage, scrollIntoView() to midFeaturesTop")
print("Step2: On Homepage, Scroll to midFeaturesTop")
time.sleep(2) #20
webdriver.ActionChains(driver).move_to_element(featuresLink1).perform()
print("Step3: On Homepage, move_to_element featuresLink1")
time.sleep(2)
webdriver.ActionChains(driver).move_to_element(featuresLink2).perform()
print("Step4: On Homepage, move_to_element featuresLink2")
time.sleep(2)
webdriver.ActionChains(driver).move_to_element(featuresLink3).perform()
print("Step5: On Homepage, move_to_element featuresLink3")
time.sleep(2)
webdriver.ActionChains(driver).move_to_element(featuresLink4).perform()
print("Step6: On Homepage, move_to_element featuresLink4")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView()", midAboutUsTop)
print("Step7: On Homepage, scrollIntoView() to midAboutUsTop")
time.sleep(2) #20
webdriver.ActionChains(driver).move_to_element(aboutUsLearnMoreButton).perform()
print("Step8: On Homepage, move_to_element aboutUsLearnMoreButton")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView()", midPricingTop)
print("Step9: On Homepage, scrollIntoView() to midPricingTop")
time.sleep(2) #20
webdriver.ActionChains(driver).move_to_element(pricingFreePurchaseNowButton).perform()
print("Step10: On Homepage, move_to_element pricingFreePurchaseNowButton")
time.sleep(2) #20
webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
print("Step11: On Homepage, move_to_element pricingProPurchaseNowButton")
time.sleep(2) #20
webdriver.ActionChains(driver).move_to_element(pricingEnterprisePurchaseNowButton).perform()
print("Step12: On Homepage, move_to_element pricingEnterprisePurchaseNowButton")
time.sleep(2) #20
driver.execute_script("arguments[0].scrollIntoView()", midFaqTop)
print("Step13: On Homepage, scrollIntoView() to midFaqTop")
time.sleep(2) #20
webdriver.ActionChains(driver).move_to_element(faqQuestion4).perform()
print("Step14: On Homepage, Move Mouse to faqQuestion4")
time.sleep(2) #20
faqQuestion4.click()
print("Step15: On Homepage, Click faqQuestion4")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView()", midTestimonialsTop)
print("Step16: On Homepage, scrollIntoView() to midTestimonialTop")
time.sleep(2) #20
driver.execute_script("arguments[0].scrollIntoView()", midOurTeamTop)
print("Step17: On Homepage, scrollIntoView() to midOurTeamTop")
time.sleep(2) #20
driver.execute_script("arguments[0].scrollIntoView()", midContactTop)
print("Step18: On Homepage, scrollIntoView() to midContactTop")
time.sleep(2) #10
driver.execute_script("arguments[0].scrollIntoView()", midPricingTop)
print("Step19: On Homepage, scrollIntoView() to midPricingTop")
time.sleep(2) #10
webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
print("Step20 On Homepage, move_to_element pricingProPurchaseNowButton")
time.sleep(2)
pricingProPurchaseNowButton.click()
print("Step21: On Homepage, click pricingProPurchaseNowButton")
time.sleep(1)

#on sign-up page, sign up
creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
print("Step22: On Signup Page, move_to_element to creditCardExpirationField")
time.sleep(1)
driver.find_element(By.ID, planRadioSelection).click()
print("Step23:On Signup Page, Clicked " + planRadioSelection)
time.sleep(2)
signUpNameField = driver.find_element(By.ID, 'signUpNameField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
print("Step24: On Signup Page, move_to_element signUpNameField")
time.sleep(1)
driver.find_element(By.ID, "signUpNameField").send_keys(customerName)
print("Step25: On Signup Page, Entered customerName")
time.sleep(2)
signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
print("Step26: On Signup Page, move_to_element signUpEmailField")
time.sleep(1)
driver.find_element(By.ID, "signUpEmailField").send_keys(customerEmail)
print("Step27: On Signup Page, Entered customerEmail")
time.sleep(2)
signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
print("Step28: On Signup Page, move_to_element signUpPasswordField")
time.sleep(1)
driver.find_element(By.ID, "signUpPasswordField").send_keys(customerPassword)
print("Step29: On Signup Page, Entered customerPassword")
time.sleep(2)
signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
print("Step30: On Signup Page, move_to_element signUpStreetAddressField")
time.sleep(1)
driver.find_element(By.ID, "signUpStreetAddressField").send_keys(customerStreetAddress)
print("Step31: On Signup Page, Entered customerStreetAddress")
time.sleep(2)
signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
print("Step32: On Signup Page, move_to_element signUpZipCodeField")
time.sleep(1)
driver.find_element(By.ID, "signUpZipCodeField").send_keys(customerPostalCode)
print("Step33: On Signup Page, Entered customerPostalCode")
time.sleep(2)
signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
print("Step34: On SignUp Page, move_to_element signUpMobileNumberField")
time.sleep(1)
driver.find_element(By.ID, "signUpMobileNumberField").send_keys(customerMobileNumber)
print("Step35: On Signup Page, Entered customerMobileNumber")
time.sleep(2)
creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
print("Step36: On Signup Page, move_to_element creditCardNumberField")
time.sleep(1)
driver.find_element(By.ID, "creditCardNumberField").send_keys(customerCreditCardNumber)
print("Step37: On Signup Page, Entered customerCreditCardNumber")
time.sleep(2)
creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
print("Step38: On Signup Page, move_to_element creditCardExpirationField")
time.sleep(1)
driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
print("Step38: On Signup Page, Entered creditCardExpirationField (hard-coded)")
time.sleep(2)
creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
print("Step39: On Signup Page, move_to_element credirCardCodeField")
time.sleep(1)
driver.find_element(By.ID, "creditCardCodeField").send_keys(customerCreditCardCode)
print("Step40: On Signup Page, Entered customerCreditCardCode")
time.sleep(2)
connectWith = driver.find_element(By.ID, 'connectWith')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(connectWith).perform()
print("Step41: On Signup Page, move_to_element connectWith")
time.sleep(1)
signUpButton = driver.find_element(By.ID, 'signUpButton')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signUpButton).perform()
print("Step42: On Signup Page, move_to_element signUpButton")
time.sleep(1)
signUpButton.click()
print("Step43: On Signup Page, click signUpButton")
time.sleep(5)

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

driver.delete_all_cookies()
driver.quit()
