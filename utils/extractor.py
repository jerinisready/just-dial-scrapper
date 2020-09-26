from bs4 import BeautifulSoup

from utils.parser import Parser


class Extractor(object):

    def __init__(self, browser):
        self.browser = browser
        content = browser.driver.page_source.encode('utf-8').strip()
        self.soup_container = BeautifulSoup(content, "html.parser")
        self.soup_list = self.soup_container.findAll('li', {"class": "cntanr"})

    def __iter__(self):
        def generator():
            for soup in self.soup_list:
                yield Parser(soup)
        return generator()
