from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    page.fill("textarea[name='q']", "Swaraj Sourav – Senior QA Automation Journey STARTED TODAY")
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)
    print("DAY 1 SUCCESS – YOU ARE NOW AUTOMATING!")
    browser.close()