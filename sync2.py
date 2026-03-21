from playwright.sync_api import sync_playwright

pw = sync_playwright().start() #assigns expression to pw variable

browser = pw.firefox.launch() #launches firefox

page = browser.new_page() #creates a page that can navigate to any website
page.goto("http://google.com")

print(page.content()) #prints the source code of the page
print(page.title()) #prints the title of the page
page.screenshot(path = "example.png") #creates a screenshot of the page with the given path


browser.close() #collapses the browser once we are done using it

