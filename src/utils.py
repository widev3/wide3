import locale
import requests


def check_server(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def stof_locale(str):
    try:
        return float(str)
    except:
        try:
            return locale.atof(str)
        except:
            return 0
