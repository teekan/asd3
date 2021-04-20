from selenium import webdriver
import os
import time
import subprocess
from selenium.webdriver.firefox.options import Options

#opts = Options()
#opts.headless = True
path = os.getcwd()+"/geckodriver"
def hit():
	try:
		driver=webdriver.Firefox(executable_path=path)
		driver.get("http://www.slutbags.tk/video.php?id=1")
		popunder = driver.find_elements_by_class_name("text-center")
	except Exception:
		subprocess.run(["sudo","./kill-gecko"])
	try:
		popunder[0].click()
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(1)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(1)
		driver.close()
	except Exception:
		subprocess.run(["sudo","./kill-firefox"])
		subprocess.run(["sudo","./kill-gecko"])
	try:
		time.sleep(1)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(1)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(1)
		driver.close()
		subprocess.run(['sudo','./delete-profiles'])
	except:
		print("Didn't complete workflow")

"""
	for x in driver.window_handles:
		driver.switch_to.window(x)
		print("Closing " + driver.title)
		driver.close()
"""
while True:
	hit()
