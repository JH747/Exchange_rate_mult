from re import T
from tkinter import*
import requests
import time
import threading
from bs4 import BeautifulSoup

win = Tk()
win.geometry("500x200")
win.resizable(False, FALSE)
win.title("USD-EUR exchange rate Finder")
win.option_add("*Font", "Arial 15")

# labels
lab1 = Label(win)
lab1.config(text = "USD")
lab1.place(x = 40, y = 30)

lab2 = Label(win)
lab2.config(text = "EUR")
lab2.place(x = 40, y = 90)

lab3 = Label(win)
lab3.config(width = 20, background = "white")
lab3.place(x = 100, y = 30)

lab4 = Label(win)
lab4.config(width = 20, background = "white")
lab4.place(x = 100, y = 90)

lab5 = Label(win)
lab5.config(text = "DIFF")
lab5.place(x = 390, y = 50)

lab6 = Label(win)
lab6.config(width = 10, background = "white")
lab6.place(x = 360, y = 90)


running = False

def start():
    global running
    running = True

def stop():
    global running
    running = False


url = "https://finance.naver.com/marketindex/exchangeList.nhn"
ex_l = [0,1,2,3,4]

def analyze():
    
    if running:

        time.sleep(1)
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        found_result = soup.find("div", attrs = {"class", "tbl_area"}).get_text()

        file1 = open("D:\\oh\\programming\\python_JAVA_multi\\data\\confirm.txt", 'w')
        file1.write(found_result)
        file1.close()

        file2 = open("D:\\oh\\programming\\python_JAVA_multi\\data\\analyzer_r.txt", 'r')
        
        for i in range(0, 5):
            line = file2.readline()
            line = line.strip()
            ex_l[i] = (line)
        file2.close()

        lab3.config(text = ex_l[1])
        lab4.config(text = ex_l[3])
        lab6.config(text = ex_l[4])
        print(ex_l[1])
        print(ex_l[3])
        print(ex_l[4])

    win.after(1000, analyze)


# buttons
btn1 = Button(win)
btn1.config(text = "Start Analyzing")
btn1.config(command = start)
btn1.place(x = 70, y = 140)

btn2 = Button(win)
btn2.config(text = "Stop Analyzing")
btn2.config(command = stop)
btn2.place(x = 300, y = 140)

analyze()

win.mainloop()