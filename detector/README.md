D:\GithubRepo\NGNE-images\detector>oha -H "Content-Type: application/json" -n 200 -c 5 -m POST  -D ./input.json  http://detectors.default.34.214.162.76.sslip.io
Summary:
  Success rate: 100.00%
  Total:        49.6034 secs
  Slowest:      1.8919 secs
  Fastest:      0.4987 secs
  Average:      1.2318 secs
  Requests/sec: 4.0320

  Total data:   11.33 KiB
  Size/request: 58
  Size/sec:     233 B

Response time histogram:
  0.499 [1]  |
  0.638 [2]  |■
  0.777 [5]  |■■■
  0.917 [42] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.056 [17] |■■■■■■■■■■■
  1.195 [11] |■■■■■■■
  1.335 [27] |■■■■■■■■■■■■■■■■■■
  1.474 [47] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.613 [35] |■■■■■■■■■■■■■■■■■■■■■■■
  1.753 [8]  |■■■■■
  1.892 [5]  |■■■

Response time distribution:
  10.00% in 0.8013 secs
  25.00% in 0.9926 secs
  50.00% in 1.3041 secs
  75.00% in 1.4105 secs
  90.00% in 1.5983 secs
  95.00% in 1.6995 secs
  99.00% in 1.7956 secs
  99.90% in 1.8919 secs
  99.99% in 1.8919 secs


Details (average, fastest, slowest):
  DNS+dialup:   0.2040 secs, 0.1943 secs, 0.2148 secs
  DNS-lookup:   0.0001 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 200 responses
