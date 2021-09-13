from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from robot.libraries.BuiltIn import BuiltIn
import logging
from checklist_Elements import checklist_Elements as elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time as t

# global driver related variables
current_driver = None
current_driver_index = -1
driver_list = []
screenshot_index = 1

# global test execution variables
turbo_mode = True

class checklist_WEB:     
    #TODO: list with browser options, allow different browsers

    # Browser Oriented

    def start_browser(self, website, browser="Chrome", width="800", height="600", headless=False, maximize=False, incognito=False):
        if browser=="Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("no-sandbox")
            options.add_argument("--disable-gpu")
            if maximize:
                options.add_argument("--start-maximized")
            else:
                options.add_argument("--window-size="+ width + "," + height)
            options.add_argument("--disable-dev-shm-usage")
            if incognito:
                options.add_argument('--incognito')
            if headless:
                options.set_headless()
            driver = webdriver.Chrome(options=options)
        
        #elif browser.lower()="firefox":
        #    driver = webdriver.Firefox()
        
        #elif browser.lower()="safari":
        
        #elif browser.lower()="opera":
        #    webdriver_service = service.Service('C:\\Users\\Kris\\Downloads\\WinPython-32bit-2.7.9.2\\operadriver.exe')
        #    webdriver_service.start()
        #    driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

        
        #elif browser.lower()="iexplorer":
        #    driver = webdriver.Ie()
        
        #elif browser.lower()="phantomjs":
        #    driver = webdriver.PhantomJS()

        global driver_list, current_driver_index
        current_driver_index = current_driver_index + 1
        driver_list.append(driver)
        checklist_WEB.go_to_url(self, website)
        return current_driver_index + 1

    def close_browser(self, index):
        global driver_list, current_driver_index
        for index_driver in range (0, len(driver_list)):
            if index_driver  == index - 1:
                driver_list[index_driver].close()
                driver_list.remove(driver_list[index_driver])
                return True

    def close_all_browsers(self):
        global driver_list, current_driver_index
        for driver in driver_list[:]:
            driver.close()
            driver_list.remove(driver)
        current_driver_index = -1

    
    def switch_browser(self, index):
        global current_driver_index
        current_driver_index = index -1

    def get_driver(self, index):
        global driver_list
        return driver_list[index]

    def get_current_driver(self):
        global driver_list, current_driver_index
        return driver_list[current_driver_index]

    def go_to_url(self, url):
        current_driver = checklist_WEB.get_current_driver(self)
        current_driver.get(url)

    def take_screenshot(self):
        global screenshot_index
        current_driver = checklist_WEB.get_current_driver(self)
        numberOfIndexDigits = len(str(screenshot_index))
        numberOfPrefixDigits = 4 - len(str(screenshot_index))
        current_driver.save_screenshot("screenshot_" + str(numberOfPrefixDigits*"0") + str(screenshot_index) +".png");
        screenshot_index = screenshot_index + 1

    # Action Oriented

    def wait_until_visible(self, element, timeout=10):
        element_xpath = elements.get_xpath(self, element)
        element = WebDriverWait(checklist_WEB.get_current_driver(self), timeout).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )
        if not turbo_mode:
            checklist_WEB.wait(self,2)

    def click(self, element):
        checklist_WEB.wait_until_visible(self, element)
        elementToClick = elements.get_xpath(self, element)
        checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick).click()
        if not turbo_mode:
            checklist_WEB.wait(self,2)
            
    def double_click(self, element):
        checklist_WEB.wait_until_visible(self, element)        
        actionChains = ActionChains(checklist_WEB.get_current_driver(self))
        actionChains.double_click(checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick)).perform()
        if not turbo_mode:
            checklist_WEB.wait(self,2)
            
    def click_and_hold(self, element):
        checklist_WEB.wait_until_visible(self, element)        
        actionChains = ActionChains(checklist_WEB.get_current_driver(self))
        actionChains.click_and_hold(checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick)).perform()
        if not turbo_mode:
            checklist_WEB.wait(self,2)
  
    def drag_and_drop(self, element, target):
        checklist_WEB.wait_until_visible(self, element)        
        actionChains = ActionChains(checklist_WEB.get_current_driver(self))
        actionChains.drag_and_drop(checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick), checklist_WEB.get_current_driver(self).find_element_by_xpath(target)).perform()
        if not turbo_mode:
            checklist_WEB.wait(self,2)
            
    def drag_and_drop_by_offset(self, element, x, y):
        checklist_WEB.wait_until_visible(self, element)        
        actionChains = ActionChains(checklist_WEB.get_current_driver(self))
        actionChains.drag_and_drop(checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick), x, y).perform()
        if not turbo_mode:
            checklist_WEB.wait(self,2)
            
    def input_text_into(self, element, text, clearfirst=False):
        checklist_WEB.wait_until_visible(self, element)
        elementToClick = elements.get_xpath(self, element)
        if clearfirst:
            checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick).clear()
        checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick).send_keys(text)
        #element.send_keys(" and some", Keys.ARROW_DOWN)
        #element.clear()
        if not turbo_mode:
            checklist_WEB.wait(self,2)

    def clear_text_of(self, element):
        checklist_WEB.wait_until_visible(self, element)
        elementToClick = elements.get_xpath(self, element)
        checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick).clear()
        
        if not turbo_mode:
            checklist_WEB.wait(self,2)

    def get_text_from(self, element, compare_string=None):
        checklist_WEB.wait_until_visible(self, element)
        elementToClick = elements.get_xpath(self, element)
        elementText = checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick).text
        if (compare_string!=None):
            assert(elementText == compare_string), "[NotEqualError] Element Text (\"" + elementText +  "\") is different from given comparison string (\"" + compare_string +"\")" 
            return (elementText == compare_string)
        return elementText


    def scroll_page(self, x_axis_percentage=0, y_axis_percentage=0):
        driver = checklist_WEB.get_current_driver(self)
        scrollWidth = driver.execute_script("return document.body.scrollWidth") * x_axis_percentage
        scrollHeight = driver.execute_script("return document.body.scrollHeight") * y_axis_percentage
        driver.execute_script("window.scrollTo("+ str(scrollWidth) + ", "+ str(scrollHeight)+");")
        if not turbo_mode:
            checklist_WEB.wait(self,2)

    def scroll_to(self, element):
        driver = checklist_WEB.get_current_driver(self)
        elementToClick = elements.get_xpath(self, element)
        element = checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        if not turbo_mode:
            checklist_WEB.wait(self,2)

    def hover(self, element):
        driver = checklist_WEB.get_current_driver(self)
        elementToClick = elements.get_xpath(self, element)
        element = checklist_WEB.get_current_driver(self).find_element_by_xpath(elementToClick)
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        #secondLevelMenu.click();
        if not turbo_mode:
            checklist_WEB.wait(self,2)

    def check_attribute(self, element, property, expected_value, contains=False, respectCapitalLetters=True):
        driver = checklist_WEB.get_current_driver(self)
        elementToClick = elements.get_xpath(self, element)
        elements_list = checklist_WEB.get_current_driver(self).find_elements_by_xpath(elementToClick)
        for item in elements_list:
            val = item.get_attribute(property)
            if contains and not respectCapitalLetters:
                assert (expected_value.lower() in val.lower())==True, "AssertionError: Expected value ('" + expected_value + "') is not contained in actual value ('" + val + "') to attribute: '" + property + "'"
            else:
                assert (val==expected_value)==True, "AssertionError: Expected value ('" + expected_value + "') is different from actual value ('" + val + "') to attribute: '" + property + "'"


    def wait(self, time):
        t.sleep(time)

    def get_current_screen(self):
        return checklist_Transitions.current_from_screen
