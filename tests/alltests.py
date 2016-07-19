from selenium import webdriver
import os
from config import *
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

def get_technical_data():
    """"This method for executing tab wise functionality"""
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Technical Data").click()
    driver.switch_to_alert()
    driver.find_element_by_id("technicalDataDialog_x_top_x_closeDlg").click()
    driver.implicitly_wait(10)
    driver.switch_to_window(driver.window_handles[-1])
    assert "Porsche 911 Targa 4S" in driver.find_element_by_id("headline").text
    print "method : {0} - PASS".format(get_technical_data.__name__)
    logfile.write("method : {0} - PASS".format(get_technical_data.__name__))
    logfile.write("\n")
    driver.close()

def get_standard_feature():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(".//*[@id='modelinfo_x_modelinfo_x_standardFeaturesDialog']/a").click()
    driver.implicitly_wait(10)
    driver.switch_to_alert()
    driver.find_element_by_xpath(".//*[@id='standardFeaturesDialog_x_top_x_closeDlg']").click()
    driver.implicitly_wait(10)
    driver.switch_to_window(driver.window_handles[-1])
    assert "Porsche 911 Targa 4S" in driver.find_element_by_id("headline").text
    print "method : {0} - PASS".format(get_standard_feature.__name__)
    logfile.write("method : {0} - PASS".format(get_standard_feature.__name__))
    logfile.write("\n")
    driver.close()

def show_summary():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
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

def load_code():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("id('navigation_contact_x_ConfigurationListView')").click()
    driver.implicitly_wait(10)
    driver.switch_to_alert()
    driver.find_element_by_id("SSOLoadSection_x_webcode").send_keys("PH9G4S20")
    driver.find_element_by_link_text("Load").click()
    driver.switch_to_window(driver.window_handles[-1])
    driver.implicitly_wait(10)
    assert "Porsche 911 Targa 4S" in driver.find_element_by_id("headline").text
    print "method : {0} - PASS".format(load_code.__name__)
    logfile.write("method : {0} - PASS".format(load_code.__name__))
    logfile.write("\n")
    driver.close()

def customize_selection():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(".//*[@id='s_interieur_x_PP06']").is_selected()
    driver.find_element_by_id("navigation_main_x_mainsuboffer_x_myPorsche").click()
    driver.implicitly_wait(20)
    driver.find_element_by_class_name("button_createPorscheCode").click()
    driver.implicitly_wait(20)
    driver.switch_to_alert()
    print driver.find_element_by_id("createPorscheCodeDialogView_x_webcode").text
    print "method : {0} - PASS".format(customize_selection.__name__)
    logfile.write("method : {0} - PASS".format(customize_selection.__name__))
    logfile.write("\n")
    driver.close()

def move_to_other_car():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    model = driver.find_element_by_id("navigation_main_x_mainsuboffer_x_models")
    sub1 = driver.find_element_by_id("s_models_x_718_x_flyoutopener")
    sub2 = driver.find_element_by_id("s_models_x_718_x__982320HC00")
    action = ActionChains(driver)
    action.move_to_element(model)
    action.move_to_element(sub1)
    sleep(5)
    action.click(sub2).perform()
    driver.switch_to_alert()
    driver.find_element_by_id("F_2034_us12_x_dialogbuttons_x_button1").click()
    driver.switch_to_window(driver.window_handles[-1])
    print "method : {0} - PASS".format(move_to_other_car.__name__)
    logfile.write("method : {0} - PASS".format(move_to_other_car.__name__))
    logfile.write("\n")
    driver.close()

def compare_cars():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    model = driver.find_element_by_id("navigation_main_x_mainsuboffer_x_models")
    driver.implicitly_wait(10)
    sub1 = driver.find_element_by_id("model_expandOpportunitymodelCompare")
    ActionChains(driver).move_to_element(model).click_and_hold(model).move_to_element(sub1).click_and_hold(sub1).click().perform()


if __name__ == '__main__':
    funcs = [getTitleName, compatibility_mode_chrome, get_technical_data, get_standard_feature, show_summary, load_code,
             customize_selection, move_to_other_car]
    for func in funcs:
        try:
            func()
        except:
            print "this method is failed : {0}".format(func)
    #getTitleName()
    #compatibility_mode_chrome()
    #get_technical_data()
    #show_summary()
    #load_code()
    #customize_selection()
    #move_to_other_car()
    #get_standard_feature()
    #compare_cars()