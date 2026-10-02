#!/usr/bin/env python3
"""Fetch one public ZUKU record with no credentials or state mutation."""
import argparse
import json
import re
import urllib.request

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('content_id')
    args = parser.parse_args()
    if not re.fullmatch(r'cnt_[A-Za-z0-9_-]{1,100}', args.content_id):
        parser.error('expected a cnt_ content ID')
    request = urllib.request.Request(
        'https://zuzunza.com/api/v1/contents/' + args.content_id,
        headers={'Accept': 'application/json', 'User-Agent': 'ZUKU-public-api-skill/1.0'},
    )
    with urllib.request.urlopen(request, timeout=12) as response:
        raw = response.read(2 * 1024 * 1024 + 1)
        if len(raw) > 2 * 1024 * 1024:
            raise ValueError('public response exceeded 2 MiB')
        result = json.loads(raw)
        if result.get('success') is not True:
            raise ValueError('API did not return a successful envelope')
        content = result['data']['content']
        if content.get('id') != args.content_id:
            raise ValueError('API content ID did not match request')
        print(json.dumps({'status': response.status, 'id': content['id'],
                          'category': content.get('category'), 'type': content.get('type'),
                          'title': content.get('title')}, ensure_ascii=False))

if __name__ == '__main__':
    main()
