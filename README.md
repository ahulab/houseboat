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