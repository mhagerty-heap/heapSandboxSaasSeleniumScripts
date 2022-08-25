import time
import json
import random
import requests
import datetime
from datetime import date

# write script run time to console
scriptRunTimestamp = datetime.datetime.now()
print("scriptRunTimestamp = " + str(scriptRunTimestamp))

# set the Heap Analytics envId
envId = "527942070"
print("Heap envID = " + envId)

# open heapCustomerPersonas.json file, randomly selected 1 out of 1000 personas, populate persona variables
randomPersonaSelector = random.randint(0,999) # used to select from the 1000 fake personas within heapCustomerPersonas.json
with open('heapCustomerPersonas.json', 'r') as f: # open file from same dir where script runs
  customerData = json.load(f)

# set customer variables based on data imported from heapCustomerPersonas.jsom  
randomIdentityEmail = customerData[randomPersonaSelector]['customerEmail']
print('randomIdentityEmail = ' + randomIdentityEmail)
customerAccountName = customerData[randomPersonaSelector]['customerAccountName']
print("customerAccountName = " + customerAccountName)  

# set random session values for userId, identity call, session, and viewselector for randomly selected main screen button
randomUserIdSelector = str(random.randint(5239706863795412, 5239706863797412)) # used for randomly selecting user id
print('randomUserIdSelector = ' + randomUserIdSelector)  
sessionId = str(random.randint(1331721900000000, 1331722000000000)) # used for randonly selecting sessionId
print('sessionId = ' + sessionId)
#pageviewId = str(random.randint(5239706900000000, 5239707000000000)) # used for randomly selecting pageviewId
#print('pageviewId = ' + pageviewId)
viewSelector = random.randint(1,13) # used for choosing random main screen button name
if viewSelector == 1: # use if you want to find it in range elif(viewSelector in (4,5,6)):
    randomButton = 'Basic + Buttons'
elif viewSelector == 2:
    randomButton = 'List'
elif viewSelector == 3:
    randomButton = 'Single Choice + Title'
elif viewSelector == 4:
    randomButton = 'Multiple Choice'
elif viewSelector == 5:
    randomButton = 'Stacked Buttons'
elif viewSelector == 6:
    randomButton = 'Dialog Callbacks'
elif viewSelector == 7:
    randomButton = 'Input'
elif viewSelector == 8:
    randomButton = 'Custom View'
elif viewSelector == 9:
    randomButton = 'Color Chooser, Primary'
elif viewSelector == 10:
    randomButton = 'File Chooser'
elif viewSelector == 11:
    randomButton = 'Folder Chooser + Buttons'
elif viewSelector == 12:
    randomButton = 'Date Picker'
else:
    randomButton = 'Informational'

# write more data to console
print("viewSelector = " + str(viewSelector))
print("Random Main Screen Button Selected = " + randomButton)


# NETWORK STEP 1 - OPEN APP - View MainActivity
# Example: https://heapanalytics.com/h?a=2356724093&s=6740642658917718&v=3242260802684940&b=ios&tv=3.0&lv=8.2.0&u=1134378632781458&m=Avo%20Keepr&p=1.1.1&g=&o=arm64&f=iOS%2015.4&vid=B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF&z=1&ts=1656342588925&h=Avo_Keepr.HomeViewController&t=&d=&y=&st=1656342588926
stepOneStartTime = round(time.time())
a=envId
s=sessionId
v=str(random.randint(1239706900000000, 1239707000000000))
b='ios'
tv='3.0'
lv='8.2.0'
u= randomUserIdSelector
m='Admin UI Mobile'
p='1.1.1'
g=''
o='arm64'
f='iOS%2015.4'
vid='B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF'
z='0'
ts=str(stepOneStartTime)
h='MainActivity'
t=''
d=''
y=''
st=str(stepOneStartTime)
openAppPayload = {'a': a, 's': s, 'v': v, 'b': b, 'tv': tv, 'lv': lv, 'u': u, 'm': m, 'p': p, 'g': g, 'o': o, 'f': f, 'vid': vid, 'z': z, 'ts': ts, 'h': h, 't': t, 'd': d, 'y': y,'st': st}
openAppGet = requests.get('https://heapanalytics.com/h', params=openAppPayload)
time.sleep(2)
print("STEP1: Open App View MainActivity")
# END NETWORK STEP 1 - OPEN APP View MainActivity

