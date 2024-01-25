import os
import requests
import json

vuldb_api_key = os.environ.get('VULDB_API_KEY')
internetDB_url = "https://internetdb.shodan.io/"

# TODO: InternetDB - This function takes an IP address as input and returns a list of ports and vulnerabilities associated with that IP.
# This function takes an IP address as input and returns a list of ports and vulnerabilities associated with that IP.
def ports_and_vuls(ip : str):
    try:
        response = requests.get(internetDB_url + ip)
        return response.json()
    except requests.exceptions.RequestException as e:
        return e
    except json.JSONDecodeError as e:
        return e
    except Exception as e:
        return e
    
# TODO: VulDB - This function takes a query as input and returns a list of vulnerabilities associated with that query.
 # This function takes a query as input and returns a list of vulnerabilities associated with that query.   
def search_vuldb(query : str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'X-VulDB-ApiKey': vuldb_api_key
    }
    try:
        response = requests.post('https://vuldb.com/?api', headers=headers, data={'search': query})
        return response.json()
    except requests.exceptions.RequestException as e:
        return e
    except json.JSONDecodeError as e:
        return e
    except Exception as e:
        return e


