import time
import json
import random
#from selenium import webdriver
#from aws_synthetics.selenium import synthetics_webdriver as webdriver
from aws_synthetics.selenium import synthetics_webdriver
from aws_synthetics.common import synthetics_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def marketingjourney():

	# Grab last digit of time since epoch, and use this to set UTM codes for beginning URL
	timeSinceEpochUtm = time.time()
	timeSinceEpochUserAgent = time.time()
	randomUTMSelector = str(timeSinceEpochUtm) # used to select UTM codes
	randomUserAgentSelector = str(timeSinceEpochUserAgent)
	randomTrafficPatternSelection = random.randint(0,9) # used for selecting traffic pattern
	randomTimeSleepInterval = random.randint(1,3) # used for time.sleep(randomTimeSleepInterval) between steps
	synthetics_logger.info("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection))  # use on AWS
	print("randomTrafficPatternSelection = " + str(randomTrafficPatternSelection)) # use on local

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

	# start webdriver for Selenium session
	# webdriver.add_user_agent(userAgentString)
	#webdriver.add_user_agent('This is a test')
	synthetics_webdriver.add_user_agent('MyApp-1.0')
	
	#chrome_options = Options()
	#chrome_options.add_argument("user-agent=" + userAgentString)
	#driver = webdriver.Chrome(chrome_options=chrome_options)
	
	#driver = webdriver.Chrome()
	driver = synthetics_webdriver.Chrome()

	user_agent = driver.execute_script("return navigator.userAgent;")
	synthetics_logger.info("userAgentString = " + userAgentString)
	synthetics_logger.info("user_agent = " + user_agent)
	driver.set_window_position(0, 0)
	driver.set_window_size(1024, 768)
	synthetics_logger.info(driver.get_window_size())
	driver.implicitly_wait(10)
	driver.get(startingUrlWithUtmCodes)

	# grab top nav link IDs
	mainHomeLink = driver.find_element(By.ID, 'mainHomeLink')
	mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
	mainContactLink = driver.find_element(By.ID, 'mainContactLink')
	mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
	mainTeamLink = driver.find_element(By.ID, 'mainTeamLink')
	mainSignUpLink = driver.find_element(By.ID, 'mainSignUpLink')
	mainSignInLink = driver.find_element(By.ID, 'mainSignInLink')


	# set a pattern of clicks/pages views by customers. 0 and 9 are 1 page visits
	if (randomTrafficPatternSelection == 0):
		driver.delete_all_cookies()
		driver.quit()
	elif(randomTrafficPatternSelection == 1):
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainAboutLink)
		driver.delete_all_cookies()
		driver.quit()
	elif(randomTrafficPatternSelection == 2):
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainTeamLink)
		driver.delete_all_cookies()
		driver.quit()
	elif(randomTrafficPatternSelection == 3):
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		driver.delete_all_cookies()
		driver.quit()
	elif(randomTrafficPatternSelection == 4):
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		driver.delete_all_cookies()
		driver.quit()
	elif(randomTrafficPatternSelection == 5):
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		driver.delete_all_cookies()
		driver.quit()
	elif(randomTrafficPatternSelection == 6):
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		driver.delete_all_cookies()
		driver.quit()
	elif(randomTrafficPatternSelection == 7):
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		time.sleep(randomTimeSleepInterval)
		mainSignInLink = driver.find_element(By.ID, 'mainSignInLink')
		driver.execute_script("arguments[0].click();", mainSignInLink)
		time.sleep(randomTimeSleepInterval)
		mainPricingLink = driver.find_element(By.ID, 'mainPricingLink')
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		mainAboutLink = driver.find_element(By.ID, 'mainAboutLink')
		driver.execute_script("arguments[0].click();", mainAboutLink)
		driver.delete_all_cookies()
		driver.quit()
	elif(randomTrafficPatternSelection == 8):
		driver.find_element(By.ID, "mainHomeLink").click()
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainContactLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainPricingLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainTeamLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainAboutLink)
		time.sleep(randomTimeSleepInterval)
		driver.execute_script("arguments[0].click();", mainSignUpLink)
		driver.delete_all_cookies()
		driver.quit()
	else:
		driver.delete_all_cookies()
		driver.quit()

def handler(event, context):
	return marketingjourney()
	# webdriver.execute_step('Run Scripts', marketingjourney())
