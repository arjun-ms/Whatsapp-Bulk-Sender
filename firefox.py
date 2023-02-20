from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from urllib.parse import quote
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO,filename=f'./log/{datetime.now()}.txt',filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')

options = Options()
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/firefox_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  			WHATSAPP BULK MESSENGER            ******")
print("*****      This tool was built by Arjun M S   	   ******")
print("*****           www.github.com/arjun-ms       	   ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

f = open("message.txt", "r")
message = f.read()
f.close()

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                except Exception as e:
                    print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
                    print("Make sure your phone and computer is connected to the internet.")
                    print("If there is an alert, please dismiss it." + style.RESET)
                    
                print("Else working")
                sleep(1)
                click_btn.click()
                sent=True
                sleep(3)
                print(style.GREEN + 'Message sent to: ' + number + style.RESET)
                logging.info('Message sent to: ' + number)
    except Exception as e:
        print(style.RED + 'Failed to send message to ' + number + "  " +"Error: "+str(e) + style.RESET)
        logging.error('Failed to send message to ' + number + "  " +"Error: "+ str(e))
driver.close()