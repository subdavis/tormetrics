# Tor metrics

Run the following to get the files.

```
wget https://ip-ranges.amazonaws.com/ip-ranges.json
wget https://www.dan.me.uk/torlist
```

The run `main.py`

This will tell you how many current tor routers are currently hosted on AWS.  At last run the results were:

```
Finding TOR nodes in the AWS network...  IPv4 only!
Loaded 1175 network ranges from AWS.
Loaded 6137 addresses from TOR service.
Found 43 matches out of 6137 total addresses.
13.124.107.51
13.229.211.201
13.231.107.46
18.221.42.20
18.221.54.60
34.214.31.61
34.214.172.23
34.216.205.9
34.217.103.233
34.218.69.53
34.226.150.252
34.228.82.98
34.241.138.212
35.157.59.169
35.163.47.243
35.168.202.103
35.170.77.224
52.6.9.146
52.15.62.13
52.38.74.143
52.39.6.26
52.47.111.91
52.47.141.25
52.50.118.8
52.56.47.154
52.60.215.15
52.63.134.148
52.66.124.255
52.67.141.3
52.90.84.21
52.90.187.233
52.209.220.12
54.80.24.96
54.86.232.140
54.88.165.229
54.94.85.201
54.153.249.26
54.179.98.204
54.187.239.16
54.191.85.166
54.233.155.67
54.241.9.145
107.20.75.202
```