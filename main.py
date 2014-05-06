from urllib import request
from bs4 import BeautifulSoup

# This is a blacklist of bad links we do not want to follow
bad_links = ['_Greek', '_language', '_Language', 'Latin']
visited_urls = []


# This function takes in a URL and returns a dictionary containing the URL of the first link on the page as well as the
# word that was linked
def get_first_link(url):
    response = request.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html)
    body_text = soup.find(id='mw-content-text')

    print('Currently on ({0}) - {1}'.format(url, soup.title.get_text()))

    paragraphs = body_text.find_all('p')
    for paragraph in paragraphs:
        links = paragraph.find_all('a')
        for link in links:
            # Check the link starts with '/wiki/' as these are the ones we care about, it also must not contain a colon
            # or be in the blacklist of links
            url = link.get('href')
            if url.startswith('/wiki/') and not ':' in url and not is_bad_link(url) and not url in visited_urls:
                result = {
                    'title': link.get('title'),
                    'url': link.get('href')
                }

                return result

    return False


def is_bad_link(url):
    for link in bad_links:
        if url.endswith(link):
            return True

    return False

# First get a random Wikipedia page
base_url = 'http://en.wikipedia.org'
current_page = '/wiki/Special:Random'
target_page = '/wiki/Psychology'

run = True
while(run):
    new_data = get_first_link(base_url + current_page)

    if not new_data:
        print('No link found in page, aborting!')
        exit()

    current_page = new_data['url']

    if current_page == target_page:
        print('Reached Psychology!')
        run = False

    visited_urls.append(current_page)
