from __future__ import print_function

import requests
import json
import time

from st2common.runners.base_action import Action

__all__ = [
    'ScanURL'
]

class ScanURL(Action):
    def run(self, url, public):
        # https://urlscan.io/about-api/
        API_URL = 'https://urlscan.io/api/v1/scan/'
        API_KEY = self.config.get('apikey', None)
        VERIFY_SSL = self.config.get('verify', None)
        RATE_LIMIT = 2
        MAX_RETRY = 5

        data = json.dumps({'url': url, 'public': public})
        headers = {'Content-Type': 'application/json', 'API-Key': API_KEY}

        # Submit the site for scanning and get a link to the results
        submission = requests.post(API_URL, data=data, headers=headers, verify=VERIFY_SSL)
        result_url = submission.json()['api']

        # Poll the results api endpoint until there are results available to retrieve
        count = 0

        while True:
            result = requests.get(result_url, headers=headers)

            # The api will return 404 while the site is being processed
            if result.status_code == 404 and count < MAX_RETRY:
                time.sleep(RATE_LIMIT)
                continue

            break

        return result.json()['task']
