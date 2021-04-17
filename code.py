from selenium import webdriver
import os
import subprocess
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.headless = True
path = os.getcwd()+"/geckodriver"
def hit():
	driver=webdriver.Firefox(options=opts,executable_path=path)
	print(driver)
	driver.get("http://www.slutbags.tk/video.php?id=1")
	print(driver)
	popunder = driver.find_elements_by_class_name("text-center")
	print(popunder)
	popunder[0].click()
	print(driver.window_handles)
	driver.switch_to.window(driver.window_handles[0])
#	time.sleep(3)
	print(driver.title)
	driver.switch_to.window(driver.window_handles[1])
#	time.sleep(3)
	print(driver.title)
	driver.close()
	subprocess.run(['./kill-firefox.sh'])
while True:
	hit()
