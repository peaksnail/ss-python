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
import conf


class Admin(object):

    def __init__(self):
        self.config = conf.Conf()
        self.usage_file = self.config.get('usage_file', utils.get_default_usage_file())
        self.usage = utils.load_file(self.usage_file)

    def show_all(self, unit = 'B'):
        for user in self.usage:
            print ('port %s, usage: %s' % (user, utils.byte_readable(int(self.usage[user]), unit)))

    def show_user(self, user, unit = 'B'):
        if(user in self.usage):
            print ('port %s, usage: %s' % (user, utils.byte_readable(int(self.usage[user]), unit)))
        else:
            print('not found port %s' % user)

    def clear_counter(self, user):
        iptable = iptables.Iptables([], self.usage_file)
        iptable.clean_counter(user)

    def shutdown_ss(self):
        pass

    def restart_ss(self):
        pass

    def reload_ss(self):
        pass

    def shutdown_self(self):
        pid = utils.get_pid(config.get('pid_file', utils.get_default_pid_file()))
        cmd = 'kill -9 ' + pid
        exec = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
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

    opts, args = getopt.getopt(sys.argv[1:], '-s:-h-v-q-r-c:', ['show=', 'help', 'version', 'quit', 'restore', 'clean='])
    for opt_name, opt_value in opts:
        #todo rich the help docs
        if opt_name in ('-h', '--help'):
            help = 'usage: \n\
-s --show       show all user or special usage \n\
-v --version    show current version \n\
-h --help       show help'
            print(help)
        elif opt_name in ('-v', '--version'):
            print('version: 0.0.1')
        elif opt_name in ('-s', '--show'):
            unit = 'B'
            if len(args)> 0:
                unit = args[0]
            if opt_value == 'all':
                admin.show_all(unit)
            else:
                admin.show_user(opt_value, unit)
        elif opt_name in ('-q', '--quit'):
            admin.shutdown_self()
        elif opt_name in ('-r', '--restore'):
            admin.restore()
        elif opt_name in ('-c', '--clean'):
            if opt_value == 'all':
                admin.clear_user()
            else:
                admin.clear_user(opt_value)




