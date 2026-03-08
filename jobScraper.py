from scrapling.fetchers import StealthyFetcher
import requests

# page = StealthyFetcher.fetch('https://www.ihire.com/search#/search?k=Data+Engineer&loc=USA&d=50&rem=false&hyb=false&inp=false&o=14&st=aggregation&ctc=17&ages=1')
# data = page.xpath('//a[@data-ref="anonymous-search-jobs-itemclick"]/@href').getall()
# print(data)

def ihire_scraping(keyword, no_of_pages):
    login_url = "https://www.ihire.com/Jobseeker/account/signin"
    base_url = f"https://www.ihire.com/search#/search?k={keyword.replace(" ", "+")}&loc=USA&d=50&rem=false&hyb=false&inp=false&o=14&st=page&ctc=17&ages=1&p="
    payload = {
        "email": "anwaarmirza65@gmail.com",
        "password": "#Nobel282"
    }
    results = []
    session = requests.Session()
    session.post(login_url, data=payload)
    cookies = [
        {"name": k, "value": v, "domain": ".ihire.com", "path": "/"}
        for k, v in session.cookies.get_dict().items()
    ]
    for i in range(1, no_of_pages+1):
        page = StealthyFetcher.fetch(base_url + f"{i}", cookies=cookies)
        data = page.xpath('//a[@data-ref="anonymous-search-jobs-itemclick"]/@href').getall()
        data = ["https://www.ihire.com" + d for d in data]
        for d in data:
            results.append(d)
    return results

def dice_scraping(keyword, no_of_pages):
    results = []
    for i in range(1, no_of_pages+1):
        page = StealthyFetcher.fetch(f"https://www.dice.com/jobs?q={keyword.replace(' ', '+')}&location=United+States&radiusUnit=mi&page={i}&latitude=38.7945952&longitude=-106.5348379&countryCode=US&locationPrecision=Country")
        data = page.xpath('//div[@class="self-stretch"]/a/@href').getall()
        for d in data:
            results.append(d)
    return results



def built_in_scraping(keyword, no_of_pages):
    results = []
    for i in range(1, no_of_pages+1):
        page = StealthyFetcher.fetch(f"https://builtin.com/jobs/hybrid?search={keyword.replace(' ', '%20')}&country=USA&allLocations=true&page={i}")
        data = page.xpath('//a[@data-id="job-card-title"]/@href').getall()
        for d in data:
            results.append("https://builtin.com" + d)
    return results

print(built_in_scraping("Data Engineer", 2))