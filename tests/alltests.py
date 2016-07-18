from selenium import webdriver
import os
from config import *
import requests
from lxml import html
import BeautifulSoup

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

def ext_color_wheel_selection():
    """"This method for executing tab wise functionality"""
    driver = webdriver.Firefox()
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Technical Data").click()
    driver.switch_to_alert()
    driver.find_element_by_id("technicalDataDialog_x_top_x_closeDlg").click()
    driver.implicitly_wait(10)
    print "method : {0} - PASS".format(ext_color_wheel_selection.__name__)
    logfile.write("method : {0} - PASS".format(ext_color_wheel_selection.__name__))
    logfile.write("\n")
    driver.close()

def show_summary():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    #driver = webdriver.Firefox()
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_id("navigation_main_x_mainsuboffer_x_myPorsche").click()
    driver.implicitly_wait(20)
    driver.find_element_by_class_name("button_createPorscheCode").click()
    driver.implicitly_wait(20)
    driver.switch_to_alert()
    print driver.find_element_by_id("createPorscheCodeDialogView_x_webcode").text
    print "method : {0} - PASS".format(show_summary.__name__)
    logfile.write("method : {0} - PASS".format(show_summary.__name__))
    logfile.write("\n")
    driver.close()


if __name__ == '__main__':
    # funcs = [getTitleName,compatibility_mode_chrome,ext_color_wheel_selection]
    # for func in funcs:
    #     try:
    #         func()
    #     except:
    #         print "this method is failed : {0}".format(func)
    #getTitleName()
    #compatibility_mode_chrome()
    #ext_color_wheel_selection()
    show_summary()
