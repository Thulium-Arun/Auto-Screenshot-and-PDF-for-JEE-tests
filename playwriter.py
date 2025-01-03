import time
from playwright.sync_api import sync_playwright
import os

ID = "0000000000000"
Password = "Password"

def open_login1(p):

    browser = p.chromium.launch_persistent_context(headless = False,slow_mo=500,user_data_dir="Data")

    #context = browser.new_context(storage_state= "state.json")
    page = browser.new_page()

    page.set_viewport_size({"width":1080,"height":2000})


    page.goto('https://glorifire.com/home')
    
    page.fill("input#txtloginemail",ID)
    page.click('button[type=submit]')

    page.get_by_text("Glorifire Login").click()

    page.get_by_placeholder("Enter Password").fill(Password)
    page.click('button[type=submit]')

    try:
        page.get_by_role("button",name="Yes",timeout=100).click()
    except:
        pass

    """    page.get_by_role("button",name="Remove").nth(2).click()
    page.get_by_role("button",name="Yes").click()
    time.sleep(50)"""

    # Save storage state into the file.
    #storage = context.storage_state(path="state.json")

    return page

def open_login_new(p):
    browser = p.chromium.launch_persistent_context(headless=False,slow_mo=500,user_data_dir="Data")

    #context=browser.new_context()

    page = browser.new_page()

    page.set_viewport_size({"width":1080,"height":1080})

    page.goto('https://glorifire.com/home')
    
    page.fill("input#txtloginemail",ID)
    page.click('button[type=submit]')

    page.get_by_text("Glorifire Login").click()

    page.get_by_placeholder("Enter Password").fill(Password)
    page.click('button[type=submit]')
    try:
        page.get_by_role("button",name="Yes",timeout=100).click()
    except:
        pass

    page.get_by_role("button",name="Remove").nth(2).click()
    try:
        page.get_by_role("button",name="Yes",timeout=100).click()
    except:
        pass

    #to let OTP be entered
    time.sleep(5)

    # Save storage state into the file.
    #storage = context.storage_state(path="state.json")

    page.wait_for_load_state("networkidle")
    return page

def open_login_saved(p):

    # Create a new context with the saved storage state.

    browser = p.chromium.launch_persistent_context(headless=False,slow_mo=100,user_data_dir="Data")

    page = browser.pages [0]

    page.set_viewport_size({"width":2096,"height":2400})

    page.goto('https://glorifire.com/home')

    return page

def take_pictures(section_name,page,i,name):
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    questions = page.locator("css=div.notice.select_questionnotice.q-num-container").all()

    for question in questions:
        question.click()  
        page.wait_for_load_state("networkidle")
        time.sleep(1.5)
        question.locator("xpath=..").screenshot(path=f"screenshots/{name}/{section_name}_{i:02d}.png",timeout=1000)  # Save screenshot with ID
        print(f"ID | {i:02d} | {name}")
        i+=1
    return i

with sync_playwright() as p:
    #p=sync_playwright().start()

    page = open_login_saved(p)
    print("logged in")
    page.wait_for_load_state("networkidle")
    time.sleep(3)
    page.get_by_text("Test History").click()

    time.sleep(10)

    """for j in range(10):
        page.mouse.wheel(0, 10000)
        time.sleep(1)

    
    time.sleep(3)
    tests=page.get_by_text("View Result").all()
    j=0
    for test in tests:
        test.click()
        name = page.get_by_role("heading").nth(0).inner_text().replace("/","-")
        print(f"{j}. {name}")
        j+=1
    
    s = int(input("Till which test would you like to start?"))
    e = int(input("Till which test would you like to be recorded?"))"""


    #for test in page.get_by_text("View Result").all():
    test = page.get_by_text("View Result").nth()
    test.click()
    time.sleep(4)
    name = page.get_by_role("heading").nth(0).inner_text().replace("/","-")

    os.makedirs(os.path.join("screenshots",name),exist_ok=True)

    page.get_by_text("View Full Result").nth(0).click()
    page.get_by_text("Question-wise Performance").click()
    page.wait_for_load_state("networkidle")
    print("question wise opened")
    i=1
    time.sleep(5)
    for section in page.locator("css=div.owl-item.active").all():
        time.sleep(5)
        section.click()
        time.sleep(5)
        i = take_pictures(section.all_inner_texts(),page,i,name)
    time.sleep(5)

    page.locator("css=a.cross-button.d-none.d-sm-none.d-md-block").click()
    time.sleep(4)

    page.get_by_role("button").nth(0).click() 

        

#page.locator("Div","_ngcontent-rin-c312").click()
#page.locator("#01").screenshot(path = "screenshot1.png")   




"""for i in range(1, 21):  # Adjust range as needed
    selector = f'div.notice.select_questionnotice[id="{i:02d}"]'
    question_div = page.locator(selector)  # Wait up to 10 seconds



    if question_div:
        question_div.click()
        page.wait_for_timeout(1000)
        
        try:  
            question_div.locator("xpath=..").screenshot(path=f"Screenshots/screenshot_{i:02d}.png",timeout=1000)  # Save screenshot with ID
            print(f"ID {i:02d} | Proper")
        except:
            page.screenshot(path=f"Screenshots/screenshot_{i:02d}.png")  # Save screenshot with ID
            print(f"ID {i:02d} | To be cropped....")
            
    else:
        print(f"Question div with ID {i:02d} not found.")"""






