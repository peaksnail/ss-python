#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import utils
import iptables
import users

PROJECT_DIR = utils.get_project_dir()

if __name__ == '__main__':

    conf = utils.load_file(PROJECT_DIR + '/docs/ss-python.conf')

    user = users.Users(conf['ss-conf'])
    iptable = iptables.Iptables(user.get())
    iptable.count_task_start('storage file')


