# kcollect
Log collector "Kristina collects" gives you ability to collect all your log files in one place.  
It's like Graylog, but works locally.  

Instruction:
It's easy to use. Just add your log files in config.yml file and start/restart service. Program will automatically implement at the start of the message a nickname of file which you set up in config, file's location and timestamp

How to run:
1. sudo touch /etc/systemd/system/kcollect.service
2. Then fill this file with this config (open in raw format):

> [Unit]  
> Description=KCollect Log Collector Daemon  
> After=network.target
>   
> [Service]  
> Type=simple  
> User=root  
> WorkingDirectory=/opt/kcollect  
>   
> ExecStartPre=/bin/mkdir -p /opt/kcollect  
> ExecStartPre=/bin/mkdir -p /opt/kcollect/offsets  
> ExecStartPre=/bin/touch /var/log/kcollect/collector.log  
> ExecStartPre=/bin/chown -R root:root /var/log/kcollect /opt/kcollect  
> ExecStartPre=/bin/chmod -R 755 /var/log/kcollect /opt/kcollect  
>   
> ExecStart=/usr/bin/python3 /opt/kcollect/main.py  
>   
> Restart=on-failure  
> RestartSec=5  
>   
> StandardOutput=append:/var/log/kcollect/collector.log  
> StandardError=append:/var/log/kcollect/collector.log  
>   
> [Install]
> WantedBy=multi-user.target

3. Then reread all unit files, update internal configuration, enable service and start service:
    
> sudo systemctl daemon-reexec

> sudo systemctl daemon-reload

> sudo systemctl enable kcollect.service

> sudo systemctl start kcollect.service
