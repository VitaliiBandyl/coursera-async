import requests
from bs4 import BeautifulSoup

url = 'https://www.unian.net/'


def get_html(url):
    r = requests.get(url)
    return r.content.decode()


def parse_titles(contents, selector='.link a'):
    soup = BeautifulSoup(contents, features='html.parser')
    selected = soup.select(selector)
    return selected


def strip_tabs(response):
    content = []

    for _ in response:
        content.append(response.pop(0).text)

    for index, _ in enumerate(content):
        content[index] = content[index].replace('Лайт', '\t').replace('Аналитика', '\t').strip()

    return content


if __name__ == '__main__':
    titles = parse_titles(get_html(url))
    title_name = strip_tabs(titles)

    times = parse_titles(get_html(url), '.link .time')

    time_text = [time.text for time in times]
    result = zip(time_text, title_name)
    to_write = []
    for time, title in result:
        to_write.append(f'{time}: {title} \n')

    with open("Unian_News.txt", 'w') as f:
        f.writelines(to_write)

