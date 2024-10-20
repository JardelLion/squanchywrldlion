#get access on the site
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError



def access(url):
    """
    Get the HTML content of a website using the user agent of Mozilla.
    """
    try:
        request_access = Request(url, headers={"User-Agent": 'Mozilla/5.0'})
        with urlopen(request_access) as response:
            return response.read()  # Retorna o conteúdo da página
    except URLError:
        return 'URL Invalid, Please check your URL'
    except ValueError:
        return "You passed an invalid value"
    except HTTPError:
        return "This page doesn't exist"
