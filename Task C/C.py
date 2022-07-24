import json
from datetime import datetime


def lambda_date(date1, date2, swap=False):
    if swap:
        return datetime.strptime(date1, "%d.%m.%Y") >= date2
    else:
        return date2 >= datetime.strptime(date1, "%d.%m.%Y")


def lambda_price(price1, price2):
    return price1 >= price2

def correct_candidate(name, price_l, price_r, date_l, date_r, item):
    if name in item['name'].lower() \
            and lambda_date(item['date'], date_r) \
            and lambda_date(item['date'], date_l, True) \
            and lambda_price(price_r, item['price']) \
            and lambda_price(item['price'], price_l):
        return True

    return False

data = json.loads(input())

name = ''
price_l = 0
price_r = 0
date_l = datetime.now()
date_r = datetime.now()

for i in range(5):
    line = input().split()
    if line[0] == "NAME_CONTAINS":
        name = line[1].lower()
    elif line[0] == "PRICE_GREATER_THAN":
        price_l = int(line[1])
    elif line[0] == "PRICE_LESS_THAN":
        price_r = int(line[1])
    elif line[0] == "DATE_AFTER":
        date_l = datetime.strptime(line[1], "%d.%m.%Y")
    else:
        date_r = datetime.strptime(line[1], "%d.%m.%Y")

products = []

for item in data:
    if correct_candidate(name, price_l, price_r, date_l, date_r, item):
        products.append(item)

products.sort(key=lambda x: x['id'])
print(json.dumps(products))
