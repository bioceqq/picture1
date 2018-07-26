#!python3.7
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www/baidu.com")
driver.add_cookie({'name':'BAIDUID','value':'449966089F31704046C69FE7FDB5E05E:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'kzVDlPTFlyRHJJfmdZcDhnZGdCOTU5TmdmZlJSVVkzS3hsb2hCai1UfmFabjViQVFBQUFBJCQAAAAAAAAAAAEAAAATUOsocWl5aWdhb3FpbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANrZVlva2VZbTG'})
driver.refresh()
username = driver.find_element_by_xpath(".//*[@id = 'ul']/a[7]").text
print(username)
driver.quit()
