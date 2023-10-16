import pandas as pd
from selenium import webdriver
import time
from random import randint

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfFaGJLx7tXeUPaEEDMuLghB8DNdEtQ4VABHbu8oWFU3SdKGw/viewform")
def selection():
    n = randint(1,3)
    if n == 1:
        ans1 = driver.find_element("xpath",'//*[@id="i5"]/div[3]/div')
        ans1.click()
    elif n == 2:
        ans1 = driver.find_element("xpath",'//*[@id="i8"]/div[3]/div')
        ans1.click()
    else:
        ans1 = driver.find_element("xpath",'//*[@id="i11"]/div[3]/div')
        ans1.click()


def fill_form():
    # data = pd.read_csv('data.csv')
    for i in range(1000):
        print(i)
        time.sleep(0.5)

        selection()

        # name = data.iloc[i]['name']
        name = "khiemvippro"
        inputName = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')

        inputName.send_keys(name)

        submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit.click()

        back = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        back.click()

fill_form()
driver.close()