from urllib.request import Request, urlopen
import bs4


def fetch_soup(url: str) -> bs4.BeautifulSoup:
    """
    Fetch and parse the HTML content of a web page using BeautifulSoup.

    :param url: The URL of the web page to be fetched and parsed.
    :type url: str
    :return: A BeautifulSoup object representing the parsed HTML content.
    :rtype: bs4.BeautifulSoup
    """
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()
    return bs4.BeautifulSoup(html_page, 'html.parser')