#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' iptables tools '

__author__ = 'psnail'

import subprocess
import threading
import time
import utils
import os

class Iptables(object):

    def __init__(self, ports = [], file = utils.get_default_usage_file()):
        # (self, conf) read port from conf

        self.SSINPUT = 'ssinput'
        self.SSOUTPUT = 'ssoutput'
        self._usage_file = file

        if os.path.isfile(file):
            self._usage = utils.load_file(file)
        else:
            self._usage = {}
            self._rule_init()
            self._add_all_rules(ports)

    def add_rule(self, port):
        port = str(port)
        cmds = [
                'iptables -A ' + self.SSINPUT + ' -p tcp --dport ' + port + ' -j ACCEPT',
                'iptables -A ' + self.SSINPUT + ' -p udp --dport ' + port + ' -j ACCEPT',
                'iptables -A ' + self.SSOUTPUT + ' -p tcp --sport ' + port + ' -j ACCEPT',
                'iptables -A ' + self.SSOUTPUT + ' -p udp --sport ' + port + ' -j ACCEPT'
                ]
        for cmd in cmds:
            exec = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = exec.stdout.readlines()
            if len(output) == 0:
                print('exec success, cmd: ' + cmd)
            else:
                print('exec failed, cmd: ' + cmd + ', ' + str(output))

    def _rule_init(self):
        self._delete_all_rules();
        cmds = [
                'iptables -N ' + self.SSINPUT,
                'iptables -A INPUT -j' + self.SSINPUT,
                'iptables -N ' + self.SSOUTPUT,
                'iptables -A OUTPUT -j' + self.SSOUTPUT
                ]
        for cmd in cmds:
            subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

    
    def _delete_all_rules(self):
        cmds = [
                'iptables -F ' + self.SSINPUT,
                'iptables -D -j ' + self.SSINPUT,
                'iptables -X ' + self.SSINPUT,
                'iptables -F ' + self.SSOUTPUT,
                'iptables -D -j ' + self.SSOUTPUT,
                'iptables -X ' + self.SSOUTPUT,
                ]
        for cmd in cmds:
            subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)


    def _add_all_rules(self, ports):
        for port in ports:
            self.add_rule(port);

    def _count(self):
        'count the flow of port'

        cmd = 'iptables -nvx -L ' + self.SSINPUT + ' && iptables -nvx -L ' + self.SSOUTPUT
        exec = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = exec.stdout.readlines()
        for line in output:
            line = line.decode('ascii').split(' ')
            if len(line) > 5 and len(line[-1]) > 1:
                # delete all space after split
                line = [item for item in filter(None, line)]
                port = line[-1].split(':')[1].strip('\n')
                self._usage[port] = line[1]

    def _task(self, retention, file):
        while True:
            self._count()
            self._storage(file)
            time.sleep(retention)

    def _storage(self, file):
        with open(file, 'w') as f:
            for item in self._usage.items():
                f.write(item[0] + ': ' + str(item[1]) + '\n')


    def count_task_start(self, retention = 5):
        #new thread to count and storage
        t = threading.Thread(target = self._task, args = ( retention, self._usage_file))
        t.start()
        t.join()

    def delete(self):
        self._delete_all_rules()
        os.remove(self._usage_file)


if __name__ == '__main__':
    iptables = Iptables([13152])
