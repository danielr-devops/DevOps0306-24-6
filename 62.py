from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("C:/Users/dan_r/My Drive/DevOpsExp/tip_calc/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
driver.find_element(by="id", value="peopleamt").send_keys("8")
driver.find_element(by="id", value="musicamt").send_keys("1")
driver.find_element(by="id", value="calculate").click()
expected = "2.88"
actual = driver.find_element(by="id", value="tip").text
if expected != actual:
    print("Failed")
else:
    print("Passed")
assert expected != actual, f"Expected: {expected}, Actual: {actual}"
sleep(5)
