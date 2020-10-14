from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
import time
import sys
import random

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('http://localhost:8000')
time.sleep(5)

Name        = driver.find_element_by_css_selector("#id_name")
Department  = Select(driver.find_element_by_css_selector("#id_departments"))
Employer    = driver.find_element_by_css_selector("#id_employer")
Package     = driver.find_element_by_css_selector("#id_package")
ReferenceNo = driver.find_element_by_css_selector("#id_ref_no")
YearAd      = driver.find_element_by_css_selector("#id_year_admission")
YearDown    = driver.find_element_by_css_selector("#id_year_down")
Add         = driver.find_element_by_css_selector("input.btn:nth-child(10)")

num = sys.argv

if len(num) > 1:
    for i in range (0,int(num[1])):
        Name        = driver.find_element_by_css_selector("#id_name")
        Department  = Select(driver.find_element_by_css_selector("#id_departments"))
        Employer    = driver.find_element_by_css_selector("#id_employer")
        Package     = driver.find_element_by_css_selector("#id_package")
        ReferenceNo = driver.find_element_by_css_selector("#id_ref_no")
        YearAd      = driver.find_element_by_css_selector("#id_year_admission")
        YearDown    = driver.find_element_by_css_selector("#id_year_down")
        Add         = driver.find_element_by_css_selector("input.btn:nth-child(10)")

        Name.send_keys("sd")
        Department.select_by_index(random.randrange(0,4))
        Employer.send_keys("idk")
        Package.send_keys("{}".format(i+1000))
        ReferenceNo.send_keys("007")
        YearAd.send_keys("2018")
        YearDown.send_keys("1")
        time.sleep(1)
        Add.click()
        time.sleep(3)

else :
    Name.send_keys("sd")
    Department.select_by_index(0)
    Employer.send_keys("idk")
    Package.send_keys("1000")
    ReferenceNo.send_keys("007")
    YearAd.send_keys("2018")
    YearDown.send_keys("1")
    time.sleep(1)
    Add.click()
    time.sleep(3)