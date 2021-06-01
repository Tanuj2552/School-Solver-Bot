import time
import turtle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import tkinter
from tkinter import *

def tinkerit():
    def do_it():
        print("cool doing")

    def stop_it():
        print('bad not doing')

    tr = tkinter.Tk()
    tr.title("New Question!!")
    tr.geometry('500x300')

    yes_button = tkinter.Button(tr, text = 'See the Question',height = '8', width = '50', command = do_it)
    no_button = tkinter.Button(tr, text = 'Nah.. dont see',height = '8', width = '50', command = stop_it)

    yes_button.pack()
    no_button.pack()

    tr.mainloop()

    do_it(current_link)

    return

def do_it(link):
    print("New Question!!")
    turtle.setpos(-300,300)
    turtle.write('New Question', font = ('Courier', 20, 'italic'))
    turtle.setpos(-300,0)
    turtle.write(f'Category = {link[1]}, price = {link[0]}, topic = {link[2]}',font = ('Courier', 20, 'italic'))
    tinkerit()
    return


def get_it(driver):
    l = []
    price = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]').text
    category = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div').text
    title = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[3]').text 

    l = [price, category, title]
    
    print('its cool')
    print(price)
    print(category)
    print(title)
    print(l)
    return l
    #category = driver.find_element_by_xpath('//*[@id="table-3684"]/tbody/tr[1]/td[2]/div')



PATH = r"D:\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(PATH)

url = 'https://www.schoolsolver.com/account/login/?next=/'

driver.get(url)

driver.find_element_by_id('id_username').send_keys('shaquib1325')
driver.find_element_by_id('id_password').send_keys('Schoolsolver@123')

driver.find_element_by_xpath('//*[@id="login-form"]/div/div[3]/div[1]').click()

driver.find_element_by_xpath('/html/body/div[1]/div[3]/nav/div[2]/ul[1]/li[4]').click()

initial_link = get_it(driver)


while(True):
    time.sleep(10)
    driver.refresh()
    current_link = get_it(driver)
    if(initial_link != current_link):
        initial_link = current_link
        do_it(current_link)
