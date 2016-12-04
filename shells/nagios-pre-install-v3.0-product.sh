#!/bin/bash
# Date : 2015年10月26日16:22:32
# Author : houqian
# Contact : houqian@oneapm.com
# Company : www.onealert.com
# OneAlert pre install script : nagios

set -e
#agent installing log file 
logfile="onealert-agent-install.log"
#current system timestamp for log
SYSTEM_TIME=`date '+%Y-%m-%d %T'`
# color
yellow='\e[0;33m'
green='\e[0;32m' 
endColor='\e[0m'

#server url
YUM_URL="http://yum.110monitor.com"
INSTALL_PROCESS_URL="http://c.110monitor.com/alert/api/escalation/agentInstall/$NAGIOS_APPKEY"
MENU_CEP_URL="http://api.110monitor.com/alert/api/event"
HB_URL="http://hb.110monitor.com/alert/api/heartbeat/"
MENU_ALERT_URL="http://api.110monitor.com/alert"

# detect whether the current user is root.
# Root user detection
if [ $(echo "$UID") = "0" ]; then
    sudo_cmd=''
else
    sudo_cmd='sudo'
fi

# it is only support redhat&centos now,other will be comming soon.. :P
OS=RedHat

#update status :creating
curl -d "status=creating" $INSTALL_PROCESS_URL
echo -e "\n"
if [ -n "$NAGIOS_APPKEY" ]; then
    app_key=$NAGIOS_APPKEY
else
    echo -e "${yellow} $SYSTEM_TIME - Missing NAGIOS_APPKEY end of the install command.${endColor}" >> $logfile
    exit 3;
fi

# depending on the operating system version installed agent.
if [ $OS = "RedHat" ]; then
    echo -e "\033[34m\n* Installing YUM sources for OneAlert\n\033[0m"
    #remove old repo for onealert
    $sudo_cmd rm -fr /etc/yum.repos.d/onealert-agent.repo
    $sudo_cmd sh -c "echo -e '[onealert-agent]\nname=OneAlert, Inc.\nbaseurl=$YUM_URL/centos6/x86_64/\nenabled=1\ngpgcheck=0\npriority=1\n' > /etc/yum.repos.d/onealert-agent.repo"

    echo -e "\033[34m* Installing the OneAlert Agent package\n\033[0m\n"
    #update status
    curl -d "status=pedding" $INSTALL_PROCESS_URL
    $sudo_cmd yum -y --disablerepo='*' --enablerepo='onealert-agent' install onealert-nagios-agent
    #update status
    curl -d "status=installed" $INSTALL_PROCESS_URL
    echo -e "\n"
fi

echo -e "${green}Yum install OneAlert Agent Successful!${endColor}"
echo -e "\n"

echo -e "Start to set configuration..."
# Set the configuration
$sudo_cmd chmod -R +x /usr/local/nagios/libexec/alert-agent
$sudo_cmd chmod -R +x /usr/local/nagios/libexec/nagios
    
echo -e "\033[34m\n* Adding your license key to the Agent configuration: /usr/local/nagios/etc/objects/110monitor.cfg\n\033[0m\n"
# backup copies
$sudo_cmd cp /usr/local/nagios/etc/objects/110monitor.cfg /usr/local/nagios/etc/objects/110monitor.cfg.example
#replace appkey at 110monitor.cfg and his backup file
$sudo_cmd sed -i "s%your-app-key%$NAGIOS_APPKEY%g" /usr/local/nagios/etc/objects/110monitor.cfg.example
$sudo_cmd sed -i "s%your-app-key%$NAGIOS_APPKEY%g" /usr/local/nagios/etc/objects/110monitor.cfg
#value for runtime.properties
$sudo_cmd sed -i "s%your_app_key%$NAGIOS_APPKEY%g" /usr/local/nagios/libexec/alert-agent/conf/runtime.properties
$sudo_cmd sed -i "s%alert_url%$MENU_CEP_URL%g" /usr/local/nagios/libexec/alert-agent/conf/runtime.properties
$sudo_cmd echo "menu.alert.url=$MENU_ALERT_URL" >> /usr/local/nagios/libexec/alert-agent/conf/runtime.properties
$sudo_cmd sed -i "s%hb_url%$HB_URL%g" /usr/local/nagios/libexec/alert-agent/conf/runtime.properties
#add 110monitor into nagios contacts.cfg
$sudo_cmd sed -i 's%members                 nagiosadmin%&,110monitor%' /usr/local/nagios/etc/objects/contacts.cfg

# Reference 110monitor.cfg in the nagios.cfg
$sudo_cmd sh -c "echo 'cfg_file=/usr/local/nagios/etc/objects/110monitor.cfg' >> /usr/local/nagios/etc/nagios.cfg"
echo -e "End to set configuration..."

# Start heartbeat daemon
$sudo_cmd chmod +x /usr/local/nagios/libexec/alert-agent/bin/heartbeat-daemon.sh
$sudo_cmd cd /usr/local/nagios/libexec/alert-agent/bin
sudo sh /usr/local/nagios/libexec/alert-agent/bin/heartbeat-daemon.sh start
#update status
echo -e "\n"
curl -d "status=success" $INSTALL_PROCESS_URL
echo -e "${green}\nCongratulations!\n :P${endColor}"
