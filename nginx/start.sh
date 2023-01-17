#!/bin/bash
systemctl start nginx
echo 'IP:' $(ip a s eth0 | grep  -w 'inet' | cut -d '/' -f 1 | tr 'inet' ' ')
tail -f /var/log/nginx/access.log /var/log/nginx/error.log 

