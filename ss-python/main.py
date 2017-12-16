#!/usr/bin/env python3

# -*- coding: utf-8 -*-

__author__ = 'psnail'

import utils
import iptables
import users
import os

PROJECT_DIR = utils.get_project_dir()

if __name__ == '__main__':


    utils.record_pid(utils.get_default_usage_file(), str(os.getpid()))

    conf = utils.load_file(PROJECT_DIR + '/docs/ss-python.conf')

    user = users.Users(conf['ss_conf'])
    iptable = iptables.Iptables(user.get())
    iptable.count_task_start()


