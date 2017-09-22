#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def get_key_info(response, *args, **kwargs):
    """回调函数
    """
    print 'Content Type: ', response.headers['Content-Type']

def download_images():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = "http://example.webscraping.com/places/static/images/flags/cn.png"
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True, hooks=dict(response=get_key_info))) as response:
        with open('cn.png', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)

if __name__ == '__main__':
    download_images()
