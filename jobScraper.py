from scrapling.fetchers import StealthyFetcher
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
from selenium import webdriver 
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from playwright.sync_api import Page
import pickle
import time

def scroll_page(page: Page):
    for _ in range(15):
        page.mouse.wheel(0, 10000)
        page.wait_for_timeout(3500)


def dice_scraping(keyword, no_of_pages):
    results = []
    for i in range(1, no_of_pages+1):
        page = StealthyFetcher.fetch(f"https://www.dice.com/jobs?q={keyword.replace(' ', '+')}&location=United+States&radiusUnit=mi&page={i}&latitude=38.7945952&longitude=-106.5348379&countryCode=US&locationPrecision=Country")
        data = page.xpath('//div[@class="self-stretch"]/a/@href').getall()
        for d in data:
            results.append(d)
    return results

def jobright_Scraping(main_url):
    results = set()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(main_url, wait_until="domcontentloaded")
        time.sleep(3)
        scroll_box = page.locator('//div[@id="scrollableDiv"]').first
        for _ in range(40):
            links = page.locator('a[class*="job-card"]')
            for l in links.all():
                href = "https://jobright.ai" + l.get_attribute("href")
                if href:
                    results.add(href)
            scroll_box.evaluate("el => el.scrollBy(0, 2000)")
            time.sleep(1.5)
        return list(results)




def built_in_scraping(keyword, no_of_pages):
    extension_path = r"C:\Users\anwaa\Downloads\Urban VPN"
    base_url = f"https://builtin.com/jobs/remote?search={keyword.replace(' ', '%20')}&daysSinceUpdated=1&country=USA&allLocations=true"
    browser = sync_playwright().start()
    context = browser.chromium.launch_persistent_context(user_data_dir="./user-data-dir", headless=False, args=[f"--disable-extensions-except={extension_path}", f"--load-extension={extension_path}"])
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://www.google.com")
    input("Enter to Exit....")
     
    # results = []
    # for i in range(1, no_of_pages+1):
    #     page = StealthyFetcher.fetch(base_url + f"&page={i}", headless=False, disable_resources=True)
    #     data = page.xpath('//a[@data-id="job-card-title"]/@href').getall()
    #     for d in data:
    #         results.append("https://builtin.com" + d)
    # return results

# print(jobright_Scraping(main_url="https://jobright.ai/jobs/search?value=Data+Engineer&searchType=job_title&country=US&jobTaxonomyList=%5B%7B%22taxonomyId%22%3A%2200-00-00%22%2C%22title%22%3A%22Data+Engineer%22%7D%5D&isH1BOnly=false&excludeStaffingAgency=false&excludeSecurityClearance=false&excludeUsCitizen=true&refresh=false&position=19&sortCondition=0&jobTypes=1%2C3%2C2&workModel=2&daysAgo=1"))

print(built_in_scraping("AI Engineer", 5))