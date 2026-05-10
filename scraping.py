from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve 


def scrape_page_for_image(prompt):
    pw = sync_playwright().start()

    browser = pw.chromium.launch(
        headless = False,
        slow_mo = 200
    )
    page = browser.new_page()
    page.goto("https://unsplash.com/")

    page.get_by_placeholder("Search photos and illustrations").nth(0).fill(prompt)

    page.get_by_role("button", name="Search Unsplash").first.click()

    button_links = page.locator("xpath = //a[@data-testid='non-sponsored-photo-download-button']").all()[:20]

    for button in button_links:

        button.evaluate("node => node.removeAttribute('target')")
        
        with page.expect_download(timeout=10000) as download_info:
            button.click(force = True)
        
        download = download_info.value
        download.save_as('/Images/' + download.suggested_filename)

    print(page.title())

    browser.close()
