from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.common.keys import Keys


# for configure browser
options = ChromeOptions()

# excute with headless mode
options.headless = True

# create object of browser
browser = Chrome(options=options)

# broweser open the URL
browser.get('https://www.google.co.jp/')

# Make sure that Google is included in the title
assert 'Google' in browser.title

# input word that you search with and send it
input_element = browser.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# Make sure that Python is included in the title
assert 'Python' in browser.title

# take a screen shot
browser.save_screenshot('search_results.png')

# print the result in the command line
for h3 in browser.find_elements_by_css_selector('a> h3'):
    a = h3.find_element_by_xpath('..')
    print(h3.text)
    print(a.get_attribute('href'))

# quit browser
browser.quit()
