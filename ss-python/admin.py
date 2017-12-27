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

    def clean_counter(self, user):
        iptable = iptables.Iptables([], self.usage_file)
        iptable.clean_counter(user)

    def shutdown_ss(self):
        #todo
        ss_cmd = self.config.get('ss_cmd', 'ssserver')
        get_ss_argv_cmd = 'ps aux | grep ' + ss_cmd + 'grep -v ' + ss_cmd + ' | awk'
        ss_argv = subprocess.Popen(get_ss_argv_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT).stdout.readlines()

    def start_ss(self):
        pass

    def reload_ss(self):
        pass

    def shutdown_self(self):
        pid_file = self.config.get('pid_file', utils.get_default_pid_file())
        if not os.path.exists(pid_file):
            print('ss-python has not started')
            return
        pid = utils.get_pid(pid_file)
        cmd = 'kill -9 ' + pid
        subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        #rm pid file
        os.remove(pid_file)

    def start_self(self):
        pid_file = self.config.get('pid_file', utils.get_default_pid_file())
        if os.path.exists(pid_file):
            print('ss-python has started...')
        else:
            project_dir = utils.get_project_dir()
            sh = os.path.sep.join([project_dir, 'bin', 'ss-python.sh'])
            cmd = 'sh ' + sh
            exe = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
            print(exe.stdout.readlines())

    def restore(self):
        '''
        restore all env
        '''
        self.shutdown_self()
        iptable = iptables.Iptables([])
        iptable.delete()


if __name__ == '__main__':

    admin = Admin()

    opts, args = getopt.getopt(sys.argv[1:], '-s-g:-h-v-q-r-c:', ['start', 'get=', 'help', 'version', 'quit', 'restore', 'clean='])
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
        elif opt_name in ('-g', '--get'):
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
                admin.clean_counter()
            else:
                admin.clean_counter(opt_value)
        elif opt_name in ('-s', '--start'):
            admin.start_self()