# NETWORK STEP 2 - Touch on Login
stepTwoSentTime = round(time.time())
stepTwoJson = {
    "sentTime": str(stepTwoSentTime),
    "messages": [{
        "envId": envId,
        "id": str(random.randint(1347000000000000, 1447000000000000)), 
        "applicationInfo": {
            "appName": "Admin UI Mobile",
            "appVersion": "1.1.1",
            "libraryVersion": "8.2.0"
        },
        "event": {
            "touchEvent": {
                "targetView": "LoginTargetView",
                "targetIvar": "Login",
                "type": "touch",
                "targetText": "",
                "viewAncestry": {
                    "ancestry": [{
                        "class": "Admin_UI_Mobile.AppDelegate"
                    }, {
                        "class": "UIApplication"
                    }, {
                        "class": "UIWindowScene"
                    }, {
                        "class": "UIWindow"
                    }, {
                        "class": "UITransitionView"
                    }, {
                        "class": "UITabBarController"
                    }, {
                        "class": "Admin_UI_Mobile.Login"
                    }, {
                        "class": "UIView"
                    }, {
                        "class": "UIView"
                    }, {
                        "class": "MainScreenLoginButton"
                    }]
                }
            },
            "appVisibilityState": 2
        },
        "pageviewInfo": {
            "screenA11yLabel": "",
            "id": str(random.randint(7700000000000000, 7800000000000000)),
            "title": "loginButton",
            "timestamp": str(stepTwoSentTime), #second, 1656338019976 
            "viewController": "Admin_UI_Mobile.MainActivity",
            "screenA11yId": ""
        },
        "sessionInfo": {
            "id": sessionId,
            "timestamp": str(stepTwoSentTime) # first, 1656337423649
        },
        "deviceInfo": {
            "iosVendorId": "B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF",
            "carrier": "",
            "phoneModel": "arm64",
            "platform": "iOS 15.4"
        },
        "timestamp": str(stepTwoSentTime), #third, 1656338032597
        "user": {
            "id": randomUserIdSelector
        }
    }]
}
stepTwoPost = requests.post('https://heapanalytics.com/api/integrations/ios/track', json=stepTwoJson)
time.sleep(2)
print("STEP2: Touch Login Network Call Complete")
# END NETWORK STEP 2 - Touch on Login

# NETWORK STEP 3 - View loginDialog
loginDialogStartTime = round(time.time())
a=envId
s=sessionId
v=str(random.randint(1239706900000000, 1239707000000000))
b='ios'
tv='3.0'
lv='8.2.0'
u= randomUserIdSelector
m='Admin UI Mobile'
p='1.1.1'
g=''
o='arm64'
f='iOS%2015.4'
vid='B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF'
z='2'
ts=str(loginDialogStartTime)
h='loginDialog'
t=''
d=''
y=''
st=str(loginDialogStartTime)
loginDialogPayload = {'a': a, 's': s, 'v': v, 'b': b, 'tv': tv, 'lv': lv, 'u': u, 'm': m, 'p': p, 'g': g, 'o': o, 'f': f, 'vid': vid, 'z': z, 'ts': ts, 'h': h, 't': t, 'd': d, 'y': y,'st': st}
openAppGet = requests.get('https://heapanalytics.com/h', params=loginDialogPayload)
time.sleep(2)
print("STEP3: loginDialog View Call Complete")
# END NETWORK STEP 3 - View loginDialog

