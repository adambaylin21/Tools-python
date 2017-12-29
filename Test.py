from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('https://viralstyle.com/Adam-Baylin/2018-just-believe-that-#pid=1&cid=230&sid=front')
source = browser.page_source
browser.quit()


print(source)