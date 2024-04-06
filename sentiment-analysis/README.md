Build the image
```bash
docker build -t lasylphide/sentiment-analysis .
```

Run the image
```bash
docker run -p 8080:8080 lasylphide/sentiment-analysis
```

Curl the server
```bash 
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/sentiment-analysis:predict -d @./input.json
```

D:\GithubRepo\NGNE-images\sentiment-analysis>oha -H "Content-Type: application/json" -n 200 -c 5 -m POST  -D ./input.json  http://sentiment-analysis.default.44.242.13.48.sslip.io/v1/models/sentiment-analysis:predict
Summary:
  Success rate: 100.00%
  Total:        42.3839 secs
  Slowest:      1.7046 secs
  Fastest:      0.4973 secs
  Average:      1.0516 secs
  Requests/sec: 4.7188

  Total data:   4.88 KiB
  Size/request: 25
  Size/sec:     117 B

Response time histogram:
  0.497 [1]  |
  0.618 [2]  |■
  0.739 [16] |■■■■■■■■■■■■■
  0.860 [37] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.980 [28] |■■■■■■■■■■■■■■■■■■■■■■■■
  1.101 [34] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.222 [33] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.342 [19] |■■■■■■■■■■■■■■■■
  1.463 [19] |■■■■■■■■■■■■■■■■
  1.584 [6]  |■■■■■
  1.705 [5]  |■■■■

Response time distribution:
  10.00% in 0.7907 secs
  25.00% in 0.8035 secs
  50.00% in 1.0056 secs
  75.00% in 1.2083 secs
  90.00% in 1.3991 secs
  95.00% in 1.4970 secs
  99.00% in 1.6920 secs
  99.90% in 1.7046 secs
  99.99% in 1.7046 secs


Details (average, fastest, slowest):
  DNS+dialup:   0.2032 secs, 0.1967 secs, 0.2213 secs
  DNS-lookup:   0.0001 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 200 responses