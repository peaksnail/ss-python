#!/usr/bin/env python3

#-*- conding: utf-8 -*-

__author__ = 'psnail'

import utils
import os

class Conf(object):

    '''
        global conf
    '''

    def __init__(self, file = None):
        self.project_dir = utils.get_project_dir()
        if file == None:
            self.conf_file = os.path.sep.join([self.project_dir, 'docs', 'ss-python.conf'])
        else:
            self.conf_file = file
        self._conf = utils.load_file(self.conf_file)

    def get(self, key, value = None):
        if key in self._conf.keys():
            return self._conf[key]
        elif value:
            return value
        else:
            return None

if __name__ == '__main__':
    conf = Conf()
    print(conf.get('key','value'))
    print(conf.get('ss_cmd','value'))
