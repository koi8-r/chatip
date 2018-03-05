# coding=utf-8
from requests import Session as UA
from fnmatch import fnmatch
import logging
import sys


__all__ = ['run']


def run():
    if 2 != len(sys.argv):
        print('Usage: {} <login>'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(255)

    logging.basicConfig(level=logging.ERROR)
    logging.captureWarnings(True)
    logging.getLogger('urllib3').level = logging.ERROR

    ua = UA()
    resp = ua.request(method='GET',
                      url='https://chat.murmangaz.lan:9091/plugins/restapi/v1/sessions',
                      headers={
                          'Accept': 'application/json',
                          'Authorization': '<SECRET_KEY>'},
                      verify=False)

    for o in filter(lambda _:
                    fnmatch(_.get('username', '').lower(), sys.argv[1]),
                    resp.json()['session']):
        print('"{username}":\n'
              '  ip: {hostAddress}\n'
              '  host: {hostName}\n'
              '  status: {presenceStatus}\n'
              .format(**o))
