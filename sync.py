from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False, slow_mo = 50) #creates a chromium browser
    page = browser.new_page() #creates a new page
    page.goto('https://www.google.com/search?sca_esv=84b4ab2849dc3d2a&rlz=1C5OZZY_enUS1148US1148&udm=2&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3vWUtYx0DZdicpfE1faGYemg2KC4yuMPyQlIvlWqq2At2yMvCZgi_bwXXU0sv2NZz2VHRSLiUHmthAMk7QQB16faWQ-JftmiAdFeqMSOLdXyHAiZXKgLooSfKIigGc2PG4gVHUqO279njgllvQY7MCROm9UYiXGghb8pffA-sjiff7Kg7Q&q=shoebill+stare&sa=X&ved=2ahUKEwiAlcTur62TAxVs4MkDHdWZPHQQtKgLegQIFBAB&biw=750&bih=823&dpr=2#sv=CAMSVhoyKhBlLVNTWjdFd1BPU2xGNnFNMg5TU1o3RXdQT1NsRjZxTToOcFRGNjFSNVctUlU1cE0gBCocCgZtb3NhaWMSEGUtU1NaN0V3UE9TbEY2cU0YADABGAcgmvWJowkwAkoIEAEYASABKAE') #tells the page to go to google
    