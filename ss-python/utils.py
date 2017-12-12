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
            content[line[0].strip()] = line[1].strip()

    return content


def clear_file(file):
    with open(file, 'w') as f:
        pass

def get_project_dir():
    cwd = os.getcwd()
    sep = os.path.sep
    return cwd[0: cwd.rfind(sep)]

def get_project_docs_dir():
    return get_project_dir() + os.path.sep + 'docs'

def get_default_usage_file():
    return get_project_dir() + os.path.sep + 'docs' + os.path.sep + 'usage.txt'

def get_default_pid_file():
    return get_project_dir() + os.path.sep + 'docs' + os.path.sep + 'pid'


def record_pid(file, pid):
    with openen(file, 'w') as f:
        f.write(pid)
