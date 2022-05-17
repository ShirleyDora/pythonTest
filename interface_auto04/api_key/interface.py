# Author:Shirley
# Date:2022-05-16
import json
import jsonpath as jsonpath
import requests as requests


class Interface:
    # get
    def do_get(self, url, params=None, headers=None, **kwargs):
        return requests.get(url=url, params=params, headers=headers, **kwargs)

    # post
    def do_post(self, url, params=None, headers=None, **kwargs):
        return requests.post(url=url, params=params, headers=headers, **kwargs)

    # get_text
    def get_text(self, txt, key):
        try:
            txt = json.dumps(txt)
            value = jsonpath.jsonpath(txt, '$..{}'.format(key))
            if value:
                if len(value) == 1:
                    return value[0]
            return value
        except:
            return None
