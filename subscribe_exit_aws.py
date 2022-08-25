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
from selenium.webdriver.common.keys import Keys

def subscribe_exit(): # used to wrap canary runs within a function

	#set some initial variables
	# Grab last digit of time since epoch, and use this to set UTM codes for beginning URL
	timeSinceEpochUtm = time.time()
	timeSinceEpochUserAgent = time.time()
	randomUTMSelector = str(timeSinceEpochUtm) # used to select UTM codes
	randomUserAgentSelector = str(timeSinceEpochUserAgent)
	randomTrafficPatternSelection = random.randint(0,9) # used for selecting traffic pattern
	#randomTrafficPatternSelection = 0 # used for testing specific traffic patterns
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
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html" 
	elif(randomUTMSelector.endswith("2")):
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html"
	elif(randomUTMSelector.endswith("3")):
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Facebook&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew"
	elif(randomUTMSelector.endswith("4")):
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Twitter&utm_medium=display&utm_campaign=SanFranciscoGeo&utm_content=SaaSDemoNew"
	elif(randomUTMSelector.endswith("5")):
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Blog&utm_medium=referral&utm_campaign=NewArticles&utm_content=BeTheBestSaaS"
	elif(randomUTMSelector.endswith("6")):
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=LinkedIn&utm_medium=display&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1"
	elif(randomUTMSelector.endswith("7")):
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Google&utm_medium=cpc&utm_campaign=SponsortedContent&utm_content=NewProductFeatures"
	elif(randomUTMSelector.endswith("8")):
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=EmailList1&utm_medium=email&utm_campaign=UpgradePath&utm_content=TryNewFeatures"
	elif(randomUTMSelector.endswith("9")):
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html?utm_source=Affiliate&utm_medium=referral&utm_campaign=SaaSForExecutives&utm_content=ExecutiveContentSeries1"
	else:
		startingUrlWithUtmCodes = "https://heap-sandbox-saas.vercel.app/main.html"

	# set Agent String for session
	# if randomTrafficPatternSelection is 0 through 9 set user agent code accordingly
	if(randomUserAgentSelector.endswith("1")):
		userAgentString = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36" 
	elif(randomUserAgentSelector.endswith("2")):
		userAgentString = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
	elif(randomUserAgentSelector.endswith("3")):
		userAgentString = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
	elif(randomUserAgentSelector.endswith("4")):
		userAgentString = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
	elif(randomUserAgentSelector.endswith("5")):
		userAgentString = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1"
	elif(randomUserAgentSelector.endswith("6")):
		userAgentString = "Mozilla/5.0 (iPad; CPU OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1"
	elif(randomUserAgentSelector.endswith("7")):
		userAgentString = "Mozilla/5.0 (iPod; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1"
	elif(randomUserAgentSelector.endswith("8")):
		userAgentString = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"
	elif(randomUserAgentSelector.endswith("9")):
		userAgentString = "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"
	else:
		userAgentString = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"


	#print and logging statements for script variables prior to browser instantiation
	synthetics_logger.info("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))  # use on AWS
	synthetics_logger.info("randomPlanSelector value = " + str(randomPlanSelector))  # use on AWS
	synthetics_logger.info("planRadioSelection = " + planRadioSelection)	
	#print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection)) # use on local
	#print("randomPlanSelector value = " + str(randomPlanSelector))
	#print("planRadioSelection = " + planRadioSelection)


	#synthetics_webdriver.add_user_agent('MyApp-1.0') # supposed to support agent string switching on Canary, but doesn't seem to work (bug?)

	driver = webdriver.Chrome() # used for local run
	#driver = synthetics_webdriver.Chrome() # used for Canary run

	user_agent = driver.execute_script("return navigator.userAgent;")
	driver.set_window_position(0, 0)
	driver.set_window_size(1024, 768)
	driver.implicitly_wait(10)
	driver.get(startingUrlWithUtmCodes)

	#print and logging statements for script variables after browser instantiation
	synthetics_logger.info("selected userAgentString = " + userAgentString) # log UserAgentString
	synthetics_logger.info("actual browser user agent string = " + user_agent) # log action browser user agent to see if setting agent string for browser worked
	synthetics_logger.info(driver.get_window_size())
	#print("selected userAgentString = " + userAgentString)
	#print("actual browser user agent string = " + user_agent)
	#print(driver.get_window_size())

	#Start of traffic patterns
	#Homepage -> About -> Pricing -> Team -> SignUp Event -> Exit
	#Tested - Works 3/8/22
	if (randomTrafficPatternSelection == 0):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)
		driver.delete_all_cookies()
		driver.quit()

	#Homepage -> Features -> Pricing -> Signup  Event -> Exit
	#Tested - Works 3/8/22
	elif(randomTrafficPatternSelection == 1):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainFeaturesLink = driver.find_element(By.ID, 'featuresLink1')
		driver.execute_script("arguments[0].click();", mainFeaturesLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)
		driver.delete_all_cookies()
		driver.quit()

	#Homepage -> Pricing -> About -> Contact -> Team -> SignUp Event -> Exit
	#Tested - Works 3/8/22
	elif(randomTrafficPatternSelection == 2):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		mainContactLink = driver.find_element(By.ID, 'mainContactLink')
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)
		driver.delete_all_cookies()
		driver.quit()

	#Homepage -> Team -> About -> Pricing -> Contact -> Signup Event -> Exit
	#Tested - Works 3/8/22
	elif(randomTrafficPatternSelection == 3):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainContactLink = driver.find_element(By.ID, 'mainContactLink')
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)
		driver.delete_all_cookies()
		driver.quit()

	#Homepage -> About -> Pricing -> Team -> Contact -> Signup Event -> Exit
	#Tested - Works 3/8/22
	elif(randomTrafficPatternSelection == 4):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		mainContactLink = driver.find_element(By.ID, 'mainContactLink')
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)
		driver.delete_all_cookies()
		driver.quit()

	#Homepage -> About -> Pricing -> Contact -> Team -> Signup -> Home ->Pricing -> Signup Event -> Exit
	#Tested - Works 3/8/22
	elif(randomTrafficPatternSelection == 5):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainContactLink = driver.find_element(By.ID, 'mainContactLink')
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)
		driver.delete_all_cookies()
		driver.quit()


	#Homepage -> Contact -> Pricing -> Team -> About -> Pricing -> Features -> Pricing -> Signup Event -> Exit
	#Tested - Works 3/8/22
	elif(randomTrafficPatternSelection == 6):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainContactLink = driver.find_element(By.ID, 'mainContactLink')
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		#mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		time.sleep(randomTimeSleepInterval)
		mainFeaturesLink = driver.find_element(By.ID, 'featuresLink1')
		driver.execute_script("arguments[0].click();", mainFeaturesLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpNameField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpStreetAddressField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpZipCodeField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpMobileNumberField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpNameField").click()
		time.sleep(5)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(7)
		driver.find_element(By.ID, "signUpStreetAddressField").click()
		time.sleep(7)
		driver.find_element(By.ID, "signUpZipCodeField").click()
		time.sleep(7)
		driver.find_element(By.ID, "signUpMobileNumberField").click()
		time.sleep(9)							
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)
		driver.delete_all_cookies()
		driver.quit()

	#Homepage -> About -> Pricing -> Signup Event -> Exit
	#Tested - Works 3/8/22
	elif(randomTrafficPatternSelection == 7):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)
		driver.delete_all_cookies()
		driver.quit()		

	#Homepage -> Pricing -> Signup Event -> Exit
	#Tested - Works 3/8/22
	elif(randomTrafficPatternSelection == 8):
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)			
		driver.delete_all_cookies()
		driver.quit()

	#Homepage -> Features -> SignUp Event -> Exit
	#Tested - Works 3/8/22
	else:
		mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		mainFeaturesLink = driver.find_element(By.ID, 'featuresLink1')
		driver.execute_script("arguments[0].click();", mainFeaturesLink)
		time.sleep(randomTimeSleepInterval)
		mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").click()
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, "signUpEmailField").send_keys(randomUserEmail)
		time.sleep(randomTimeSleepInterval)
		driver.find_element(By.ID, planRadioSelection).click()
		time.sleep(randomTimeSleepInterval)
		#driver.find_element(By.ID, "signUpButton").click()
		#time.sleep(randomTimeSleepInterval)			
		driver.delete_all_cookies()
		driver.quit()

def handler(event, context): # used for canary runs wrapped in a function
	return subscribe_exit()
