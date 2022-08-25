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

# open heapCustomerPersonas.json file, randomly selected 1 out of 1000 personas, populate persona variables
randomPersonaSelector = random.randint(0,999) # used to select from the 1000 fake personas within heapCustomerPersonas.json
with open('heapCustomerPersonas.json', 'r') as f: # open file from same dir where script runs
  customerData = json.load(f)
# set customer variables based on data imported from heapCustomerPersonas.json 
customerName = customerData[randomPersonaSelector]['customerName']
print("customerName = " + customerName)
customerEmail = customerData[randomPersonaSelector]['customerEmail']
print("customerEmail = " + customerEmail)
customerPassword = customerData[randomPersonaSelector]['customerPassword']
print("customerPassword = " + customerPassword)
customerAccountName = customerData[randomPersonaSelector]['customerAccountName']
print("customerAccountName = " + customerAccountName)
customerSubscribedLevel = customerData[randomPersonaSelector]['customerSubscribedLevel']
print("customerSubscribedLevel = " + customerSubscribedLevel)

randomSaasFunnelPlan = random.randint(1,4) # value for determining if success or failure funnel, 1 = success, 2-4 equals failure
#randomSaasFunnelPlan = 2 # used for debugging
print("randomSaaSFunnelPlan = " + str(randomSaasFunnelPlan) + ", 1=conversion, 2-4=failure")

# set UTM Codes for starting page
startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/signin.html?sessionReplay=true&sessionReplayName=saasAppJourneyWithActions"

# set Agent String for session
# if randomTrafficPatternSelection is 0 through 9 set user agent code accordingly
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
time.sleep(2)

#set key for session recording, not required but might be useful
driver.execute_script("console.log('heapReplaySession')")
print("heapReplaySession Console Message Sent")
time.sleep(2)

# Enter Email Address
signInEmailField = driver.find_element(By.ID, "signInEmailField")
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signInEmailField).perform()
print("Moved to signInEmailField")
time.sleep(1)
signInEmailField.click()
print("Clicked signInEmailField")
time.sleep(1)
signInEmailField.send_keys(customerEmail)
time.sleep(1)
print("Entered signInEmailField")

# Enter Password
signInPasswordField = driver.find_element(By.ID, "signInPasswordField")
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signInPasswordField).perform()
print("Moved to signInPasswordField")
time.sleep(1)
signInPasswordField.click()
print("Clicked signInPasswordField")
time.sleep(1)
signInPasswordField.send_keys(customerPassword)
time.sleep(1)
print("Entered signInPasswordField")

# Click Sign In Button
signInButton = driver.find_element(By.ID, "signInButton")
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(signInButton).perform()
print("Moved to signInButton")
time.sleep(1)
signInButton.click()
print("Clicked signInButton")
time.sleep(3)

#Find and move to the Submenu item below Crud for click visibility
subMenuItem = driver.find_element(By.CSS_SELECTOR, '#root > div > div.layout-sidebar > div > ul > li:nth-child(6) > ul > li:nth-child(1) > a > span:nth-child(2)')
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView(true);", subMenuItem);
print("scrollIntoView subMenuItem")
time.sleep(2)

#Find CRUD component in SaaS App
crudMenuItem = driver.find_element(By.CSS_SELECTOR, '#root > div > div.layout-sidebar > div > ul > li:nth-child(5) > ul > li:nth-child(1) > a > span:nth-child(2)')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(crudMenuItem).perform()
print("Moved to crudMenuItem")
time.sleep(1)
crudMenuItem.click()
print("Clicked crudMenuItem")
time.sleep(1)

# Find New Button, move to it, and click it
crudNewButton = driver.find_element(By.CSS_SELECTOR, '#root > div > div.layout-main-container > div.layout-main > div > div > div > div.p-toolbar.p-component.mb-4 > div.p-toolbar-group-left > div > button.p-button.p-component.p-button-success.mr-2')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(crudNewButton).perform()
print("Moved to crudNewButton")
time.sleep(1)
crudNewButton.click()
print("Clicked crudNewButton")
time.sleep(1)

# Added for SR, if this is not a conversion, remove the description label
if randomSaasFunnelPlan != 1: # if this is not a conversion, remove the description label
    driver.execute_script('descriptionLabel = document.querySelector("#pr_id_6_content > div:nth-child(2) > label"); descriptionLabel.remove()');
    time.sleep(1)
    print("Not a conversion, so removed description label for SR demo")

#Enter Test name into Name Field
crudNewItemName = driver.find_element(By.CSS_SELECTOR, '#name')
webdriver.ActionChains(driver).move_to_element(crudNewItemName).perform()
print("Moved to crudNewItemName")
time.sleep(1)
crudNewItemName.click()
print("Clicked crudNewItemName")
time.sleep(1)
crudNewItemName.send_keys("Test Field Name")
print("Entered crudNewItemName")
time.sleep(1)

# added for SR, if not a conversion click into description and do nothing, otherwise enter a description
if randomSaasFunnelPlan != 1:
    #click into description, but don't enter anything
    crudNewItemDescription = driver.find_element(By.CSS_SELECTOR, '#description')
    time.sleep(1)
    webdriver.ActionChains(driver).move_to_element(crudNewItemDescription).perform()
    print("Moved to crudNewItemDescription")
    time.sleep(1)
    crudNewItemDescription.click()
    time.sleep(3)
    print("Clicked crudNewItemDescription")
