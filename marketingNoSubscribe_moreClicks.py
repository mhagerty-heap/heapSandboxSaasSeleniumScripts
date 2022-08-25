import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


#set some variables
# Grab last digit of time since epoch, and use this to set UTM codes for beginning URL
timeSinceEpochUtm = time.time()
timeSinceEpochUserAgent = time.time()
randomUTMSelector = str(timeSinceEpochUtm) # used to select UTM codes
randomUserAgentSelector = str(timeSinceEpochUserAgent)
# randomUserAgentSelector = 3
randomTrafficPatternSelection = random.randint(0,9) # used for selecting traffic pattern

randomTrafficPatternSelection = 0 # used for testing or using specific traffic patterns

randomTimeSleepInterval = random.randint(1,5) # used for time.sleep(randomTimeSleepInterval) between steps
randomUserSelector = str(random.randint(1,1000)) # used for creating a customerxxxx@gmail address for entry into form
randomUserEmail = "customer" + randomUserSelector + "@gmail.com"
randomPlanSelector = str(random.randint(1,3)) # used for randomly selecting plans for users, free/pro/enterprise
if(randomPlanSelector.endswith("1")):
	planRadioSelection = "freePlanRadioSelection" 
elif(randomPlanSelector.endswith("2")):
	planRadioSelection = "proPlanRadioSelection"
else:
	planRadioSelection = "enterprisePlanRadioSelection"

