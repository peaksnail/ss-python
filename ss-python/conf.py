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
        self.project_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
        if file == None:
            self.conf_file = os.path.sep.join([self.project_dir, 'docs', 'ss-python.conf'])
        else:
            self.conf_file = file
        self._conf = utils.load_file(self.conf_file)

    def get(self, value):
        pass

if __name__ == '__main__':
    conf = Conf()