else:    
    #Enter Test name into Description Field if this is a conversion
    crudNewItemDescription = driver.find_element(By.CSS_SELECTOR, '#description')
    time.sleep(1)
    webdriver.ActionChains(driver).move_to_element(crudNewItemDescription).perform()
    print("Moved to crudNewItemDescription")
    time.sleep(1)
    crudNewItemDescription.click()
    print("Clicked crudNewItemDescription")
    time.sleep(1)
    crudNewItemDescription.send_keys("Test Field Description")
    time.sleep(1)
    print("Entered crudNewItemDescription")

# Select accessories category in crud menu
crudCategoryAccessoriesCheckmark = driver.find_element(By.CSS_SELECTOR, '#pr_id_6_content > div:nth-child(3) > div > div:nth-child(1) > div > div.p-radiobutton-box')
webdriver.ActionChains(driver).move_to_element(crudCategoryAccessoriesCheckmark).perform()
print("Moved to crudCategoryAccessoriesCheckmark")
time.sleep(1)
crudCategoryAccessoriesCheckmark.click()
print("Clicked crudCategoryAccessoriesCheckmark")
time.sleep(1)

# enter price in crud price field
crudPrice = driver.find_element(By.CSS_SELECTOR, '#price > input')
webdriver.ActionChains(driver).move_to_element(crudPrice).perform()
print("Moved to crudPrice")
time.sleep(1)
webdriver.ActionChains(driver).double_click(crudPrice).perform()
print("double_click crudPrice")
time.sleep(1)
crudPrice.send_keys("10.00")
print("Entered crudPrice")
time.sleep(1)

# enter quantity in crud quantity field
crudQuantity = driver.find_element(By.CSS_SELECTOR, '#quantity > input')
webdriver.ActionChains(driver).move_to_element(crudQuantity).perform()
print("Moved to crudQuantity")
time.sleep(1)
crudQuantity.click()
print("Clicked crudQuantity")
time.sleep(1)
crudQuantity.send_keys("1")
print("Entered crudQuantity")
time.sleep(1)

if randomSaasFunnelPlan == 1: # 1 = success for crud funnel click save button, 2-4 = failure for crud funnel
    print('randomSaaSFunnelPlan = ' + str(randomSaasFunnelPlan) + ', so this will be a successful conversion, 1=success, 2-4=failure')
    # Select Save Button
    crudSaveButton =  driver.find_element(By.CSS_SELECTOR, '#pr_id_6 > div.p-dialog-footer > button:nth-child(2) > span.p-button-label.p-c')
    time.sleep(1)
    webdriver.ActionChains(driver).move_to_element(crudSaveButton).perform()
    print('Moved to crudSaveButton')
    time.sleep(1)
    crudSaveButton.click()
    print("Clicked crudSaveButton")
    time.sleep(2)
    print("CRUD Product Saved")
    dashboardButton = driver.find_element(By.CSS_SELECTOR, '#root > div > div.layout-sidebar > div > ul > li:nth-child(1) > ul > li > a > span:nth-child(2)')
    time.sleep(1)
    webdriver.ActionChains(driver).move_to_element(dashboardButton).perform()
    print("Moved to dashboardButton")
    time.sleep(1)
    dashboardButton.click()
    print("Clicked dashboardButton")
    time.sleep(3)
else:
    # click cancel button
    print('randomSaaSFunnelPlan = ' + str(randomSaasFunnelPlan) + ', so this will be a failed conversion, 1=success, 2-4=failure')
    # Select Cancel Button
    crudCancelButton =  driver.find_element(By.CSS_SELECTOR, '#pr_id_6 > div.p-dialog-footer > button:nth-child(1) > span.p-button-label.p-c')
    time.sleep(1)
    webdriver.ActionChains(driver).move_to_element(crudCancelButton).perform()
    print("Moved to crudCancelButton")
    time.sleep(1)
    crudCancelButton.click()
    print("Clicked crudCancelButton")
    time.sleep(1)
    print("CRUD Product Cancelled")
    dashboardButton = driver.find_element(By.CSS_SELECTOR, '#root > div > div.layout-sidebar > div > ul > li:nth-child(1) > ul > li > a > span:nth-child(2)')
    time.sleep(1)
    webdriver.ActionChains(driver).move_to_element(dashboardButton).perform()
    print("Moved to dashboardButton")
    time.sleep(1)
    dashboardButton.click()
    print("Clicked dashboardButton")
    time.sleep(3)

# make API call back to Heap for custom user properties, specifically Account - Account Name
addUserPropConn = http.client.HTTPSConnection('heapanalytics.com')
headers = {'Content-type': 'application/json'}
addUserPropsHeapTrackJson = {
    'app_id': heapEnv,
    'identity': customerEmail,
    'properties': {'Account - Account Name': '' + customerAccountName + '', 'Account - Customer Name': '' + customerName + '', 'Account - Subscribed Plan': '' + customerSubscribedLevel + ''},
}
addUserProps_json_data = json.dumps(addUserPropsHeapTrackJson)
addUserPropConn.request('POST', '/api/add_user_properties', addUserProps_json_data, headers)
time.sleep(1)
print("Send Offline addUserProperties: Account Name, Customer Name, Subscribed Plan")

print("saasAppJourneyWithActions Complete")
driver.delete_all_cookies()
driver.quit()