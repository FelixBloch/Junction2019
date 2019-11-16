# get the data from api the company gives.

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'x-api-key': 'jmdSHjy6WPaXwoR75E6mJ1ImhxKPRJb51v6DBS0A'
}

base_url = 'https://junction.dev.qoco.fi/api/'


def request_baggage():
    url = base_url + 'baggage'
    r = requests.get(url, headers=headers)
    with open('baggage.json', 'wb') as f:
        f.write(r.content)


def request_customers():
    url = base_url + 'customers'
    r = requests.get(url, headers=headers)
    with open('customers.json', 'wb') as f:
        f.write(r.content)


def request_event(baggage_id):
    url = base_url + 'events/{}'.format(baggage_id)
    r = requests.get(url, headers=headers)
    print(r.content.decode(encoding='utf-8'))


request_baggage()
request_customers()
request_event('90cda708-b57d-4195-b30d-627e9f99ea36')
