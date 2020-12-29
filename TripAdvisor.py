from selenium import webdriver

# access the browser driver [in incognito mode and without
# opening a browser window (headless argument)]
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="/mnt/c/Users/Public/chromedriver_win32 (1)/chromedriver.exe", chrome_options=options)
# driver = webdriver.Chrome(executable_path="C:\Users\Public\chromedriver_win32\chromedriver.exe", chrome_options=options)

# Get Trip Advisor review page and click relevant buttons
import time

# driver = webdriver.Chrome("C:\Users\Public\chromedriver_win32")
driver.get("https://www.tripadvisor.com/Restaurant_Review-g34733-d17387315-Reviews-Little_Hen-Weston_Broward_County_Florida.html")
more_buttons = driver.find_elements_by_class_name("taLnk ulBlueLinks")

for x in range(len(more_buttons)):
    if more_buttons[x].is_displayed():
        driver.execute_script("arguments[0].click();", more_buttons[x])
        time.sleep(1)
page_source = driver.page_source

# Hand off the manipulated page source to BeautifulSoup
from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'html.parser')
reviews = []
reviews_selector = soup.find_all('div', class_='reviewSelector')
for review_selector in reviews_selector:
    review_div = review_selector.find('div', class_='prw_rup prw_reviews_text_summary_hsx')
    # if review_div is None:
    #     review_div = review_selector.find('div', class_='partial_entry')
    review = review_div.find('div', class_='entry').find('p').get_text()
    review = review.strip()
    reviews.append(review)
    file = open("TripAdvisorReviews.txt", "w")
    for customerReview in reviews:
        file.write(customerReview + "\n")
    file.close()