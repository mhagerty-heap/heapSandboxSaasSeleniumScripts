import time
import json
import random
import http.client
import datetime
from datetime import date
from selenium import webdriver
#from aws_synthetics.selenium import synthetics_webdriver as webdriver
#from aws_synthetics.selenium import synthetics_webdriver
#from aws_synthetics.common import synthetics_logger
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

# open heapCustomerPersonas.json file, randomly selected 1 out of 1000 personas, populate persona variables
randomPersonaSelector = random.randint(0,999) # used to select from the 1000 fake personas within heapCustomerPersonas.json
with open('heapCustomerPersonas.json', 'r') as f: # open file from same dir where script runs
  customerData = json.load(f)
# set customer variables based on data imported from heapCustomerPersonas.jsom
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

randomSaasFeatureSelection = random.randint(1,16) # value for determining which feature to interact with
#randomSaasFeatureSelection = 13 # used for debugging

# set UTM Codes for starting page
startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/signin.html?sessionReplay=true&sessionReplayName=saasAppJourneyWithActions"

# set Agent String for session
# if randomTrafficPatternSelection is 0 through 9 set user agent code accordingly
userAgentString = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"

# start webdriver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
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

#make API call back to Heap for custom user properties, specifically Account - Account Name
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
print("Sent Offline User Properties, Account Name, Customer Name, Subscribed Plan")

#Start of Feature Interactions
#Form Layout
#Enters first ane last name test data in the Inline FirstName LastName fields and 1 out of 4 selects Submit button
if(randomSaasFeatureSelection == 1):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Form Layout")
    feature = driver.find_element(By.LINK_TEXT, "Form Layout")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    print("Clicked Form Layout Lefthand Menu")
    time.sleep(2)
    inlineFirstName = driver.find_element(By.ID, "firstname1")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(inlineFirstName).perform()
    print("move_to_element Form Layout inlineFirstName")
    time.sleep(2)
    inlineFirstName.click()
    print("Click Form Layout inlineFirstName")
    time.sleep(2)
    inlineFirstName.send_keys("firstname")
    print("Enter value in Form Layout inlineFirstName")
    time.sleep(2)
    inlineLastName = driver.find_element(By.ID, "lastname1")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(inlineLastName).perform()
    print("move_to_element Form Layout inlineLastName")
    time.sleep(2)
    inlineLastName.click()
    print("Click Form Layout inlineLastName")
    time.sleep(2)
    inlineLastName.send_keys("lastname")
    print("Enter value in Form Layout inlineLastName")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select Submit button")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select the Submit button
        print("randomAdditionalAction = 4, so additional Submit Button will be selected")
        inlineButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(2) > div:nth-child(2) > div > button > span.p-button-label.p-c")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(inlineButton).perform()
        print("move_to_element Form Layout inlineButton")
        time.sleep(2)
        inlineButton.click()
        print("Click Form Layout inlineButton")
        time.sleep(2)

#Input
#Scrolls down page and selects SelectButton Option1 & Option2 & 1 out of 4 selects Option3
elif(randomSaasFeatureSelection == 2):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Input")
    feature = driver.find_element(By.LINK_TEXT, "Input")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    selectButtonLabel = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(2) > div:nth-child(3) > h5:nth-child(3)")
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", selectButtonLabel);
    print("Scroll to Input selectButtonLabel to be able to see Option buttons")
    time.sleep(2)
    option1 = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(option1).perform()
    print("move_to_element SelectButton option1")
    time.sleep(2)
    option1.click()
    print ("Click SelectButton option1")
    time.sleep(2)
    option2 = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > span.p-button-label.p-c")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(option2).perform()
    print("move_to_element SelectButton option1")
    time.sleep(2)
    option2.click()
    print ("Click SelectButton option2")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select Option3 button")
    #randomAdditionalAction = 1 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select the Options3 button
        print("randomAdditionalAction = 4, so additional Option3 button will be selected")
        option3 = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(3) > span.p-button-label.p-c")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(option3).perform()
        print("move_to_element SelectButton option1")
        time.sleep(2)
        option3.click()
        print ("Click SelectButton option3")
        time.sleep(2)

