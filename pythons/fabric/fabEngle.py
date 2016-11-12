#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.colors import *
import sys, os, string

env.use_ssh_config = True
env.roledefs = {
	'mgservers': ['engle_m1'],
	'cwservers': ['engle_cw1', 'engle_cw2'],
	'rservers': ['engle_r1', 'engle_r2', 'engle_r3', 'engle_r4', 'engle_r5', 'engle_r6', 'engle_r7', 'engle_r8']
}

@task
@roles('cwservers')
def restart_cwforwarder():
	run("sudo systemctl restart cwforwarder.service")

@task
@roles('cwservers')
def restart_arjlog():
	run("sudo systemctl restart arjlog.service")

@task
@roles('rservers')
def restart_services():
	run("sudo chroot /mnt/test/ ikstcp_restart.sh")