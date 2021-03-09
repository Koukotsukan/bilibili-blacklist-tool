from selenium import webdriver

browser = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser.get('https://www.bilibili.com')
browser.maximize_window()
with open ('space.txt','r') as f:
    url = f.readlines()
    url = [c.replace('\n','') for c in url]
    print (url)
    for i in url:
        js = 'window.open("' + i + '");'
        print (js)
        browser.execute_script(js)
