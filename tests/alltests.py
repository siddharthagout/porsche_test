from selenium import webdriver
import os
from config import *
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



#This is log file write
logfile = open(logs, 'w')

def getTitleName():
    driver = webdriver.Firefox()
    driver.get(base_url)
    driver.maximize_window()
    assert "Porsche Car Configurator" in driver.title
    driver.close()

def compatibility_mode_chrome():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    assert "Porsche Car Configurator" in driver.title
    driver.close()

def get_technical_data():
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
    driver.close()

def print_summary_to_end_user():
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(".//*[@id='navigation_main_x_mainsuboffer_x_myPorsche']").click()
    driver.implicitly_wait(20)
    driver.find_element_by_id("s_navigation_summary_config_x_s_navigation_summary_config_x_printButton").click()
    driver.implicitly_wait(10)
    driver.switch_to_alert()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(".//*[@id='TechnischeDaten']/span[1]").click()
    driver.find_element_by_xpath(".//*[@id='Seriendaten']/span[1]").click()
    driver.find_element_by_xpath(".//*[@id='print_x_dialogbuttons_x_print_button']/a").click()
    driver.close()


if __name__ == '__main__':
    funcs = [getTitleName, compatibility_mode_chrome, get_technical_data, get_standard_feature, show_summary, load_code,
             customize_selection, move_to_other_car, print_summary_to_end_user]
    for func in funcs:
        try:
            func()
            print "Testcases : {0} - PASS".format(func)
            logfile.write("Testcase : {0} - PASS".format(func))
            logfile.write("\n")
        except:
            print "Testcases : {0} - FAILED".format(func)
            logfile.write("Testcase : {0} - FAILED".format(func))
            logfile.write("\n")
