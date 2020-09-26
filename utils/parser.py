

cls_to_num_map = {
    'icon-ba': '-',     # <-- ab
    'icon-dc': '+',     # <-- cd
    'icon-fe': '(',     # <-- ef
    'icon-hg': ')',     # <-- gh
    'icon-ji': '9',     # <-- ij
    'icon-lk': '8',     # <-- kl
    'icon-nm': '7',     # <-- mn
    'icon-po': '6',     # <-- op
    'icon-rq': '5',     # <-- qr
    'icon-ts': '4',     # <-- st
    'icon-vu': '3',     # <-- uv
    'icon-wx': '2',     # <-- wx
    'icon-yz': '1',     # <-- yz
    'icon-acb': '0',    # <-- acb
}


class Parser(object):

    def __init__(self, soup):
        self.soup = soup

    @property
    def summery_node(self):
        return self.soup.find("span", {"class": "jcn"}).find('a')

    @property
    def summery(self):
        return self.summery_node.attrs['title']

    @property
    def link(self):
        return self.summery_node.attrs['href']

    @property
    def address(self):
        return (self.soup.find("span", {"class": "cont_fl_addr"})).text[:-6].strip()

    @property
    def name(self):
        return self.soup.find("span", {"class": "lng_cont_name"}).text

    @property
    def verification(self):
        return "Verified" if len(self.soup.findAll("span", {"class", "jd_verified"})) > 0 else ""

    @property
    def contact(self):
        class_names = [item['class'][1] for item in
                       self.soup.select('.contact-info  span[class*="icon"]')]
        telephoneNumber = ''.join([cls_to_num_map[class_name] for class_name in class_names])
        return str(telephoneNumber)
