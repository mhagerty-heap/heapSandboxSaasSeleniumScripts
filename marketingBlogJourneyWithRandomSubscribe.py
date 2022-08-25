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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

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

# randomBlogJourney = 5 # for debugging
randomBlogJourney = random.randint(1,5) # value for determining if success or failure funnel, 1 = success, 2-4 equals failure

if(randomBlogJourney == 1):
    blogIdSelector = "blogGridPost1"
    print("blogIdSelector = blogGridPost1 = Charts")
elif(randomBlogJourney == 2):
    blogIdSelector = "blogGridPost2"
    print("blogIdSelector = blogGridPost2 = Tables")
elif(randomBlogJourney == 3):
    blogIdSelector = "blogGridPost3"
    print("blogIdSelector = blogGridPost3 = NoFuss")
elif(randomBlogJourney == 4):
    blogIdSelector = "blogGridPost4"
    print("blogIdSelector = blogGridPost4 = EarnMoreMoney")
else:
    blogIdSelector = "blogGridPost6"
    print("blogIdSelector = blogGridPost6 = AutoManage")

#randomSubscribe = 15 # for debugging
randomSubscribe = random.randint(1,15) # value for determining if subscribe happens for blog visitor, 6.6% conversion
print("randomSubsribe = " + str(randomSubscribe) + " (15 = conversion)")

# what's the starting URL, in this instance, it's the blog home page
startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/blog-grids.html?utm_source=Blog&utm_medium=referral&utm_campaign=NewBlogPosts&utm_content=PlayBlog&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"

# set Agent String for session
userAgentString = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"

# start webdriver 
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

#Start Session with starting URL
driver.get(startingUrlWithUtmCodes)
print("Open on blog-grids.html")
time.sleep(2)

#set key for session recording, not required but might be useful
driver.execute_script("console.log('heapReplaySession')")
print("heapReplaySession Console Message Sent")

blogPost = driver.find_element(By.ID, blogIdSelector)
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView(true);", blogPost);
print("On blog-grids.html, scrollIntoView blogPost")
time.sleep(2)
webdriver.ActionChains(driver).move_to_element(blogPost).perform()
print("On blog-grids.html, move_to_element blogPost")
time.sleep(2)
blogPost.click()
print("On blog-grids.html, Click blogPost")
time.sleep(2)
blogDetailsMidPageQuote = driver.find_element(By.ID, "blogDetailsMidPageQuote")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView(true);", blogDetailsMidPageQuote);
print("On blog post details page, scrollIntoView blogDetailsMidPageQuote")
time.sleep(2)
webdriver.ActionChains(driver).move_to_element(blogDetailsMidPageQuote).perform()
print("On blog post details page, move_to_element blogDetailsMidPageQuote")
time.sleep(2)

# conversions steps
if (randomSubscribe == 15):
    signUpButton = driver.find_element(By.ID, "mainSignUpLink")
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", signUpButton);
    print("On blog post details page, scrollIntoView signUpButton")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(signUpButton).perform()
    print("On blog post details page, move_to_element blogDetailsMidPageQuote")
    time.sleep(2)
    signUpButton.click()
    time.sleep(2)
    print("On blog post details page, click sign up signUpButton")

    # on sign-up page, select randomly selected plan from above and subscribe
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    time.sleep(2)
    driver.find_element(By.ID, planRadioSelection).click()
    print("On SignUp Page, click random planRadioSelection input value")
    time.sleep(2)
    signUpNameField = driver.find_element(By.ID, 'signUpNameField')
    webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
    driver.find_element(By.ID, "signUpNameField").send_keys(customerName)
    print("On SignUp Page, enter Name Field")
    time.sleep(2)   
    signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
    webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
    driver.find_element(By.ID, "signUpEmailField").send_keys(customerEmail)
    print("On SignUp Page, enter Email Field")
    time.sleep(2)   
    signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
    webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
    driver.find_element(By.ID, "signUpPasswordField").send_keys(customerPassword)
    print("On SignUp Page, enter Password Field")
    time.sleep(2)   
    signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
    webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
    driver.find_element(By.ID, "signUpStreetAddressField").send_keys(customerStreetAddress)
    print("On SignUp Page, enter Street Address Field")
    time.sleep(2)   
    signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
    webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
    driver.find_element(By.ID, "signUpZipCodeField").send_keys(customerPostalCode)
    print("On SignUp Page, enter Postal Code")
    time.sleep(2)   
    signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
    webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
    driver.find_element(By.ID, "signUpMobileNumberField").send_keys(customerMobileNumber)
    print("On SignUp Page, enter Mobile Number")
    time.sleep(2)   
    creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
    webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
    driver.find_element(By.ID, "creditCardNumberField").send_keys(customerCreditCardNumber)
    print("On SignUp Page, enter Credit Card Number")
    time.sleep(2)   
    creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
    webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
    driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
    print("On SignUp Page, enter Expiration Date (hardcoded)")
    time.sleep(2)
    creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
    webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
    driver.find_element(By.ID, "creditCardCodeField").send_keys(customerCreditCardCode)
    print("On SignUp Page, enter Credit Card Code")
    time.sleep(2)
    connectWith = driver.find_element(By.ID, 'connectWith')
    webdriver.ActionChains(driver).move_to_element(connectWith).perform()
    print("On SignUp Page, move to connectWith")
    signUpButton = driver.find_element(By.ID, 'signUpButton')
    signUpButton.click()
    print("On SignUp Page, click signUpButton")

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
    print("Send Offline Subscription Event")

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
    print("Send Offline User Property: Account - Account Name")

time.sleep(3)
driver.delete_all_cookies()
driver.quit()
print("blogJourney Complete")