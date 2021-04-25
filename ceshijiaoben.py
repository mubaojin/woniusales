from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://121.5.205.252:8050/woniusales/')

driver.maximize_window()

driver.find_element('id','username').send_keys('oooaaa11')
driver.find_element('id','password').send_keys('simonvic11')
driver.find_element('css selector','.form-control.btn-primary').click()
print('caonimabi')
