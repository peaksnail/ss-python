#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' user info'

__author__ = 'zengshaojian'


import json

class Users(object):

    def __init__(self, file):
        self._user_list = []
        self._user_usage = {}
        self._conf = file

    def _load(self):
        with open(self._conf, 'r') as json_content:
            conf = json.load(json_content)

        if 'server_port' in conf:
            self._user_list.append(conf['server_port'])
        elif 'port_password' in conf:
            for port in conf['port_password'].keys():
                self._user_list.append(int(port))
        else:
            print('file is unvalid, read user info failed!')

    def get(self):
        return self._user_list

    def recover(self):
        'read user info when restart'
        pass

if __name__ == '__main__':

    user = Users()
    user.load('../docs/json.json')
    print(user._user_list)
