# import requests
# from bs4 import BeautifulSoup

# res = requests.get('https://www.icici.bank.in/personal-banking/loans/car-loan', verify=False)
# soup = BeautifulSoup(res.content, 'html.parser')

# print(soup.prettify())

# import requests
# res = requests.get('https://www.icici.bank.in/personal-banking/loans/car-loan')
# print(res.status_code)
# print(res.content)

import requests
from bs4 import BeautifulSoup

# Step 1: Fetch webpage
url = "https://www.icici.bank.in/personal-banking/loans/car-loan"
headers = {
    "User-Agent": "Mozilla/5.0"
}
res = requests.get(url, headers=headers)

# Step 2: Parse HTML
soup = BeautifulSoup(res.content, "html.parser")

# Step 3: Remove unwanted elements
for tag in soup(["script", "style", "noscript"]):
    tag.extract()

# Step 4: Extract text
text = soup.get_text(separator="\n")

# Clean text
lines = [line.strip() for line in text.splitlines()]
cleaned_text = "\n".join([line for line in lines if line])

# Step 5: Save to file
with open("icici_car_loan_content.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Content saved successfully!")