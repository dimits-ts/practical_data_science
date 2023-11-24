from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import dateparser
import bs4
import time


#code credit https://serpapi.com/blog/scrape-youtube-video-page-with-python/
def scrape_youtube(driver, search_url: str, max_scrolls:int=10, 
                   scroll_wait_secs: float=1, verbose: bool=False) -> bs4.BeautifulSoup:
    """
    Scrape YouTube search results using a Selenium WebDriver.

    :param driver: Selenium WebDriver instance.
    :type driver: selenium.webdriver.remote.webdriver.WebDriver

    :param search_url: The URL of the YouTube search results page.
    :type search_url: str

    :param max_scrolls: Optional. The maximum number of times to scroll down the page.
    :type max_scrolls: int, default: 10

    :param scroll_wait_secs: Optional. The number of seconds to wait between each scroll.
    :type scroll_wait_secs: float, default: 1

    :param verbose: Optional. If True, print progress.
    :type verbose: bool, default: False

    :return: A BeautifulSoup object representing the scraped YouTube search results page.
    :rtype: bs4.BeautifulSoup

    This function uses a Selenium WebDriver to open the specified YouTube search URL, scrolls down 
    the page up to the specified maximum number of times, and returns the BeautifulSoup object representing
    the page source.
    """
    driver.get(search_url)

    old_height = driver.execute_script("""
        function getHeight() {
            return document.querySelector('ytd-app').scrollHeight;
        }
        return getHeight();
    """)
    scrolled_times = 0

    while scrolled_times <= max_scrolls:
        if verbose:
            print(f"Scrolling ({scrolled_times} out of max {max_scrolls})...")

        driver.execute_script("window.scrollTo(0, document.querySelector('ytd-app').scrollHeight)")

        time.sleep(scroll_wait_secs)
        scrolled_times += 1

        new_height = driver.execute_script("""
            function getHeight() {
                return document.querySelector('ytd-app').scrollHeight;
            }
            return getHeight();
        """)

        if new_height == old_height:
            break

        old_height = new_height

    soup = bs4.BeautifulSoup(driver.page_source, features="lxml")
    return soup


def extract_search_results(search_soup: bs4.BeautifulSoup) -> tuple[list[str], list[str]]:
    """
    Extract video titles and links from a YouTube search results page represented by a BeautifulSoup object.

    :param search_soup: A BeautifulSoup object representing the YouTube search results page.
    :type search_soup: bs4.BeautifulSoup

    :return: A tuple containing two lists - the first list represents video titles, and the second list represents video links.
    :rtype: tuple(list[str], list[str])
    """
    titles = []
    links = []
    video_tag = search_soup.find("ytd-app")

    for link_tag in video_tag.find_all("a", {"id": "video-title"}):
        titles.append(link_tag.get_text())
        links.append(link_tag.get("href"))

    return titles, links


def extract_comments(video_soup: bs4.BeautifulSoup) -> tuple[list[str], list[str]]:
    """
    Extract comments from a YouTube video page represented by a BeautifulSoup object.

    :param video_soup: A BeautifulSoup object representing the YouTube video page.
    :type video_soup: bs4.BeautifulSoup

    :return: A tuple containing a list of strings representing the extracted comments and a 
    list containing the respective dates the comments were posted.
    :rtype: tuple[list[str], list[str]]
    """
    comment_tags = video_soup.find_all("yt-formatted-string", {"id": "content-text"})
    comments = [comment_tag.get_text() for comment_tag in comment_tags]
    
    date_tags = video_soup.find_all("yt-formatted-string", class_= "published-time-text")
    date_texts = [date_tag.find("a").get_text().strip() if date_tag is not None else None 
                  for date_tag in date_tags]
    date_texts = [text.replace("(edited)", "").replace("(τροποποιήθηκε)", "") 
                 for text in date_texts]
    dates = [dateparser.parse(date_text) for date_text in date_texts]
    
    assert len(dates) == len(comments), f"{len(dates)} != {len(comments)} "
    return comments, dates