# set UTL Codes for starting page
#if randomTrafficPatternSelection is 0 through 9 set UTM code accordingly
if(randomUTMSelector.endswith("1")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks" 
elif(randomUTMSelector.endswith("2")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"
elif(randomUTMSelector.endswith("3")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Facebook&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"
elif(randomUTMSelector.endswith("4")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Twitter&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"
elif(randomUTMSelector.endswith("5")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Blog&utm_medium=referral&utm_campaign=NewArticles&utm_content=BeTheBestSaaS&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"
elif(randomUTMSelector.endswith("6")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=LinkedIn&utm_medium=display&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"
elif(randomUTMSelector.endswith("7")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Google&utm_medium=cpc&utm_campaign=SponsortedContent&utm_content=NewProductFeatures&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"
elif(randomUTMSelector.endswith("8")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=EmailList1&utm_medium=email&utm_campaign=UpgradePath&utm_content=TryNewFeatures&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"
elif(randomUTMSelector.endswith("9")):
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Affiliate&utm_medium=referral&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"
else:
	startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html&sessionReplay=true&sessionReplayName=NoSubscribe_moreClicks"

# set Agent String for session
# if randomTrafficPatternSelection is 0 through 9 set user agent code accordingly
# if(randomUserAgentSelector.endswith("1")):
# 	userAgentString = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36" 
# elif(randomUserAgentSelector.endswith("2")):
# 	userAgentString = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
# elif(randomUserAgentSelector.endswith("3")):
userAgentString = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
# elif(randomUserAgentSelector.endswith("4")):
# 	userAgentString = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
# elif(randomUserAgentSelector.endswith("5")):
# 	userAgentString = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1"
# elif(randomUserAgentSelector.endswith("6")):
# 	userAgentString = "Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1"
# elif(randomUserAgentSelector.endswith("7")):
# 	userAgentString = "Mozilla/5.0 (iPod; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1"
# elif(randomUserAgentSelector.endswith("8")):
# 	userAgentString = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"
# elif(randomUserAgentSelector.endswith("9")):
# 	userAgentString = "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"
# else:
# 	userAgentString = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"


#print and logging statements for script variables prior to browser instantiation
print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection)) # use on local
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
driver.set_window_size(1280, 1020)
#driver.maximize_window()
print(driver.get_window_size())
driver.implicitly_wait(10)
driver.get(startingUrlWithUtmCodes)
time.sleep(1)
driver.execute_script("console.log('heapReplaySession')")
print("heapReplaySession Console Message Sent")
time.sleep(1)

#Start of traffic pattern
# Home - Features Page - Pricing Page (select Pro) -> 
# SignUp Page (switching between plans) - Features Page -> 
# Blog Grid Page - Blog Article 1 -> 
# Blog Grid Page - Blog Article 2 - Pricing -> 
# Signup - SaaS Page (subscribed)

if (randomTrafficPatternSelection == 0):
	# at homepage
	time.sleep(2)
	# find pages dropdown menu
	pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
	time.sleep(2)
	# click on pages dropdown menu to open it for next click
	webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
	print("Moved to pagesDropDownMenu")
	time.sleep(2)
	# find features page from pages dropdown and click it. This same pattern is used multiple times within this script
	pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
	print("Moved to pagesFeaturesLink")
	time.sleep(2)
	pagesFeaturesLink.click()
	print("Clicked pagesFeaturesLink")
	time.sleep(2)
	featuresPricingLink1 = driver.find_element(By.ID, 'featuresPricingLink1')
	webdriver.ActionChains(driver).move_to_element(featuresPricingLink1).perform()
	print("Moved to featuresPricingLink1")
	time.sleep(2)
	featuresPricingLink1.click()
	print("Clicked featuresPricingLink1")
	time.sleep(2)
	pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
	webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
	print("Moved to pricingProPurchaseNowButton")
	time.sleep(2)
	pricingProPurchaseNowButton.click()
	print("Clicked pricingProPurchaseNowButton")
	time.sleep(2) #15
	driver.find_element(By.ID, "signUpEmailField").click()
	print("Clicked signUpEmailField")
	time.sleep(2)
	creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
	print("Moved to creditCardExpirationField")
	# show confusion by clicking plans multiple times
	driver.find_element(By.ID, "proPlanRadioSelection").click()
	print("Clicked proPlanRadioSelection")
	time.sleep(2)
	driver.find_element(By.ID, "enterprisePlanRadioSelection").click()
	print("Clicked enterprisePlanRadioSelection")
	time.sleep(2)
	driver.find_element(By.ID, "proPlanRadioSelection").click()
	print("Clicked proPlanRadioSelection")
	time.sleep(2) #4
	driver.find_element(By.ID, "enterprisePlanRadioSelection").click()
	print("Clicked enterprisePlanRadioSelection")
	time.sleep(2) #8
	pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
	print("Moved to pagesDropDownMenu")
	time.sleep(2)
	pagesFeaturesLink = driver.find_element(By.ID, 'pagesFeaturesLink')
	webdriver.ActionChains(driver).move_to_element(pagesFeaturesLink).perform()
	print("Moved to pagesFeaturesLink")
	time.sleep(2)
	pagesFeaturesLink.click()
	print("Clicked pagesFEaturesLink")
	time.sleep(2)
	
	pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
	print("Moved to pagesDropDownMenu")
	time.sleep(2)
	pagesBlogGridLink = driver.find_element(By.ID, 'pagesBlogGridLink')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(pagesBlogGridLink).perform()
	print("Moved to pageBlogGridLink")
	time.sleep(2)
	pagesBlogGridLink.click()
	print("Clicked pageBlogGridLink")
	time.sleep(2)
	blogGridPost1 = driver.find_element(By.ID, 'blogGridPost1')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(blogGridPost1).perform()
	print("Moved to blogGridPost1")
	time.sleep(2)
	blogGridPost1.click()
	print("Clicked blogGridPost1")
	blogDetailsMidPageQuote = driver.find_element(By.ID, 'blogDetailsMidPageQuote')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(blogDetailsMidPageQuote).perform()
	print("Moved to blogDetailsMidPageQuote")
	time.sleep(2) #30

	pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
	print("Moved to pagesDropDownMenu")
	time.sleep(2)
	pagesBlogGridLink = driver.find_element(By.ID, 'pagesBlogGridLink')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(pagesBlogGridLink).perform()
	print("Moved to pagesBlogGridLink")
	time.sleep(1)
	pagesBlogGridLink.click()
	print("Clicked pagesBLogGridLink")
	time.sleep(2)
	blogGridPost2 = driver.find_element(By.ID, 'blogGridPost2')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(blogGridPost2).perform()
	print("Moved to blogGridPost2")
	time.sleep(2)
	blogGridPost2.click()
	print("Clicked to blogGridPost2")
	blogDetailsMidPageQuote = driver.find_element(By.ID, 'blogDetailsMidPageQuote')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(blogDetailsMidPageQuote).perform()
	print("Moved to logDetailsMidPageQuote")
	time.sleep(2) #30


	pagesDropDownMenu = driver.find_element(By.ID, 'pagesDropDownMenu')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(pagesDropDownMenu).perform()
	print("Moved to pagesDropDownMenu")
	time.sleep(2)
	pagesPricingLink = driver.find_element(By.ID, 'pagesPricingLink')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(pagesPricingLink).perform()
	print("Moved to pagesPricingLink")
	time.sleep(2)
	pagesPricingLink.click()
	print("Clicked pagesPricingLink")
	time.sleep(2) #10
	pricingProPurchaseNowButton = driver.find_element(By.ID, 'pricingProPurchaseNowButton')
	webdriver.ActionChains(driver).move_to_element(pricingProPurchaseNowButton).perform()
	print("Moved to pricingProPurchaseButton")
	time.sleep(2)
	pricingProPurchaseNowButton.click()
	print("Clicked pricingProPurchaseButton")
	time.sleep(2)
	creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
	time.sleep(2)
	webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
	print("Moved to creditCardExpirationField")
	driver.find_element(By.ID, "proPlanRadioSelection").click()
	print("Clicked proPlanRadioSelection")
	time.sleep(2)
	signUpNameField = driver.find_element(By.ID, 'signUpNameField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(signUpNameField).perform()
	print("Moved to signUpNameField")
	driver.find_element(By.ID, "signUpNameField").send_keys("John Smith")
	print("Entered signUpNameField")
	time.sleep(2)	
	signUpEmailField = driver.find_element(By.ID, 'signUpEmailField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(signUpEmailField).perform()
	time.sleep(1)
	print("Moved to signUpEmailField")
	driver.find_element(By.ID, "signUpEmailField").send_keys("johnsmith@test.com")
	print("Entered signUpEmailField")
	time.sleep(2)	
	signUpPasswordField = driver.find_element(By.ID, 'signUpPasswordField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(signUpPasswordField).perform()
	print("Moved to signUpPasswordField")
	driver.find_element(By.ID, "signUpPasswordField").send_keys("1234")
	print("Entered Password")
	time.sleep(2)	
	signUpStreetAddressField = driver.find_element(By.ID, 'signUpStreetAddressField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(signUpStreetAddressField).perform()
	print("Moved to signUpStreetAddressField")
	driver.find_element(By.ID, "signUpStreetAddressField").send_keys("225 Bush Street")
	print("Entered signUpStreetAddress Field")
	time.sleep(2)	
	signUpZipCodeField = driver.find_element(By.ID, 'signUpZipCodeField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(signUpZipCodeField).perform()
	print("Moved to signUpZipCodeField")
	driver.find_element(By.ID, "signUpZipCodeField").send_keys("94104")
	print("Entered signUpZipCodeField")
	time.sleep(2)	
	signUpMobileNumberField = driver.find_element(By.ID, 'signUpMobileNumberField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(signUpMobileNumberField).perform()
	time.sleep(1)
	print("Moved to signUpMobileNumberField")
	driver.find_element(By.ID, "signUpMobileNumberField").send_keys("1231231234")
	print("Entered signUpMobileNumberField")
	time.sleep(2)	
	creditCardNumberField = driver.find_element(By.ID, 'creditCardNumberField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(creditCardNumberField).perform()
	print("Moved to creditCardNumberField")
	driver.find_element(By.ID, "creditCardNumberField").send_keys("4444444444444444")
	print("Entered creditCardNumberField")
	time.sleep(2)	
	creditCardExpirationField = driver.find_element(By.ID, 'creditCardExpirationField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(creditCardExpirationField).perform()
	print("Moved to creditCardExpirationField")
	driver.find_element(By.ID, "creditCardExpirationField").send_keys("4/26")
	print("Entered creditCardExpirationField")
	time.sleep(2)
	creditCardCodeField = driver.find_element(By.ID, 'creditCardCodeField')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(creditCardCodeField).perform()
	print("Moved to creditCardCodeField")
	driver.find_element(By.ID, "creditCardCodeField").send_keys("123")
	print("Entered creditCardCodeField")
	time.sleep(2)
	connectWith = driver.find_element(By.ID, 'connectWith')
	time.sleep(1)
	webdriver.ActionChains(driver).move_to_element(connectWith).perform()
	print("Moved to connectWith")
	#signUpButton = driver.find_element(By.ID, 'signUpButton')
	# signUpButton.click()
	time.sleep(2)
	print("NoSubscribe_moreClicks Complete")
	driver.delete_all_cookies()
	driver.quit()

#def handler(event, context): # used for canary runs wrapped in a function
	#return marketingjourney()
