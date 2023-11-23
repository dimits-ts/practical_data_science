from src.data import Post, Thread
from src.util import fetch_soup
import dateparser
import bs4


def parse_warmane_thread(head_url: str, thread: bs4.Tag) -> Thread:
    """
    Parse the HTML content of a Warmane forum thread and return a Thread object.

    :param head_url: The base URL of the forum.
    :type head_url: str
    :param thread: The BeautifulSoup Tag representing the thread to be parsed.
    :type thread: bs4.Tag
    :return: A Thread object representing the parsed thread.
    :rtype: Thread
    """
    title_tag = thread.find("a", {"class": "title"})
    title = title_tag.get_text().strip()
    thread_id = _extract_int(title_tag.get("id"))
    author = thread.find("dl", {"class": "threadauthor td"}).get_text().strip()

    thread = Thread(thread_id, title, author)

    posts = parse_warmane_posts(head_url, thread_id)
    for post in posts:
        thread.add_post(post)

    return thread


def parse_warmane_posts(head_url: str, thread_id: int) -> list[Post]:
    """
    Parse the HTML content of Warmane forum posts within a thread and return a list of Post objects.

    :param head_url: The base URL of the forum.
    :type head_url: str 
    :param thread_id: The identifier of the thread.
    :type thread_id: int
    :return: A list of Post objects representing the parsed posts.
    :rtype: list[Post]
    """
    posts = []

    url = _get_thread_url(head_url, thread_id)
    post_soup = fetch_soup(url)

    if post_soup is None:
        print("Error fetching " + url)

    post_tags = post_soup.find_all("ol", {"id": "posts"})[0].find_all("li", recursive=False)

    last_post_id = None

    for post_tag in post_tags:
        try:
            post_id = _extract_int(post_tag.get("id"))
            post_author = post_tag.find(class_="userinfo").find("strong").get_text().strip()
            content = post_tag.find(class_="content").find("blockquote").get_text().strip()

            date_text = post_tag.find(class_="date").find("a").get_text().strip()
            date     = dateparser.parse(date_text)

            post = Post(post_id, thread_id, post_author, content, date, last_post_id)
            last_post_id = post_id
            posts.append(post)
        except Exception as e:
            print("ERROR: Failed to get information on post ", url)

    return posts


def _get_thread_url(head_url: str, thread_id: str) -> str:
    """
    Generate the URL for a specific Warmane forum thread.

    :param head_url: The base URL of the forum.
    :type head_url: str
    :param thread_id: The identifier of the thread.
    :type thread_id: str
    :return: The URL of the specified thread.
    :rtype: str
    """
    return f"{head_url}/showthread.php?t={thread_id}"

import re


def _extract_int(string: str) -> int|None:
    """
    Get the first integer from a string.
    :param string: the string
    :return: the integer if found, else None
    """
    number = re.findall("\d+", string)[0]
    if number is None:
        return None
    else:
        return int(number)