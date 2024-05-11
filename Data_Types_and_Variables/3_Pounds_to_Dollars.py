pounds = int(input())
dollars = 1.31 * pounds

print(f'{dollars:.3f}')

#import requests

#def convert_gbp_to_usd(amount):
#    response = requests.get('http://api.exchangerate-api.com/v4/latest/GBP')
#    exchange_rates = response.json()['rates']
#    usd_rate = exchange_rates['USD']
#    usd_amount = amount * usd_rate

#    return usd_amount

#pounds = int(input('Enter an amount of pounds'))
#us_dollars = convert_gbp_to_usd(pounds)
#print(f'{pounds:.3f} GBP is equivalent to {us_dollars:.3f} USD')
