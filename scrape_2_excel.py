import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define Url, make request and save the content
url = 'https://www.bankbazaar.com/reviews.html'

result = requests.get(url)

src = result.content

# Create bs object
soup = BeautifulSoup(src, features="lxml")

# get review text from bs object and set to array
review_text = []

review_text_element = soup.find_all(class_='text_here review-desc-more')

for item in review_text_element:
    review_text.append(item.text)

# get user names from bs object and set to array
user_name = []

user_name_element = soup.findAll(class_='js-author-name')

for item in user_name_element:
    user_name.append(item.text)

# get bank names from bs object and set to array
bank_name = []

bank_name_element = soup.findAll(class_='review-bank-title')

for item in bank_name_element:
    bank_name.append(item.find('img').get('alt'))

# create dataframe
final_data = []

for text, user, bank in zip(review_text, user_name, bank_name):
    final_data.append({'Review_Text': text, 'User': user, 'Bank': bank})

df = pd.DataFrame(final_data)

df.to_excel(r'C:\Users\natba\Documents\scrape_2_excel_files\bank_bazaar.xlsx',
            index=False, header=True)