# NETWORK STEP 4, Touch on identifyTextField
stepThreeSentTime = round(time.time())
stepThreeJson = {
    "sentTime": str(stepThreeSentTime),
    "messages": [{
        "envId": envId,
        "id": str(random.randint(1347000000000000, 1447000000000000)),
        "applicationInfo": {
            "appName": "Admin UI Mobile",
            "appVersion": "1.1.1",
            "libraryVersion": "8.2.0"
        },
        "event": {
            "touchEvent": {
                "targetView": "identityTextFieldTargetView",
                "targetIvar": "identityTextField",
                "type": "touch",
                "targetText": "",
                "viewAncestry": {
                    "ancestry": [{
                        "class": "Admin_UI_Mobile.AppDelegate"
                    }, {
                        "class": "UIApplication"
                    }, {
                        "class": "UIWindowScene"
                    }, {
                        "class": "UIWindow"
                    }, {
                        "class": "UITransitionView"
                    }, {
                        "class": "UIDropShadowView"
                    }, {
                        "class": "UITabBarController"
                    }, {
                        "class": "UILayoutContainerView"
                    }, {
                        "class": "UITransitionView"
                    }, {
                        "class": "UIViewControllerWrapperView"
                    }, {
                        "class": "UINavigationController"
                    }, {
                        "class": "UILayoutContainerView"
                    }, {
                        "class": "UINavigationTransitionView"
                    }, {
                        "class": "UIViewControllerWrapperView"
                    }, {
                        "class": "Admin_UI_Mobile.AboutTableViewController"
                    }, {
                        "class": "UITableView"
                    }, {
                        "class": "UIView"
                    }, {
                        "class": "LoginDialogIdentifyTextField"
                    }]
                }
            },
            "appVisibilityState": 2
        },
        "pageviewInfo": {
            "screenA11yLabel": "",
            "id": str(random.randint(7700000000000000, 7800000000000000)),
            "title": "identifyTextField",
            "timestamp": str(stepThreeSentTime),
            "viewController": "loginDialog",
            "screenA11yId": ""
        },
        "sessionInfo": {
            "id": sessionId,
            "timestamp": str(stepThreeSentTime)
        },
        "deviceInfo": {
            "iosVendorId": "B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF",
            "carrier": "",
            "phoneModel": "arm64",
            "platform": "iOS 15.4"
        },
        "timestamp": str(stepThreeSentTime),
        "user": {
            "id": randomUserIdSelector
        }
    }]
}
stepThreePost = requests.post('https://heapanalytics.com/api/integrations/ios/track', json=stepThreeJson)
time.sleep(2)
print("STEP4: identifyTextField Network Call Complete")
# END NETWORK STEP 4, Touch on identifyTextField

# NETWORK STEP 5 - Touch on IdentifyButton on login screen
stepFourSentTime = round(time.time())
stepFourJson = {
    "sentTime": str(stepFourSentTime),
    "messages": [{
        "envId": envId,
        "id": str(random.randint(1347000000000000, 1447000000000000)),
        "applicationInfo": {
            "appName": "Admin UI Mobile",
            "appVersion": "1.1.1",
            "libraryVersion": "8.2.0"
        },
        "event": {
            "touchEvent": {
                "targetView": "UIButtonTargetView",
                "targetIvar": "IdentifyButton",
                "type": "touch",
                "targetText": "",
                "viewAncestry": {
                    "ancestry": [{
                        "class": "Admin_UI_Mobile.AppDelegate"
                    }, {
                        "class": "UIApplication"
                    }, {
                        "class": "UIWindowScene"
                    }, {
                        "class": "UIWindow"
                    }, {
                        "class": "UITransitionView"
                    }, {
                        "class": "UITabBarController"
                    }, {
                        "class": "Admin_UI_Mobile.Login"
                    }, {
                        "class": "UIView"
                    }, {
                        "class": "UIView"
                    }, {
                        "class": "LoginIdentifyButton"
                    }]
                }
            },
            "appVisibilityState": 2
        },
        "pageviewInfo": {
            "screenA11yLabel": "",
            "id": str(random.randint(7700000000000000, 7800000000000000)),
            "title": "identifyButton",
            "timestamp": str(stepFourSentTime), #second, 1656338019976 
            "viewController": "loginDialog",
            "screenA11yId": ""
        },
        "sessionInfo": {
            "id": sessionId,
            "timestamp": str(stepFourSentTime) # first, 1656337423649
        },
        "deviceInfo": {
            "iosVendorId": "B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF",
            "carrier": "",
            "phoneModel": "arm64",
            "platform": "iOS 15.4"
        },
        "timestamp": str(stepFourSentTime), #third, 1656338032597
        "user": {
            "id": randomUserIdSelector
        }
    }]
}
stepFourPost = requests.post('https://heapanalytics.com/api/integrations/ios/track', json=stepFourJson)
time.sleep(2)
print("STEP5: Touch on IdentifyButton on login screen Network Call Complete")
# END NETWORK STEP 5 - Touch on IdentifyButton on login screen

