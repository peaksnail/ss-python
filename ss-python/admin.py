#!/usr/bin/env python3

# -*- coding: utf-8 -*-

'''
    admin tool for manage ss
'''


__author__ = 'psnail'

import os
import subprocess
import sys
import getopt
import time
import utils
import iptables


class Admin(object):

    def __init__(self):
        self.usage = utils.load_file(utils.get_default_usage_file())

    def show_all(self, unit='B'):
        for user in self.usage:
            print ('port %s, usage: %s' % (user, utils.byte_readable(int(self.usage[user]), unit)))

    def show_user(self, user, unit='B'):
        if(user in self.usage):
            print ('port %s, usage: %s' % (user, utils.byte_readable(int(self.usage[user]), unit)))
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

    def shutdown_self(self):
        pid = utils.get_pid(utils.get_default_pid_file())
        cmd = 'kill -9 ' + pid
        exec = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = exec.stdout.readlines()
        print(output)

    def restore(self):
        '''
        restore all env
        '''
        self.shutdown_self()
        iptable = iptables.Iptables([])
        iptable.delete()


if __name__ == '__main__':

    admin = Admin()

    opts, args = getopt.getopt(sys.argv[1:], '-s:-h-v-q-r-c', ['show=', 'help', 'version', 'quit', 'restore', 'clean'])
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            print('''usage: \n-s --show    show all user or special usage\n-v --version     show current version\n-h --help    show help ''')
        elif opt_name in ('-v', '--version'):
            print('version: 0.0.1')
        elif opt_name in ('-s', '--show'):
            if opt_value == 'all':
                admin.show_all()
            else:
                admin.show_user(opt_value)
        elif opt_name in ('-q', '--quit'):
            admin.shutdown_self()
        elif opt_name in ('-r', '--restore'):
            admin.restore()




