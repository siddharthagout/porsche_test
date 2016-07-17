from selenium import webdriver
import os
from config import *

#This is log file write
logfile = open(logs, 'w')

def getTitleName():
    """"This test gets title from page"""
    driver = webdriver.Firefox()
    driver.get(base_url)
    driver.maximize_window()
    assert "Porsche Car Configurator" in driver.title
    print "method : {0} - PASS".format(getTitleName.__name__)
    logfile.write("method : {0} - PASS".format(getTitleName.__name__))
    logfile.write("\n")
    driver.close()

def compatibility_mode_chrome():
    """"Here we are checking compatibility of website with chrome"""
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    assert "Porsche Car Configurator" in driver.title
    print "method : {0} - PASS".format(compatibility_mode_chrome.__name__)
    logfile.write("method : {0} - PASS".format(compatibility_mode_chrome.__name__))
    logfile.write("\n")
    driver.close()


if __name__ == '__main__':
    funcs = [getTitleName,compatibility_mode_chrome]
    for func in funcs:
        try:
            func()
        except:
            print "this method is failed : {0}".format(func)
    #getTitleName()
    #compatibility_mode_chrome()
