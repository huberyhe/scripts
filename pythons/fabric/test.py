#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run, env
import sys, os

env.use_ssh_config = True
env.hosts = ['gfw1']

def whoami():
	print sys.argv[0]
	print os.path.dirname(os.path.realpath(__file__))
	run('sudo whoami')
