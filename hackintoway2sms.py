from splinter import Browser
browser=Browser('firefox')
browser.visit('http://www.way2sms.com/content/index.html')
browser.find_by_name('username').fill('mob')
browser.find_by_name('password').fill('pass')
browser.find_by_name('Login').click()
browser.find_by_css('.boo.I4').click()
browser.find_by_id('quicksms').click()

with browser.get_iframe('frame') as iframe:  
    browser.find_by_name('textArea').fill('textttareaarereara')
    browser.find_by_css('.inp').fill('9710101067')
    browser.find_by_name('Send').click()

