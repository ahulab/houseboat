## Description
Some services to run on a cron and track network
perf over time

## Deployment
```
rsync --filter=':- .gitignore' $PWD/ some-host:/opt/houseboat/ -r --delete

# execute the rest of this on the target host
ssh some-host
cd /opt/houseboat
docker-compose -f docker/docker-compose.yml build collector 
docker-compse up -d
```

Create a script to wrap the collector runs with some logs
```
#!/usr/bin/env bash

echo "$(date): Running collector" >> ./collector.log
/usr/local/bin/docker-compose -f /opt/houseboat/docker/docker-compose.yml up collector
echo "$(date): Done running collector" >> ./collector.log
```

```
# create a cronjob to run the collector at some interval
*/7 * * * * /root/run-collector.sh
```

## Appendix
Example speedtest cli out json:
```json
{
    "type":"result",
    "timestamp":"2020-09-28T01:17:20Z",
    "ping": {
        "jitter": 5.5609999999999999,
        "latency":18.079999999999998
    },
    "download": {
        "bandwidth":5429538,
        "bytes":64531544,
        "elapsed":13517
    },
    "upload": {
        "bandwidth": 625648,
        "bytes": 6727972,
        "elapsed": 12316
    },
    "packetLoss":0,
    "isp":"Comcast Cable",
    "interface": {
        "internalIp": "172.17.0.2",
        "name":"eth0",
        "macAddr":"02:42:AC:11:00:02",
        "isVpn":false,
        "externalIp":"71.232.61.49"
    },
    "server":{
        "id": 35437,
        "name": "Acella Construction",
        "location": "Pembroke, MA",
        "country": "United States",
        "host":"sp1.acel.la",
        "port":8080,
        "ip":"96.230.79.118"
    },
    "result": {
        "id":"c9e5fe54-08d1-4ae4-b79a-e7d07434589d",
        "url":"https://www.speedtest.net/result/c/c9e5fe54-08d1-4ae4-b79a-e7d07434589d"
    }
}
```
