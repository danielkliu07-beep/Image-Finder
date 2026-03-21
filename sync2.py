from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve #for making files into urls

pw = sync_playwright().start() #assigns expression to pw variable

browser = pw.firefox.launch(
    headless = False,
    slow_mo = 20000

) #launches firefox

page = browser.new_page() #creates a page that can navigate to any website
page.goto("https://arxiv.org/search") #goes to arxiv page

page.get_by_placeholder("Search term...").fill(
    "neural network"

) #locates a text bar with 'Search term...' as a placeholder and fills in the text bar with the given text
page.get_by_role("button").get_by_text(
    "Search"
).nth(1).click() #locates a button on the page that's titled 'Search' in the html and clicks it
#The .nth() function makes it so that the button is clicked the 2nd time since there's 2 buttons titled 'Search'
#.nth(0) is the first instance, .nth(1) is the second instance, and so on

#Xpath can target elements with specific property values
links = page.locator(
    "xpath = //a[contains(@href, 'arxiv.org/pdf')]"

).all() #locates all elements that is an href and has 'arxiv.org/pdf' in its <a href = "https://arxiv.org/pdf/..."> bracket
#//a selects all of the anchors on the page. The square brackets [] narrows the anchors down.
#Note: the <a> tag with href attribute is used to create a link when clicked



for link in links:
    url = link.get_attribute("href")
    urlretrieve(url, "ResearchPapers/" + url[-5:] + ".pdf") #saves the following link as a pdf file in the ResearchPapers folder
    #url[-5:] removes every character of the link except the last 5 and .pdf makes it a pdf file



print(page.title()) #prints the title of the page
page.screenshot(path = "example.png") #creates a screenshot of the page with the given path


browser.close() #collapses the browser once we are done using it

