# Swaraj Sourav – 30-Day Senior QA Automation Challenge

Senior Manual QA (10+ yrs) → Full-stack Automation Engineer in 30 days  
**Day 1 COMPLETE** – Playwright + Selenium running on Mac

## Day 1 Proof
![Playwright running](day1_screenshot.png)  

<img width="443" height="299" alt="Screenshot 2025-11-27 at 5 59 28 PM" src="https://github.com/user-attachments/assets/8992368f-a0f5-4802-aa73-b5cd7ad78fe5" />


## Scripts
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    page.fill("textarea[name='q']", "Swaraj Sourav – Senior QA")
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)
    print("DAY 1 SUCCESS – YOU ARE NOW AUTOMATING!")
    browser.close()

Currently Refreshing: POM, Pytest, Allure, GitHub Actions, API testing  
Open to Senior SDET / Automation Lead roles (India + Remote)

Reach out → swarajsourav@gmail.com | +91-8431511113 | linkedin.com/in/swarajsourav
