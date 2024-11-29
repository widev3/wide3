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


def rgb_to_lum(rgb):
    return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]


def new_rgb_lum(rgb, lum):
    return (
        (
            int(lum / rgb_to_lum([1, rgb[1] / rgb[0], rgb[2] / rgb[0]]))
            if rgb[0] != 0
            else 0
        ),
        (
            int(lum / rgb_to_lum([rgb[0] / rgb[1], 1, rgb[2] / rgb[1]]))
            if rgb[1] != 0
            else 0
        ),
        (
            int(lum / rgb_to_lum([rgb[0] / rgb[2], rgb[1] / rgb[2], 1]))
            if rgb[2] != 0
            else 0
        ),
    )


def freq_to_nm(freq):
    wavelength = 299792458 / freq
    wavelength_nm = wavelength * 1e9
    return wavelength_nm
