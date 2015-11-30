import requests

def download_url(url):
    """handle api calls with error catching"""
    response = requests.get(url)
    if response.status_code != 200:
        # http request error
        error = 'HTTPError: {}'.format(response.status_code)
        return {"success": False, "error": error}
    else:
        try:
            return response.json()
        except ValueError as error:
            return {"success": False, "error": error}
