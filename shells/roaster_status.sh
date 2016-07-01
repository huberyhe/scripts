#!/bin/bash
ssh root@128.199.58.37 'echo -e "\033[31m status of all servers: \033[0m" && roaster status serversall && echo -e "\033[31m status of services: \033[0m" &&  roaster status services & exit'
exit 3
