from bs4 import BeautifulSoup
import requests
import pandas as pd

user_data = []
date_data = []
title_data = []
star_data = []
review_data = []
number = []
no_of_pages = 4
temp_url = 'https://www.amazon.in/Redmi-Y3-Prime-Black-Storage/product-reviews/B07QNQPDTV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
j = 0
while(j <= no_of_pages):
    url = temp_url + "&pageNumber=%d" % j
    number.append(j)
    print(j)
    j = j + 1
    r = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    user = soup.find_all("span", {"class": "a-profile-name"})
    date = soup.find_all("span", {"class": "a-size-base a-color-secondary review-date"})

    title = soup.find_all("a", {
        "class": "a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"})
    star = soup.find_all("span", {"class": "a-icon-alt"})
    review = soup.find_all("span", {"class": "a-size-base review-text review-text-content"})
    helpful = soup.find_all("span", {"class": "a-size-base a-color-tertiary cr-vote-text"})

    for i in range(len(title)):
        title_data.append(title[i].text)
    for i in range(2, len(user)):
        user_data.append(user[i].text)
    for i in range(2, len(date)):
        date_data.append(date[i].text)
    for i in range(len(review)):
        star_data.append(star[i].text)
    for i in range(len(review)):
        review_data.append(review[i].text)
        # helpful_data.append(helpful[i].text)
    # print(user_data)
    # print(date_data)
    # print(title_data)
    # print(star_data)
#print(review_data)
df = pd.DataFrame(
    {'user': user_data, 'date': date_data, 'title': title_data, 'star': star_data, 'review': review_data})

df.to_csv('amazon_review.csv', index=False)
