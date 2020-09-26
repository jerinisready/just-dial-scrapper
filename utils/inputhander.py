

class InputHandler(object):
    urls = []

    def __init__(self, filename='./data/input.txt'):
        with open(filename, 'r') as txt:
            print("Loading Urls...")
            self.urls = [url for url in txt.read().strip().split("\n") if url]      # eliminating blank lines.
            for _url in self.urls:
                print(f"\t{_url}")

    def __iter__(self):
        def generator(i=0):
            if i <= len(self.urls):
                yield self.urls[i]
                i += 1
        return generator()
