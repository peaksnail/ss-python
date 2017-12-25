#!/usr/bin/env bash

bin=$(dirname $0)

if [ `whoami` = 'root' ];then
    echo 'start ss-python now'
    python3 $bin/../ss-python/main.py &
else
    echo 'need root to work'
fi
