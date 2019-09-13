#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import choice
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
import os

import pprint as pp
import json
import traceback

_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
]


class PriceFileScraper:
    def __init__(self):
        pass

    @staticmethod
    def extract_rows(html):
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("body")
        tables = body.findChildren("table")
        my_table = tables[0]
        rows = my_table.findChildren(["tr"])
        return rows

    def insta_prices(self):
        results = []
        try:
            url = "index.html"
            page = open(url)
            rows = self.extract_rows(page.read())

            with open("account_sell_data.csv", "w") as f:
                for row in rows:
                    try:
                        cells = row.findChildren("td")
                        line = ", ".join(
                            [
                                cells[0].a.text.strip(),
                                cells[1].text.replace(",", ""),
                                cells[2].text.replace(",", ""),
                                cells[3].a.text.strip(),
                                cells[4].text,
                            ]
                        )
                        f.write(line + "\n")
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


def main():
    obj = PriceFileScraper()
    obj.insta_prices()


if __name__ == "__main__":
    main()
