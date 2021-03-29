import asyncio
from pyppeteer import launch


async def main():
    
    # create an object of browser
    # if headless is not enable  "await launch(headless=False)"
    browser = await launch()

    # open Google
    page = await browser.newPage()
    await page.goto('https://www.google.co.jp/')

    # Make sure that Google is include in the title
    assert 'Google' in (await page.title())

    # input words to search
    input_element = await page.querySelector('[name="q"]')
    await input_element.type('Python')

    # send a form and wait next page come back
    await asyncio.wait([
        input_element.press('Enter'),
        page.waitForNavigation(),
    ])

    # Make sure that Python is include in the title
    assert 'Python' in (await page.title())

    # Take a screen shot
    await page.screenshot({'path':'search_results_2.png'})

    # Print result
    for h3 in await page.querySelectorAll('a>h3'):
        text = await page.evaluate('(e)=>e.textContent', h3)
        print(text)
        a = await page.evaluateHandle('(e)=>e.parentElement', h3)
        url = await page.evaluate('(e)=>e.href', a)
        print(url)

    # Quit a browser
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
