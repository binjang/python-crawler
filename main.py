import requests
import re

class WebPost:
    def __init__(self, url):
        self.url = url
        self.author = ""
        self.text = ""
        self.date = ""
        self.site = ""
        self.queries = ""

    def get_items(self):
        html = requests.get(self.url)
        pass

