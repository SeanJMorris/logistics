import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://aliandseanwedding.streamlit.app/")
    page.locator("iframe[title=\"streamlitApp\"]").content_frame.get_by_role("link", name="I Have Responsibilities").click()
    time.sleep(5)
    page.locator("iframe[title=\"streamlitApp\"]").content_frame.get_by_test_id("stBaseButton-secondary").click()
    page.locator("iframe[title=\"streamlitApp\"]").content_frame.get_by_test_id("stDialog").get_by_test_id("stBaseButton-secondary").click()
    page.locator("iframe[title=\"streamlitApp\"]").content_frame.get_by_role("link", name="Decor Inventory").click()

    time.sleep(10)
    # ---------------------
    context.close()
    browser.close()

    #WILO on 10/27/25 - this worked after I added in the wait command on line 12. The next step is to test this after it goes to sleep so that it clicks on a button to wake it up. If this works, then you should be able to disable the automatic commit (but you don't have to). Then you also run this with the github action.


with sync_playwright() as playwright:
    run(playwright)
