'''
From stocks data.... sort in increasing order of stocks price and find min, max etc and corresponding company name
'''

stocks = {
    'YAHOO' : 99.35,
    'AMAZON' : 329.93,
    'APPLE' : 123.35,
    'FLIPKART' : 45.45,
    'GOOGLE' : 213.34
}

print(min(zip(stocks.values(), stocks.keys())))  # list will be sorted with respect to values ans values is first argument

print(max(zip(stocks.values(), stocks.keys())))   # prints Max from List

print(sorted(zip(stocks.values(), stocks.keys())))  # sorted as per values

print(sorted(zip(stocks.keys(), stocks.values())))   # sorted as per key values i.e. alphabet wise