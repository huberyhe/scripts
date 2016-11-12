#!/usr/bin/env bash

#selinux
semanage fcontext -a -t httpd_sys_script_exec_t '/var/wwws(/.*)?'
restorecon -Rv /var/wwws
semanage fcontext -l | grep '/var/wwws'

#firewall
firewall-cmd --zone=public --add-port=443/tcp --permanent
firewall-cmd --reload