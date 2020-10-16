
## Serial

```bash
$ bombardier http://localhost:1337 
Bombarding http://localhost:1337 for 10s using 125 connection(s)
[=================================================================================================================] 10s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec      3327.05    1096.20    6354.03
  Latency       43.36ms   498.66ms     17.23s
  HTTP codes:
    1xx - 0, 2xx - 33403, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   254.09KB/s

```

```bash
$ python server.py localhost 1337 serial
```