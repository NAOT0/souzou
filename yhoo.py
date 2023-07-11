import requests


def reaaaad(searchJanCode):
    YahooItemSearchURL = ('https://shopping.yahooapis.jp/ShoppingWebService/'
                          'V3/itemSearch')

    params = {}
    params['appid'] = ('dj00aiZpPXJ4ZHVxZGdVWmIydCZ'
                       'zPWNvbnN1bWVyc2VjcmV0Jng9Yjk-')
    params['jan_code'] = 'jan_code'
    params['jan_code'] = searchJanCode
    response = requests.get(YahooItemSearchURL, params)
    results = response.json()

    YitemName = results['hits'][0]['name']

    return YitemName