# STEP 6 IDENTIFY NETWORK CALL
# Example: https://heapanalytics.com/api/identify_v3?a=2356724093&s=2273256378657165&v=1292487889593889&b=ios&tv=3.0&lv=8.2.0&u=1134378632781458&i=test%40test.com&st=1658419727208
identifyStepTime=round(time.time())  #get current time for event time
a=envId
s=sessionId
v=str(random.randint(1239706900000000, 1239707000000000))
b='ios'
tv='3.0'
lv='8.2.0'
u=randomUserIdSelector
i=randomIdentityEmail
st=identifyStepTime
identifyPayload = {'a': a, 's': s, 'v': v, 'b': b, 'tv': tv, 'lv': lv, 'u': u, 'i': i, 'st': st}
identifyGet = requests.get('https://heapanalytics.com/api/identify_v3', params=identifyPayload)
print(identifyGet)
time.sleep(2)
print("STEP6: Heap Identify Network Call Complete with: " + randomIdentityEmail)
# END STEP 6 IDENTIFY NETWORK CALL

# STEP 6.5 addUserProperty call for Account Name
# make API call back to Heap for custom user properties, specifically Account - Account Name
# addUserPropConn = http.client.HTTPSConnection('heapanalytics.com')
# headers = {'Content-type': 'application/json'}
addUserPropsHeapTrackJson = {
    'app_id': envId,
    'identity': randomIdentityEmail,
    'properties': {'Account - Account Name': '' + customerAccountName + ''},
}
stepUserPropPost = requests.post('https://heapanalytics.com/api/add_user_properties', json=addUserPropsHeapTrackJson)
#addUserProps_json_data = json.dumps(addUserPropsHeapTrackJson)
#addUserPropConn.request('POST', '/api/add_user_properties', addUserProps_json_data, headers)
time.sleep(1)
print("Step6.5: Heap addUserProperty call complete with: Account - " + customerAccountName)

# NETWORK STEP 7 - View MainActivity
# Example: https://heapanalytics.com/h?a=2356724093&s=6740642658917718&v=3242260802684940&b=ios&tv=3.0&lv=8.2.0&u=1134378632781458&m=Avo%20Keepr&p=1.1.1&g=&o=arm64&f=iOS%2015.4&vid=B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF&z=1&ts=1656342588925&h=Avo_Keepr.HomeViewController&t=&d=&y=&st=1656342588926
stepViewMainActivityStartTime = round(time.time())
a=envId
s=sessionId
v=str(random.randint(1239706900000000, 1239707000000000))
b='ios'
tv='3.0'
lv='8.2.0'
u= randomUserIdSelector
m='Admin UI Mobile'
p='1.1.1'
g=''
o='arm64'
f='iOS%2015.4'
vid='B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF'
z='2'
ts=str(stepViewMainActivityStartTime)
h='MainActivity'
t=''
d=''
y=''
st=str(stepViewMainActivityStartTime)
stepViewMainActivityPayload = {'a': a, 's': s, 'v': v, 'b': b, 'tv': tv, 'lv': lv, 'u': u, 'm': m, 'p': p, 'g': g, 'o': o, 'f': f, 'vid': vid, 'z': z, 'ts': ts, 'h': h, 't': t, 'd': d, 'y': y,'st': st}
stepViewMainActivityGet = requests.get('https://heapanalytics.com/h', params=stepViewMainActivityPayload)
time.sleep(2)
print("STEP7: View MainActivity Again")
# NETWORK STEP 7 - View MainActivity


