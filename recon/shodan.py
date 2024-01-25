import os
import shodan

shodan_api_key = os.environ.get('SHODAN_API_KEY')
api = shodan.Shodan(shodan_api_key)

shodan_general_filters = [
    'all',
    'asn',
    'city',
    'country',
    'cpe',
    'device',
    'geo',
    'hash',
    'has_ssl',
    'has_vuln',
    'hostname',
    'isp',
    'ip',
    'link',
    'net',
    'org',
    'os',
    'port',
    'postal',
    'product',
    'region',
    'scan',
    'state',
    'version',
    'http.component',
    'http.html',
]


def search(query : str, filters : list = shodan_general_filters):
    try:
        results = api.search(query)
        return results
    except shodan.APIError as e:
        return e