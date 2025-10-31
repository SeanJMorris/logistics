import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://aliandseanwedding.streamlit.app/", wait_until="load")
    time.sleep(5)

    def page_is_appearing_correctly():
        standard_page_is_present = page.get_by_text("I Have Responsibilities").is_visible()
        if standard_page_is_present:
            print("Page is appearing correctly.")
            return True
        else:
            return False

    def page_is_asleep():
        wake_up_button = page.get_by_text("Yes, get this app back up!").is_visible()
        if wake_up_button:
            print("Page is asleep, attempting to wake up...")
            wake_up_button.click()
            print("Clicked wake up button, waiting 60 seconds and will hope that this did something...")
            time.sleep(60)
            return True
        else:
            return False

    def page_has_some_other_error():
        message = "Error running app. If this keeps happening, please contact support."
        error_message = page.get_by_text(message).is_visible()
        if error_message:
            print(f"Page is showing the '{message}' message.")
            return True
        else:
            return False

    if not page_is_appearing_correctly() and not page_is_asleep() and not page_has_some_other_error():
        print("Unknown error occurred.")

    # ---------------------
    context.close()
    browser.close()

    #WILO on 10/27/25 - this worked after I added in the wait command on line 12. The next step is to test this after it goes to sleep so that it clicks on a button to wake it up. If this works, then you should be able to disable the automatic commit (but you don't have to). Then you also run this with the github action.

    #WILO on 10/30/25 - as of today, even when I tried to wake up the app by clicking on the wake up button, the app had this text: "Oh no. Error running app. If this keeps happening, please contact support."

def main():
    with sync_playwright() as playwright:
        run(playwright)
