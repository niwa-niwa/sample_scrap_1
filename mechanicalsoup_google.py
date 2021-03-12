import mechanicalsoup

# create object of mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()

# target URL
browser.open('https://www.google.co.jp/')

# select form in google search page
browser.select_form('form[action="/search"]')
# q is name of input box
browser['q'] = 'Python'
# submit form
browser.submit_selected()

# To get result after submit 
page = browser.get_current_page()
# choose element of html and print the text
for a in page.select('h3'):
    print(a.text)
    print(browser.absolute_url(a.get('href')))
