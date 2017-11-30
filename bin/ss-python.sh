#!/usr/bin/env bash

if [ `whoami` = 'root' ];then
    echo 'start ss-python now'
    python3 ../ss-python/main.py &
else
    echo 'need root to work'
fi
