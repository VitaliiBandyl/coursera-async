import requests
from time import time

url = 'https://loremflickr.com/320/240'


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    file_name = response.url.split('/')[-1]

    with open(f'D:\Python\Coursera\images\{file_name}', 'wb') as f:
        f.write(response.content)


def main():
    t0 = time()

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)


if __name__ == '__main__':
    main()
