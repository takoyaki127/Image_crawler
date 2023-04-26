import os
import requests
import datetime
import time
from tqdm.contrib import tenumerate

from Chrome import Chrome


def now():
    dt_now = datetime.datetime.now()
    current_time = dt_now.strftime(f"%Y_%m%d_%H%M%S")
    return current_time


def read_file():
    try:
        with open('./settings.txt', mode='r') as f:
            dir = f.read().split('=')[1]
            return dir
    except:
        print('settings.txtファイルが見つかりません')
        exit()


def create_directly(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def download_image(url, file_path):
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(r.content)


def main():
    file = read_file()
    browser = Chrome()
    page_url = input('URL->')

    img_urls = browser.search_img(page_url, size_lower_limit=False)
    if img_urls:
        current_time = now()
        folder_name = f'{file}/{current_time}'
        create_directly(folder_name)

        for i, img_url in tenumerate(img_urls):
            download_image(img_url, f'{folder_name}/{i}.png')
            time.sleep(0.5)

    browser.close()


if __name__ == "__main__":
    main()
