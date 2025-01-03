import time
from playwright.sync_api import sync_playwright

p=sync_playwright().start()

browser = p.chromium.launch_persistent_context(headless=False,slow_mo=100,user_data_dir="Data")

page = browser.pages [0]

page.set_viewport_size({"width":2000,"height":912})

page.goto('https://glorifire.com/home')

page.wait_for_load_state("networkidle")
time.sleep(3)
page.get_by_text("Test History").click()

"""for j in range(10):
    page.mouse.wheel(0, 10000)
    time.sleep(1)


time.sleep(3)
tests=page.get_by_text("View Result").all()
j=0
for test in tests:
    test.click()
    time.sleep(2)
    name = page.get_by_role("heading").nth(0).inner_text().replace("/","-")
    print(f"{j}. {name}")
    page.get_by_role("button").nth(0).click() 
    time.sleep(1)
    for f in range(j):
        page.mouse.wheel(0,200)
        time.sleep(1)
    j+=1


s = int(input("Till which test would you like to start?   Ans->"))
e = int(input("Till which test would you like to be recorded?    Ans->"))"""
