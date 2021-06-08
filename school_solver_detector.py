import time
import turtle
from selenium import webdriver
import tkinter
from tkinter import *
from datetime import datetime

def tinkerit(driver, link):
    def start_it():
        print("cool doing")
        do_it(link)
        tr.destroy()

    def stop_it():
        print('bad not doing')
        logic(driver, link)
        tr.destroy()

    tr = tkinter.Tk()
    tr.title("New Question!!")
    tr.geometry('500x300')

    yes_button = tkinter.Button(tr, text = 'See the Question',height = '8', width = '50', command = start_it)
    no_button = tkinter.Button(tr, text = 'Nah.. dont see',height = '8', width = '50', command = stop_it)

    yes_button.pack()
    no_button.pack()

    tr.mainloop()

    return

def do_it(link):
    print("New Question!!")
    turtle.setpos(-300,300)
    turtle.write(f'Category = {link[1]}, \n price = {link[0]},\n topic = {link[2]}',font = ('Courier', 20, 'italic'))
    return

def get_it(driver):
    l = []
    price = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]').text
    category = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div').text
    title = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[3]').text 

    l = [price, category, title]

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    print('Price = ',price)
    print('Category = ', category)
    print('Title =  ', title)
    print('At time of: ', current_time)
    print('')

    return l
    #category = driver.find_element_by_xpath('//*[@id="table-3684"]/tbody/tr[1]/td[2]/div')

def open_it():
    PATH = r"D:\chromedriver_win32\chromedriver.exe"

    driver = webdriver.Chrome(PATH)

    url = 'https://www.schoolsolver.com/account/login/?next=/'

    driver.get(url)

    driver.find_element_by_id('id_username').send_keys('master_educator')
    driver.find_element_by_id('id_password').send_keys('Adminjane@20')

    driver.find_element_by_xpath('//*[@id="login-form"]/div/div[3]/div[1]').click()

    driver.find_element_by_xpath('/html/body/div[1]/div[3]/nav/div[2]/ul[1]/li[4]').click()

    initial_link = get_it(driver)
    return driver, initial_link


def logic(driver, initial_link):
    while(True):
        time.sleep(10)
        driver.refresh()
        current_link = get_it(driver)
        if(initial_link != current_link):
            initial_link = current_link
            tinkerit(driver, current_link)
            return current_link

if(__name__ == "__main__"):
    print("start")
    driver, initial_link = open_it()
    temp_link = logic(driver, initial_link)




