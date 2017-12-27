#!/usr/bin/env python3

# -*- coding: utf-8 -*-

__author__ = 'psnail'

import conf
import utils
import iptables
import users
import os


if __name__ == '__main__':

    config = conf.Conf()

    utils.record_pid(config.get('pid_file', utils.get_default_pid_file()), str(os.getpid()))

    user = users.Users(config.get('ss_conf', '/etc/shadowsocks.json'))
    iptable = iptables.Iptables(user.get(), config.get('usage_file', utils.get_default_usage_file()))
    iptable.count_task_start(int(config.get('flush_retention', 5)))


