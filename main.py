import math
import sys
import time
import traceback

from utils.browserhander import BrowserHandler
from utils.csvhander import CsvHandler, clean
from utils.extractor import Extractor
from utils.inputhander import InputHandler
from utils.parser import Parser
additional_urls = []


def process(url_handler, firefox, csv_handler, process_additional_pages=False):

    for url in url_handler:
        sr_no = 1
        url = str(url)
        try:
            print("Surfing Over Just Dial ......!")
            print("LOADING : ", url)
            firefox.fetch(url)
            print("Scrolling to bottom just to make sure, all contents are loaded!")
            pagination_count = firefox.scroll_to_bottom()
            """
            Since the url is input from user, we have to be ready to handle ambiguity in urls.
                1. "..../Fabric-Retailers/nct-10890504"
                2. "..../Fabric-Retailers/nct-10890504/"
                3. "..../Fabric-Retailers/nct-10890504/page-1"
                4. "..../Fabric-Retailers/nct-10890504/page-1/"
                5. "..../Fabric-Retailers/nct-10890504/page-"
                6. "..../Fabric-Retailers/nct-10890504/page"
                ...
                ...
                for same input of first page.
                so we 
            """
            _formatted_url = url.rstrip('/')
            if pagination_count > 10 and process_additional_pages:
                """
                The Service provider supports only 10 pages as endless scrolling, 
                Hence, we need to scrape every 10th page! 

                if we are scraping the first page, and we have more than 10 pages, better we add 
                11th page, 21st page, 31st page ... etc to the urls, list! 
                """
                base_url = url.split('/page')[0] if '/page' in url else url
                print("adding further pages to list:", pagination_count)
                for tenth_digit in range(2, math.floor(pagination_count / 10)):
                    additional_urls.append(f'{base_url}/page-{tenth_digit + 1}')
                    print(f'Added: {base_url}/page-{tenth_digit + 1}')
            cards = Extractor(firefox)
            # firefox.driver.minimize_window()
            for soup in cards.soup_list:
                soup = Parser(soup)
                csv_handler.write_row(
                    '\n{name},  {summery}, {address}, {phone_num}, {verification}, {link}'.format(**{
                        'name': clean(soup.name),
                        'summery': clean(soup.summery),
                        'address': clean(soup.address),
                        'phone_num': clean(soup.contact),
                        'verification': clean(soup.verification),
                        'link': clean(soup.link),
                    }))
                print(f"Entry Item #{sr_no} : \t", soup.name)
                sr_no = sr_no + 1
            time.sleep(6)
            print("=" * 60)
            print(f"Loaded {sr_no - 1} items from :: {url}")
            print("=" * 40)
        except Exception as e:
            time.sleep(6)
            print("=" * 60)
            print('Error detected : ' + str(e.__class__.__name__) + '\n')
            print(e)
            print(traceback.format_exc())
            print("=" * 40)


def run():
    url_handler = InputHandler()
    csv_handler = CsvHandler(filename_suffix='test')
    print("Loading Browser......")
    firefox = BrowserHandler()
    process([url for url in url_handler], firefox, csv_handler, process_additional_pages=True)
    process(additional_urls, firefox, csv_handler, process_additional_pages=False)
    firefox.close()
    input(f"""Loading Completed! Open "{csv_handler.filename}" for data.\n
    Copy the file in different name if you want to rerun the program.\n\n
    Press Enter To Exit!""")


if __name__ == '__main__':
    print(""" Go through "README.md" for documentation. """)
    run()





