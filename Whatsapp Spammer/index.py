#these are the main libraries we are using in this project
import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib



scriptDirectory = pathlib.Path().absolute()
#this changes the directory of the data file that will be created cause you wont be able create the user data file in the chrome directorys



option = Options()
option.add_argument("--user-data-dir=chrome-data")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
#these are the arguments required to pass so that chrome does not detect automation else it will report for bot and your ip will get ban from whatsapp web



#path = "C:\Program Files (x86)\Google\chromedriver.exe"
driver = webdriver.Chrome('C:\\Users\\KingP\\Desktop\\WHATSAPPSPAMIII\\chromedriver.exe', options=option)
driver.maximize_window()
driver.get('https://web.whatsapp.com')
#this opens the link you can change it to instagram messenger or telegram or anything you want buit you would have to change the find element syntax accordingly



#we have used 10 sec you can change accordingto your pc and internet speed in this period of thime the we page will be loading
time.sleep(10)
#this statement find the element title (name of user or group) form the web page using chrome web driver
driver.find_element_by_xpath("//*[@title='Testing']").click()


#this loop is used to specify how many times the loop will recurse 
#click function is used to specify the coordinates of (text msg)
#press will perform a function of pressing enter 
for i in range(10):
    pg.click(769, 735)
    pg.write("HELLO WORLD.")
    pg.press("enter")


#after spamming it will close after 5 seconds we can change it to whatever time we want it to close after
#close will close the driver immediately after 'xyz' seconds
time.sleep(5)
driver.close()
