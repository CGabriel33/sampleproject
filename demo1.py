from selenium import webdriver
# need to declare the executable path inside the browser
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\IEDriverServer.exe")


driver.get("https://www.cambridgedev.org/go-qa/")
print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()