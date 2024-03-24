from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
import concurrent.futures
import threading
from selenium.webdriver.common.keys import Keys

options = Options()
# options.add_argument('--headless')  # Enable Headless Mode
options.add_argument('--disable-gpu') # Disable GPU to prevent errors in certain systems or web pages
# prefs = {"profile.managed_default_content_settings.images":2}

# Dictionary containing preferences to manage default content settings in the browser.
prefs = {
    "profile.managed_default_content_settings.images": 2,  # Disable loading of images
    "profile.default_content_setting_values.notifications": 2,  # Disable notifications
    "profile.managed_default_content_settings.stylesheets": 2,  # Disable stylesheets
    "profile.managed_default_content_settings.cookies": 2,  # Disable cookies
    "profile.managed_default_content_settings.javascript": 2,  # Disable JavaScript
    "profile.managed_default_content_settings.plugins": 2,  # Disable plugins (e.g., Flash)
    "profile.managed_default_content_settings.popups": 2,  # Disable pop-ups
    "profile.managed_default_content_settings.geolocation": 2,  # Disable geolocation
    "profile.managed_default_content_settings.media_stream": 2,  # Disable media stream (e.g., camera and microphone access)
}

# Dictionary containing a single preference for disabling cookies.
prefs1 = {
    "profile.default_content_settings.cookies": 2  # Disable cookies
}

# Nested dictionary specifying default content setting values for disabling images and JavaScript.
prefs2 = {
    'profile.default_content_setting_values': {
        'images': 2,  # Disable loading of images
        'javascript': 2  # Disable JavaScript
    }
}

options.add_experimental_option('prefs', prefs1)
options.add_experimental_option('prefs', prefs2)
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.css': 2})
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.stylesheet': 2})
options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
options.add_argument("--disable-javascript") 
options.add_argument("--disable-plugins") 
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('--disable-browser-side-navigation')
options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications":2
        })
options.add_argument('disable-smooth-scrolling')
driver_path = 'C:\chromedriver.exe'  # Import Chrome Driver to start the simulator
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
time_start = time.time() 
        
def bot():
    browser = webdriver.Chrome(executable_path = driver_path, chrome_options=options)
    # browser.get("https://www.witsper.com/products/madcatz-rat-pro-x3-se")
    browser.get("https://www.witsper.com/products/0907a")
    browser.get("https://www.witsper.com/users/sign_in")
    
    fblogin = browser.find_element_by_link_text('使用Facebook登入') # Find the location for entering the account and record it for later input.
    browser.execute_script("arguments[0].click();", fblogin)
    username = browser.find_element_by_name('email') # username
    password = browser.find_element_by_name('pass') # password
    browser.execute_script("arguments[0].value = 'username';arguments[1].value = 'password';", username, password)
    loginbtn = browser.find_element_by_id('loginbutton')
    browser.execute_script("arguments[0].click();", loginbtn)
    # nums = browser.find_element_by_xpath('//*[@id="Content"]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/input')
    # nums.send_keys(Keys.BACKSPACE)
    # nums.send_keys('4')
    # search_buy = browser.find_element_by_class_name('btn-buy-now-content').click()
    ele = browser.find_element_by_xpath('//*[@id="Content"]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/variation-label-selector/div/div/div[1]')
    browser.execute_script("arguments[0].click();", loginbtn)
    browser.execute_script("arguments[0].click();", ele)
    print("buy!!!!!!!!!!!!!") 
  
  '''Use explicit wait to check every 0.5 seconds. If not detected within five seconds, exit the wait.
  Then, refresh the website in the 'except' block and continue checking for another five seconds. The timing can be adjusted as needed. '''        
    while 1:     
        try:
            # WebDriverWait(browser, 1, 0.01).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-buy-now-content'))) # Implement explicit wait to prevent the crawler from running too fast and failing to capture the elements
            # nums = browser.find_element_by_xpath('//*[@id="Content"]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/input')
            # nums.send_keys(Keys.BACKSPACE)
            # nums.send_keys('4')
            search_buy = browser.find_element_by_xpath('//*[@id="#btn-variable-buy-now"]/div/span').click()
            # browser.execute_script("arguments[0].click();", search_buy)
            print ('已定位到元素')
            break
        except:
            print("還未定位到元素! 刷新")
            browser.refresh()
    WebDriverWait(browser, 20, 0.01).until(EC.presence_of_element_located((By.ID, 'order-delivery-method')))
    select = Select(browser.find_element_by_id('order-delivery-method'))
    select.select_by_value("60c1b3113d447c0020f97b7e") 
    WebDriverWait(browser, 20, 0.01).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout-container"]/div/div/div/div[3]/div[5]/div[2]/section/div[2]/a')))        
    buy = browser.find_element_by_xpath('//*[@id="checkout-container"]/div/div/div/div[3]/div[5]/div[2]/section/div[2]/a')
    browser.execute_script("arguments[0].click();", buy)
    # WebDriverWait(browser, 20, 0.01).until(EC.presence_of_element_located((By.XPATH, '//*[@id="delivery-form-content"]/div[1]/label')))
    # browser.find_element_by_xpath('//*[@id="delivery-form-content"]/div[1]/label').click()
    select = Select(browser.find_element_by_id('order-field-0'))
    select.select_by_visible_text("同意")
    policy = browser.find_element_by_name("policy")
    browser.execute_script("arguments[0].click();", policy)
    money = browser.find_element_by_id("place-order-btn") 
    browser.execute_script("arguments[0].click();", money)# buy


threads = []

for i in range(1):
  threads.append(threading.Thread(target = bot))
  threads[i].start()

for i in range(1):
      threads[i].join()
# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     executor.map(bot)    
# sleep(60)
time_end = time.time()   
print("finish")
print(time_end - time_start)
