#!/usr/bin/env python3

# -*- coding: utf-8 -*-

'''
    admin tool for manage ss
'''


__author__ = 'psnail'

import os
import sys
import getopt
import time
import utils


class Admin(object):

    def __init__(self):
        self.usage = utils.load_file(utils.get_default_usage_file())

    def show_all(self):
        for user in self.usage:
            print ('port %s, usage: %s' % (user, self.usage[user]))

    def show_user(self, user):
        if(user in self.usage):
            print ('port %s, usage: %s' % (user, self.usage[user]))
        else:
            print('not found port %s' % user)

    def clear_all(self):
        utils.clear_file(utils.get_default_usage_file())

    def clear_user(self, user):
        while True:
            mtime = os.stat(utils.get_default_usage_file()).st_mtime
            ctime = time.time()
            if ctime - mtime <= 3:
                selff.usage[user] = 0

    def shutdown_ss(self):
        pass

    def restart_ss(self):
        pass

    def reload_ss(self):
        pass


if __name__ == '__main__':

    admin = Admin()

    opts, args = getopt.getopt(sys.argv[1:], '-s:-h-v', ['show=', 'help', 'version'])
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            print('''usage: \n-s --show    show all user or special usage\n-v --version     show current version\n-h --help    show help ''')
        if opt_name in ('-v', '--version'):
            print('version: 0.0.1')
        if opt_name in ('-s', '--show'):
            if opt_value == 'all':
                admin.show_all()
            else:
                admin.show_user(opt_value)
