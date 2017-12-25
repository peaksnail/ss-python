#!/usr/bin/env python3

# -*- coding: utf-8 -*-

__author__ = 'psnail'

import os

def load_file(file):
    content = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            if line == '\n':
                continue
            if line.startswith('#'):
                continue
            line = line.split(':')
            if line[1].strip() == '':
                content[line[0].strip()] = None
            else:
                content[line[0].strip()] = line[1].strip()

    return content


def clear_file(file):
    with open(file, 'w') as f:
        pass

def get_project_dir():
    return os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

def get_project_docs_dir():
    return get_project_dir() + os.path.sep + 'docs'

def get_default_usage_file():
    return get_project_dir() + os.path.sep + 'docs' + os.path.sep + 'usage.txt'

def get_default_pid_file():
    return get_project_dir() + os.path.sep + 'docs' + os.path.sep + 'pid'


def record_pid(file, pid):
    with open(file, 'w') as f:
        f.write(pid)

def get_pid(file):
    with open(file) as f:
        return f.read()

def byte_readable(data, unit='B'):
    '''
    make byte_readable
    data original is bytes
    '''
    if unit == 'B':
        return data
    elif unit == 'K':
        return data/1024
    elif unit == 'M':
        return data/1024/1024
    elif unit == 'G':
        return data/1024/1024/1024
    