# NETWORK STEP 8 - Touch randomly selected screen buttons determined by stepper selection above
stepFiveSentTime = round(time.time())
stepFiveJson = {
    "sentTime": str(stepFiveSentTime),
    "messages": [{
        "envId": envId,
        "id": str(random.randint(1347000000000000, 1447000000000000)),
        "applicationInfo": {
            "appName": "Admin UI Mobile",
            "appVersion": "1.1.1",
            "libraryVersion": "8.2.0"
        },
        "event": {
            "touchEvent": {
                "targetView": "randomButtonTargetView",
                "targetIvar": randomButton,
                "type": "touch",
                "targetText": "",
                "viewAncestry": {
                    "ancestry": [{
                        "class": "Admin_UI_Mobile.AppDelegate"
                    }, {
                        "class": "UIApplication"
                    }, {
                        "class": "UIWindowScene"
                    }, {
                        "class": "UIWindow"
                    }, {
                        "class": "UITransitionView"
                    }, {
                        "class": "UITabBarController"
                    }, {
                        "class": "Admin_UI_Mobile.AppDelegate"
                    }, {
                        "class": "UIView"
                    }, {
                        "class": "UIView"
                    }, {
                        "class": randomButton +"MainScreenButton"
                    }]
                }
            },
            "appVisibilityState": 2
        },
        "pageviewInfo": {
            "screenA11yLabel": "",
            "id": str(random.randint(7700000000000000, 7800000000000000)),
            "title": "randomButton",
            "timestamp": str(stepFiveSentTime), #second, 1656338019976 
            "viewController": "Admin_UI_Mobile.MainActivity",
            "screenA11yId": ""
        },
        "sessionInfo": {
            "id": sessionId,
            "timestamp": str(stepFiveSentTime) # first, 1656337423649
        },
        "deviceInfo": {
            "iosVendorId": "B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF",
            "carrier": "",
            "phoneModel": "arm64",
            "platform": "iOS 15.4"
        },
        "timestamp": str(stepFiveSentTime), #third, 1656338032597
        "user": {
            "id": randomUserIdSelector
        }
    }]
}
stepFivePost = requests.post('https://heapanalytics.com/api/integrations/ios/track', json=stepFiveJson)
time.sleep(2)
print("STEP8: Touch Random Screen Button Network Call Complete")
# END NETWORK STEP 8 - Touch randomly selected screen buttons determined by stepper selection above

# NETWORK STEP 9 - View Random Button Screen
randomButtonDialogViewStartTime = round(time.time())
a=envId
s=sessionId
v=str(random.randint(1239706900000000, 1239707000000000))
b='ios'
tv='3.0'
lv='8.2.0'
u= randomUserIdSelector
m='Admin UI Mobile'
p='1.1.1'
g=''
o='arm64'
f='iOS%2015.4'
vid='B7B6D296-C0BE-419A-9CFE-F240C1DDC8DF'
z='2'
ts=str(randomButtonDialogViewStartTime)
h=randomButton + 'Dialog'
t=''
d=''
y=''
st=str(randomButtonDialogViewStartTime)
randomButtonDialogViewPayload = {'a': a, 's': s, 'v': v, 'b': b, 'tv': tv, 'lv': lv, 'u': u, 'm': m, 'p': p, 'g': g, 'o': o, 'f': f, 'vid': vid, 'z': z, 'ts': ts, 'h': h, 't': t, 'd': d, 'y': y,'st': st}
randomButtonDialogViewGet = requests.get('https://heapanalytics.com/h', params=randomButtonDialogViewPayload)
time.sleep(2)
print("STEP9: " + randomButton + " View Network Call Complete")
# END NETWORK STEP 9 - View Random Button Screen