from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import autoit
import os

def path():
    global chrome
    chrome = webdriver.Chrome(os.getcwd()+'\chromedriver.exe')

def url_twitter(url):
    chrome.get(url)
    time.sleep(3)

def login(username, password):
    uname = chrome.find_element_by_name("session[username_or_email]")
    passw = chrome.find_element_by_name("session[password]")
    uname.send_keys(username)
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)
    time.sleep(3)
    cur_login = chrome.current_url
    if(cur_login == 'https://twitter.com/home'):
        print('status : login pass')
    else:
        print('status : login failed')

def post_text_and_image():
    text = chrome.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
    text.send_keys('Hello Twitter')
    time.sleep(3)
    img = chrome.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div')
    img.click()
    autoit.win_wait_active("Open")
    time.sleep(3)
    autoit.control_set_text("Open", "Edit1", r"" + os.getcwd() + "\image.JPG")
    autoit.send("{ENTER}")
    time.sleep(3)
    tweet_click = chrome.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/span/span')
    tweet_click.click()
    time.sleep(3)
    print('status : post tweet and image pass')

if __name__ == '__main__':
    path()
    url_twitter('https://twitter.com/login')
    login('dama70015138','inipassword')
    post_text_and_image()
