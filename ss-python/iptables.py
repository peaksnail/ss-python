#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' iptables tools '

__author__ = 'zengshaojian'

import subprocess

class Iptables(object):

    def __init__(self, ports = []):
        self.SSINPUT = 'ssinput'
        self.SSOUTPUT = 'ssoutput'
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

    def count(self):
        'count the flow of port'

        usage = {}
        cmd = 'iptables -nvx -L ' + self.SSINPUT + ' && iptables -nvx -L ' + self.SSOUTPUT
        exec = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = exec.stdout.readlines()
        for line in output:
            line = line.decode('ascii').split(' ')
            if len(line) > 5 and len(line[-1]) > 1:
                port = line[-1].split(':')[1]
                if port in usage:
                    usage[port] = usage[port] + int(line[8])
                else:
                    usage[port] = int(line[8])
        return usage


if __name__ == '__main__':
    iptables = Iptables([13152])
