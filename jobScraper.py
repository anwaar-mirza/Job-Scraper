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

def ihire_scraping(keyword, no_of_pages):
    results = []
    # base_url = f"https://www.ihire.com/candidate/jobs/search?loc=Dallas,%20TX&d=100&k=#/search?loc=&d=0&k=data+engineer&rem=false&hyb=false&inp=false&st=aggregation&ages=1&empltype=1|2|3|4"
    base_url = f"https://www.ihire.com/search#/search?k={keyword.replace(' ', '+')}&loc=USA&d=50&rem=false&hyb=false&inp=false&o=14&st=page&ctc=17&ages=1&p="

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = uc.Chrome(version_main=145)
    driver.implicitly_wait(5)

    driver.get("https://www.ihire.com")

    with open(r"D:\Crawling\Geta Pro\LocalCh\cookies-ihire.pkl", "rb") as cookie:
        cookies = pickle.load(cookie)

    for c in cookies:
        driver.add_cookie(c)

    driver.get(base_url)
    driver.refresh()
    time.sleep(5)
    links = driver.find_elements(By.XPATH, '//a[@data-ref="anonymous-search-jobs-itemclick"]')
    driver.implicitly_wait(15)
    for l in links:
        results.append(l)
    return results

def dice_scraping(keyword, no_of_pages):
    results = []
    for i in range(1, no_of_pages+1):
        page = StealthyFetcher.fetch(f"https://www.dice.com/jobs?q={keyword.replace(' ', '+')}&location=United+States&radiusUnit=mi&page={i}&latitude=38.7945952&longitude=-106.5348379&countryCode=US&locationPrecision=Country")
        data = page.xpath('//div[@class="self-stretch"]/a/@href').getall()
        for d in data:
            results.append(d)
    return results

def jobright_Scraping(keyword, no_of_pages):
    results = []
    page = StealthyFetcher.fetch('https://jobright.ai/jobs/search?value=Data+Engineer&searchType=job_title&country=US&jobTaxonomyList=%5B%7B%22taxonomyId%22%3A%2200-00-00%22%2C%22title%22%3A%22Data+Engineer%22%7D%5D&isH1BOnly=false&excludeStaffingAgency=false&excludeSecurityClearance=false&excludeUsCitizen=true&refresh=false&position=19&sortCondition=0&jobTypes=1%2C3%2C2&workModel=2&daysAgo=1', page_action=scroll_page, headless=False)
    data = page.xpath('//a[@data-tut="jobs-card-match-score"]/@href').getall()
    return data



def built_in_scraping(keyword, no_of_pages):
    results = []
    for i in range(1, no_of_pages+1):
        page = StealthyFetcher.fetch(f"https://builtin.com/jobs/hybrid?search={keyword.replace(' ', '%20')}&country=USA&allLocations=true&page={i}")
        data = page.xpath('//a[@data-id="job-card-title"]/@href').getall()
        for d in data:
            results.append("https://builtin.com" + d)
    return results

print(len(jobright_Scraping("Data Engineer", 2)))