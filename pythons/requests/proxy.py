#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}

url = 'https://www.facebook.com/'

response = requests.get(url, proxies=proxies, timeout=10)

print response.text
