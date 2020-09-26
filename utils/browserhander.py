import time

from selenium import webdriver


class BrowserHandler(object):
    sr_no = 1
    page_no = 1

    def __init__(self):
        self.driver = webdriver.Firefox()

    def close(self):
        self.driver.quit()

    def fetch(self, url):
        self.driver.get(url)

    def scroll_to_bottom(self):
        SCROLL_PAUSE_TIME = 2.5
        script_to_get_page_count = "return document.querySelectorAll('#srchpagination  a').length"
        count_of_pages = self.driver.execute_script(script_to_get_page_count)
        # has one extra count but we are just ignoring that to be on safe part.
        script_to_scroll = """$('html, body > div').animate({
                scrollTop: $('#tab-5 ul > li.cntanr:last-child').offset().top - 100 
            }, 'slow')
        """
        for i in range(min(count_of_pages, 10)):
            self.driver.execute_script(script_to_scroll)
            time.sleep(SCROLL_PAUSE_TIME)
            while self.driver.find_elements_by_css_selector('section.ldmore:not(.dn)'):
                """
                Check weather if loader element exists!
                """
                time.sleep(SCROLL_PAUSE_TIME)

        return count_of_pages       # count of pages.