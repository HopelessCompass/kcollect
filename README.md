# kcollect
Log collector "Kcollect" gives you ability to collect all your log files and directories in one place

How to run:
    1. sudo touch /etc/systemd/system/logcollector.service
    2. Then fill this file with this config:

[Unit]
Description=Custom Log Collector Daemon
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/youruser/log_collector/main.py
WorkingDirectory=/home/youruser/log_collector
StandardOutput=file:/home/youruser/log_collector/logcollector_stdout.log
StandardError=file:/home/youruser/log_collector/logcollector_stderr.log
Restart=on-failure

[Install]
WantedBy=multi-user.target

    3. Then reread all unit files, update internal configuration, enable service and start service:
    
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable logcollector.service
sudo systemctl start logcollector.service