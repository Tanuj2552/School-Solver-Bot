import requests
from bs4 import BeautifulSoup
import time
import turtle
import tkinter
from tkinter import *
from datetime import datetime

def tinkerit(link):
    def start_it():
        print("cool doing")
        tr.destroy()
        do_it(link)
        logic(link)
       
    def stop_it():
        print('bad not doing')
        tr.destroy()
        logic(link)
        
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
    turtle.setpos(-300,100)
    turtle.write(f'Category = {link[1]}, \n price = {link[0]},\n topic = {link[2]}',font = ('Courier', 20, 'italic'))
    turtle.exitonclick()
    return

def get_it():
    response = requests.get("https://www.schoolsolver.com/questions/")
    text = response.text
    data = BeautifulSoup(text, 'html.parser')
    New_qn = data.find_all('tr')[1]

    col_vals = New_qn.find_all('td')
    l = []

    for x in col_vals[:3]:
        d = x.text
        d = d.replace('\n','')
        l.append(d)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    print('Price = ',l[0])
    print('Category = ', l[1])
    print('Title =  ', l[2])
    print('At time of: ', current_time)
    print('')

    return l
    #category = driver.find_element_by_xpath('//*[@id="table-3684"]/tbody/tr[1]/td[2]/div')

def open_it():
    initial_link = get_it()
    return initial_link


def logic(initial_link):
    while(True):
        time.sleep(10)
        current_link = get_it()
        if(initial_link != current_link):
            initial_link = current_link
            tinkerit(current_link)
            return current_link

if(__name__ == "__main__"):
    print("start")
    initial_link = open_it()
    temp_link = logic(initial_link)








