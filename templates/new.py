import requests
from bs4 import BeautifulSoup
from lxml import etree
import pyautogui
import time
import clipboard
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains


linkofep = clipboard.paste()
options = Options()
options.add_argument(r"user-data-dir=C:\Users\admin\AppData\Roaming\Opera Software\Opera Stable")

driver = webdriver.Opera(executable_path=r'F:\operadriver_win64\operadriver.exe', options=options)
driver.get('https://google.com/search?q=doom+at+your+service+viki')
time.sleep(3)
element = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a')
href = element.get_attribute('href')
driver.quit()

link_of_serie = str('https://www.viki.com/tv/37776c-doom-at-your-service')
driver = webdriver.Opera(executable_path=r'F:\operadriver_win64\operadriver.exe', options=options)
driver.get(link_of_serie)
img1 = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div[1]/div[1]/img')
link_of_all = str(img1.get_attribute('srcset'))
listbhai = list(link_of_all.split(","))

size_for_1_input = len(listbhai[0])
size_for_2_input = len(listbhai[1])
size_for_3_input = len(listbhai[2])
size_for_4_input = len(listbhai[3])

link_for_1_input = listbhai[0]
link_for_2_input = listbhai[1]
link_for_3_input = listbhai[2]
link_for_4_input = listbhai[3]

link_for_1_input_real = link_for_1_input[:size_for_1_input - 5]
link_for_2_input_real = link_for_2_input[:size_for_2_input - 5]
link_for_3_input_real = link_for_3_input[:size_for_3_input - 5]
link_for_4_input_real = link_for_4_input[:size_for_4_input - 5]

print("link 1 \n" + link_for_1_input_real)
print("link 2 \n" + link_for_2_input_real)
print("link 3 \n" + link_for_3_input_real)
print("link 4 \n" + link_for_4_input_real)

imglast = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div[1]/div[1]/img')
last_img = imglast.get_attribute('src')



title = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div[1]/div[2]/div/div[1]/div[2]/h1')
title_to_upload = title.text

des = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div[1]/div[2]/div/div[5]/div[1]/div[2]/div/div[1]/div')
description = des.text

yr = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div[1]/div[2]/div/div[1]/span/span[1]')
year = yr.text

gnr = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div[1]/div[2]/div/div[2]/div[1]/span')
genre = gnr.text

cst = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div[1]/div[2]/div/div[2]/div[2]/span')
cast = cst.text


# url = str(href)
# source_code = requests.get(url)
# plain_text = source_code.text
# soup = BeautifulSoup(plain_text, 'html.parser')
# dom = etree.HTML(str(soup))

# netflix_link_for_last_two = str(dom.xpath('//*[@id="section-hero"]/div[1]/div[2]/picture/source[1]').href)
# print(netflix_link_for_last_two)