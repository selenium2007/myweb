#!/bin/bash
ps -ef|grep runserver|grep -v grep|awk '{print $2}'|xargs kill -9
cd /home/ubuntu/buckwheat/buckwheat;../manage.py runserver 0.0.0.0:8080
ps -efl|grep runserver|grep -v grep