#Float Label
#Selects New York and Rome from MultiSelect menu, 1 out of 4 then closes menu
elif(randomSaasFeatureSelection == 3):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Float Label")
    feature = driver.find_element(By.LINK_TEXT, "Float Label")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    multiSelectMenu = driver.find_element(By.CSS_SELECTOR, "#multiselect > div.p-multiselect-label-container")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(multiSelectMenu).perform()
    print("move_to_element multiSelectMenu")
    time.sleep(2)
    multiSelectMenu.click()
    print ("Click multiSelectMenu")
    time.sleep(2)
    newYork = driver.find_element(By.CSS_SELECTOR, "body > div.p-multiselect-panel.p-component.p-connected-overlay-enter-done > div.p-multiselect-items-wrapper > ul > li:nth-child(1)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(newYork).perform()
    print("move_to_element New York")
    time.sleep(2)
    newYork.click()
    print ("Click New York")
    time.sleep(2)
    rome = driver.find_element(By.CSS_SELECTOR, "body > div.p-multiselect-panel.p-component.p-connected-overlay-enter-done > div.p-multiselect-items-wrapper > ul > li:nth-child(2)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(rome).perform()
    print("move_to_element Rome")
    time.sleep(2)
    rome.click()
    print ("Click Rome")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select close menu button")
    #randomAdditionalAction = 1 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select the close button
        closeButton = driver.find_element(By.CSS_SELECTOR, "body > div.p-multiselect-panel.p-component.p-connected-overlay-enter-done > div.p-multiselect-header > button")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(closeButton).perform()
        print("move_to_element multiSelect closeButton")
        time.sleep(2)
        closeButton.click()
        print ("Click multiSelect closeButton")
        time.sleep(2)

#Invalid State
#Selects New York and Rome from MultiSelect menu, then 1 out of 4 closes menu
elif(randomSaasFeatureSelection == 4):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Invalid State")
    feature = driver.find_element(By.LINK_TEXT, "Invalid State")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    multiSelectMenu = driver.find_element(By.CSS_SELECTOR, "#multiselect > div.p-multiselect-label-container")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(multiSelectMenu).perform()
    print("move_to_element multiSelectMenu")
    time.sleep(2)
    multiSelectMenu.click()
    print ("Click multiSelectMenu")
    time.sleep(2)
    newYork = driver.find_element(By.CSS_SELECTOR, "body > div.p-multiselect-panel.p-component.p-connected-overlay-enter-done > div.p-multiselect-items-wrapper > ul > li:nth-child(1)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(newYork).perform()
    print("move_to_element New York")
    time.sleep(2)
    newYork.click()
    print ("Click New York")
    time.sleep(2)
    rome = driver.find_element(By.CSS_SELECTOR, "body > div.p-multiselect-panel.p-component.p-connected-overlay-enter-done > div.p-multiselect-items-wrapper > ul > li:nth-child(2)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(rome).perform()
    print("move_to_element Rome")
    time.sleep(2)
    rome.click()
    print ("Click Rome")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select close menu button")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select the close button
        closeButton = driver.find_element(By.CSS_SELECTOR, "body > div.p-multiselect-panel.p-component.p-connected-overlay-enter-done > div.p-multiselect-header > button")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(closeButton).perform()
        print("move_to_element multiSelect closeButton")
        time.sleep(2)
        closeButton.click()
        print ("Click multiSelect closeButton")
        time.sleep(2)

#Button
#Select Outlined primary and secondary buttons, and 1 out of 4 will also select the danger button
elif(randomSaasFeatureSelection == 5):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Button")
    feature = driver.find_element(By.LINK_TEXT, "Button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    outlinedPrimaryButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div:nth-child(4) > button:nth-child(2)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(outlinedPrimaryButton).perform()
    print("move_to_element outlinedPrimaryButton")
    time.sleep(2)
    outlinedPrimaryButton.click()
    print ("Click outlinedPrimaryButton")
    time.sleep(2)
    outlinedSecondaryButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div:nth-child(4) > button.p-button.p-component.p-button-outlined.p-button-secondary.mr-2.mb-2")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(outlinedSecondaryButton).perform()
    print("move_to_element outlinedSecondaryButton")
    time.sleep(2)
    outlinedSecondaryButton.click()
    print ("Click outlinedSecondaryButton")
    time.sleep(2)
    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select additional Danger button")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select the Danger button
        print("randomAdditionalAction = 4, so additional outlined danger button will be selected")
        outlinedDangerButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div:nth-child(4) > button.p-button.p-component.p-button-outlined.p-button-danger.mr-2.mb-2")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(outlinedDangerButton).perform()
        print("move_to_element outlinedDangerButton")
        time.sleep(2)
        outlinedDangerButton.click()
        print ("Click outlinedDangerButton")
        time.sleep(2)

#Table
# selects filter under name, enters Art under Search by name, then Apply, then filter again, then 1 out of 4 will clear
elif(randomSaasFeatureSelection == 6):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Table")
    feature = driver.find_element(By.LINK_TEXT, "Table")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    filterButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > div.p-datatable-wrapper > table > thead > tr > th:nth-child(1) > div > div > button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(filterButton).perform()
    print("move_to_element filterButton")
    time.sleep(2)
    filterButton.click()
    print ("Click filterButton")
    searchByNameField = driver.find_element(By.CSS_SELECTOR, "body > div.p-column-filter-overlay.p-component.p-fluid.p-column-filter-overlay-menu.p-connected-overlay-enter-done > div.p-column-filter-constraints > div > input")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(searchByNameField).perform()
    print("move_to_element searchByNameField")
    time.sleep(2)
    searchByNameField.click()
    print ("Click searchByNameField")
    time.sleep(2)
    searchByNameField.send_keys("Art")
    print("Type Art in searchByNameField")
    applyButton = driver.find_element(By.CSS_SELECTOR, "body > div.p-column-filter-overlay.p-component.p-fluid.p-column-filter-overlay-menu.p-connected-overlay-enter-done > div.p-column-filter-buttonbar > button:nth-child(2)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(applyButton).perform()
    print("move_to_element applyButton")
    time.sleep(2)
    applyButton.click()
    print ("Click applyButton")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will clear the selection")
    #randomAdditionalAction = 1 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also clear the selection
        filterButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > div.p-datatable-wrapper > table > thead > tr > th:nth-child(1) > div > div > button")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(filterButton).perform()
        print("move_to_element filterButton")
        time.sleep(2)
        filterButton.click()
        print ("Click filterButton")
        clearButton = driver.find_element(By.CSS_SELECTOR, "body > div.p-column-filter-overlay.p-component.p-fluid.p-column-filter-overlay-menu.p-connected-overlay-enter-done > div.p-column-filter-buttonbar > button.p-button.p-component.p-button-outlined.p-button-sm")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(clearButton).perform()
        print("move_to_element clearButton")
        time.sleep(2)
        clearButton.click()
        print ("Click clearButton")
        time.sleep(2)

#List
# scrolls to bottom of screen, selects filter all button, then 1 out of 4 will select the unfilterall button
elif(randomSaasFeatureSelection == 7):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", List")
    feature = driver.find_element(By.LINK_TEXT, "List")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    pickListLabel = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div.col-12.lg\\:col-8 > div > h5")
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", pickListLabel);
    filterAllButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div.col-12.lg\\:col-8 > div > div > div.p-picklist-buttons.p-picklist-transfer-buttons > button:nth-child(2)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(filterAllButton).perform()
    print("move_to_element filterAllButton")
    time.sleep(2)
    filterAllButton.click()
    print("Click filterAllButton")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select unfilterAllButton")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select unfilterAllButton
        unfilterAllButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div.col-12.lg\\:col-8 > div > div > div.p-picklist-buttons.p-picklist-transfer-buttons > button:nth-child(4)")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(unfilterAllButton).perform()
        print("move_to_element unfilterAllButton")
        time.sleep(2)
        unfilterAllButton.click()
        time.sleep(2)
        print ("Click unfilterAllButton")

#Tree
# selects all documents and expands the tree, and then does the same for events, and then 1 out of 4 will do this for and movies
elif(randomSaasFeatureSelection == 8):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Tree")
    feature = driver.find_element(By.LINK_TEXT, "Tree")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    selectAllDocumentsButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > ul > li:nth-child(1) > div > div > div")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(selectAllDocumentsButton).perform()
    print("move_to_element selectAllDocumentsButton")
    time.sleep(2)
    selectAllDocumentsButton.click()
    print ("Click selectAllDocumentsButton")
    time.sleep(2)
    expandAllDocumentsButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > ul > li:nth-child(1) > div > button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(expandAllDocumentsButton).perform()
    print("move_to_element expandAllDocumentsButton")
    time.sleep(2)
    expandAllDocumentsButton.click()
    print ("Click expandAllDocumentsButton")
    time.sleep(2)
    selectAllEventsButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > ul > li:nth-child(2) > div > div > div")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(selectAllEventsButton).perform()
    print("move_to_element selectAllEventsButton")
    time.sleep(2)
    selectAllEventsButton.click()
    print ("Click selectAllEventsButton")
    time.sleep(2)
    expandAllEventsButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > ul > li:nth-child(2) > div > button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(expandAllEventsButton).perform()
    print("move_to_element expandAllEventsButton")
    time.sleep(2)
    expandAllEventsButton.click()
    print ("Click expandAllEventsButton")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select and expand movies")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select and expand movies
        selectAllMoviesButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > ul > li:nth-child(3) > div > div > div")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(selectAllMoviesButton).perform()
        print("move_to_element selectAllMoviesButton")
        time.sleep(2)
        selectAllMoviesButton.click()
        print ("Click selectAllMoviesButton")
        time.sleep(2)
        expandAllMoviesButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > ul > li:nth-child(3) > div > button")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(expandAllMoviesButton).perform()
        print("move_to_element expandAllMoviesButton")
        time.sleep(2)
        expandAllMoviesButton.click()
        print ("Click expandAllMoviesButton")
        time.sleep(2)

#Panel
# expands header2 and 1 out of 4 will expand header3
elif(randomSaasFeatureSelection == 9):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Panel")
    feature = driver.find_element(By.LINK_TEXT, "Panel")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(3)
    expandHeaderTwo = driver.find_element(By.CSS_SELECTOR, "#pr_id_3 > div:nth-child(2)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(expandHeaderTwo).perform()
    print("move_to_element expandHeaderTwo")
    time.sleep(2)
    expandHeaderTwo.click()
    print ("Click expandHeaderTwo")
    time.sleep(3)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select and expand header3")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select and expand header3
        expandHeaderThree = driver.find_element(By.CSS_SELECTOR, "#pr_id_3 > div:nth-child(3)")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(expandHeaderThree).perform()
        print("move_to_element expandHeaderThree")
        time.sleep(2)
        expandHeaderThree.click()
        print ("Click expandHeaderThree")
        time.sleep(2)

#Overlay
# opens DataTable, sorts by price, 1/4 will close DataTable window
elif(randomSaasFeatureSelection == 10):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Overlay")
    feature = driver.find_element(By.LINK_TEXT, "Overlay")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    dataTable = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div.grid > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(dataTable).perform()
    print("move_to_element dataTable")
    time.sleep(2)
    dataTable.click()
    time.sleep(2)
    print ("Click dataTable")
    sortByPrice = driver.find_element(By.CSS_SELECTOR, "#overlay_panel > div > div > div.p-datatable-wrapper > table > thead > tr > th:nth-child(3)")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(sortByPrice).perform()
    print("move_to_element sortByPrice")
    time.sleep(2)
    sortByPrice.click()
    print ("Click sortByPrice")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will close DataTable modal")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also close DataTable modal
        closeDataTable = driver.find_element(By.CSS_SELECTOR, "#overlay_panel > button")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(closeDataTable).perform()
        print("move_to_element closeDataTable")
        time.sleep(2)
        closeDataTable.click()
        print ("Click closeDataTable")
        time.sleep(2)

#Media
#Scroll carousel to the right 2 times, 1/4 will click for a third time
elif(randomSaasFeatureSelection == 11):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Media")
    feature = driver.find_element(By.LINK_TEXT, "Media")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    rightArrowCarouselButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > div > div > div > button.p-carousel-next.p-link")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(rightArrowCarouselButton).perform()
    print("move_to_element rightArrowCarouselButton")
    time.sleep(2)
    rightArrowCarouselButton.click()
    print ("Click rightArrowCarouselButton")
    time.sleep(2)
    rightArrowCarouselButton.click()
    print ("Click rightArrowCarouselButton")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will close DataTable modal")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also close DataTable modal
        rightArrowCarouselButton.click()
        print ("Click rightArrowCarouselButton")
        time.sleep(2)

#Menu
# Select 1 then 2 then 3 then 1/4 will select 4
elif(randomSaasFeatureSelection == 12):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Menu")
    feature = driver.find_element(By.LINK_TEXT, "Menu")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    oneButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(3) > div > div.p-steps.p-component > ul > li.p-steps-item.p-highlight.p-steps-current > a > span.p-steps-number")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(oneButton).perform()
    print("move_to_element oneButton")
    time.sleep(2)
    oneButton.click()
    print ("Click oneButton")
    time.sleep(2)
    twoButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(3) > div > div.p-steps.p-component > ul > li:nth-child(2) > a > span.p-steps-number")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(twoButton).perform()
    print("move_to_element twoButton")
    time.sleep(2)
    twoButton.click()
    print ("Click twoButton")
    time.sleep(2)
    threeButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(3) > div > div.p-steps.p-component > ul > li:nth-child(3) > a > span.p-steps-number")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(threeButton).perform()
    print("move_to_element threeButton")
    time.sleep(2)
    threeButton.click()
    print ("Click threeButton")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select 4th option")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select 4th option
        fourButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(3) > div > div.p-steps.p-component > ul > li:nth-child(4) > a > span.p-steps-number")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(fourButton).perform()
        print("move_to_element fourButton")
        time.sleep(2)
        fourButton.click()
        print ("Click fourButton")
        time.sleep(2)

#Message
# Select Toast Success then Info then Warn then 1/4 will select Error
elif(randomSaasFeatureSelection == 13):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Message")
    feature = driver.find_element(By.LINK_TEXT, "Message")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    toastSuccessButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > button.p-button.p-component.p-button-success.mr-2")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(toastSuccessButton).perform()
    print("move_to_element toastSuccessButton")
    time.sleep(2)
    toastSuccessButton.click()
    print ("Click toastSuccessButton")
    time.sleep(2)
    toastInfoButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > button.p-button.p-component.p-button-info.mr-2")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(toastInfoButton).perform()
    print("move_to_element toastInfoButton")
    time.sleep(2)
    toastInfoButton.click()
    print ("Click toastInfoButton")
    time.sleep(2)
    toastWarnButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > button.p-button.p-component.p-button-warning.mr-2")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(toastWarnButton).perform()
    print("move_to_element toastWarnButton")
    time.sleep(2)
    toastWarnButton.click()
    print ("Click toastWarnButton")
    time.sleep(2)

    randomAdditionalAction = random.randint(1,4)
    print("randomAdditionalAction = " + str(randomAdditionalAction) + ", 4 will select 4th option")
    #randomAdditionalAction = 4 # for debugging
    if(randomAdditionalAction == 4): # if 4 is the random number, also select 4th option
        toastErrorButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(1) > div > button.p-button.p-component.p-button-danger.mr-2")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(toastErrorButton).perform()
        print("move_to_element toastErrorButton")
        time.sleep(2)
        toastErrorButton.click()
        print ("Click toastErrorButton")
        time.sleep(2)

#File
#Select Advanced Choose button
elif(randomSaasFeatureSelection == 14):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", File")
    feature = driver.find_element(By.LINK_TEXT, "File")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    advancedChooseButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div > div > div.p-fileupload.p-fileupload-advanced.p-component > div.p-fileupload-buttonbar > span")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(advancedChooseButton).perform()
    print("move_to_element advancedChooseButton")
    time.sleep(2)
    advancedChooseButton.click()
    print ("Click advancedChooseButton")
    time.sleep(2)

#Misc
#Select emails button, then messages button
elif(randomSaasFeatureSelection == 15):
    print("randomSaasFeatureSelection = " + str(randomSaasFeatureSelection) + ", Misc")
    feature = driver.find_element(By.LINK_TEXT, "Misc")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(feature).perform()
    time.sleep(2)
    feature.click()
    time.sleep(2)
    emailsButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(2) > div:nth-child(1) > button.p-button.p-component.mr-2")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(emailsButton).perform()
    print("move_to_element emailsButton")
    time.sleep(2)
    emailsButton.click()
    print ("Click emailsButton")
    time.sleep(2)
    messagesButton = driver.find_element(By.CSS_SELECTOR, "#root > div > div.layout-main-container > div.layout-main > div > div:nth-child(2) > div:nth-child(1) > button.p-button.p-component.p-button-warning")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(messagesButton).perform()
    print("move_to_element messagesButton")
    time.sleep(2)
    messagesButton.click()
    print ("Click messagesButton")
    time.sleep(2)

#Cog wheel UI Menu
#Open cog wheel ui, select 2-3 bootstrap buttons, select close cog wheel
else:
    cogWheel = driver.find_element(By.CSS_SELECTOR, "#layout-config-button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(cogWheel).perform()
    print("move_to_element cogWheel")
    time.sleep(2)
    cogWheel.click()
    print ("Click cogWheel")
    time.sleep(2)

    boostrapButtonOne = driver.find_element(By.CSS_SELECTOR, "#layout-config > div > div:nth-child(11) > div:nth-child(2) > button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(boostrapButtonOne).perform()
    print("move_to_element boostrapButtonOne")
    time.sleep(2)
    boostrapButtonOne.click()
    print ("Click boostrapButtonOne")
    time.sleep(2)

    boostrapButtonTwo = driver.find_element(By.CSS_SELECTOR, "#layout-config > div > div:nth-child(11) > div:nth-child(3) > button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(boostrapButtonTwo).perform()
    print("move_to_element boostrapButtonTwo")
    time.sleep(2)
    boostrapButtonTwo.click()
    print ("Click boostrapButtonTwo")
    time.sleep(2)

    boostrapButtonThree = driver.find_element(By.CSS_SELECTOR, "#layout-config > div > div:nth-child(11) > div:nth-child(4) > button")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(boostrapButtonThree).perform()
    print("move_to_element boostrapButtonThree")
    time.sleep(2)
    boostrapButtonThree.click()
    print ("Click boostrapButtonThree")
    time.sleep(2)

    closeCogMenuButton = driver.find_element(By.CSS_SELECTOR, "#layout-config > button.p-button.p-component.p-button-danger.layout-config-close.p-button-rounded.p-button-text.p-button-icon-only")
    time.sleep(2)
    webdriver.ActionChains(driver).move_to_element(closeCogMenuButton).perform()
    print("move_to_element closeCogMenuButton")
    time.sleep(2)
    closeCogMenuButton.click()
    print ("Click closeCogMenuButton")
    time.sleep(2)

driver.delete_all_cookies()
driver.quit()
print("Journey Complete")
