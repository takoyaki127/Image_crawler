from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Chrome():
    # ブラウザの設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')

    def __init__(self):
        self.driver = webdriver.Chrome(
            '/chromedriver.exe', options=Chrome.options)
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.close()

    def search_img(self, url, min_width=50, min_height=50, size_lower_limit=True):
        width = min_width
        height = min_height

        self.driver.get(url)
        img_tags = self.driver.find_elements(By.XPATH, "//img")

        img_urls = []
        for img_tag in img_tags:
            img_url = self.__excluded_small_image(
                img_tag, width, height, size_lower_limit)
            if img_url:
                img_urls.append(img_url)

        return img_urls

    def __excluded_small_image(self, img_tag: WebElement, width, height, size_lower_limit):
        if size_lower_limit == False:
            return img_tag.get_attribute('src')
        if self.__isLarge(img_tag, 'width', width):
            if self.__isLarge(img_tag, 'height', height):
                return img_tag.get_attribute('src')
        return None

    def __isLarge(self, tag: WebElement, side, size):
        return int(tag.get_attribute(side)) >= size
