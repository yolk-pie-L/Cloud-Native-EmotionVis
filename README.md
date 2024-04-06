# NGNE-images

```shell
hey_windows_amd64.exe -H "Content-Type: application/json" -z 60s -c 10 -m POST -t 0 -D ./input.json  http://emo-vis.default.44.242.13.48.sslip.io
``` 

```shell
oha -H "Content-Type: application/json" -n 3 -c 1 -m POST  -D ./input.json  http://emo-vis.default.44.242.13.48.sslip.io
```

```shell
kubectl delete isvc --all
``` 

D:\GithubRepo\NGNE-images>oha -H "Content-Type: application/json" -n 200 -c 5 -m POST  -D ./input.json  http://emo-vis.default.34.214.162.76.sslip.io
Summary:
  Success rate: 99.00%
  Total:        675.8155 secs
  Slowest:      134.3369 secs
  Fastest:      1.5287 secs
  Average:      15.9404 secs
  Requests/sec: 0.2959

  Total data:   102.91 MiB
  Size/request: 53
  Size/sec:     155.93 KiB

Response time histogram:
    1.529 [1]   |
   14.809 [122] |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
   28.090 [67]  |■■■■■■■■■■■■■■■■■
   41.371 [5]   |■
   54.652 [0]   |
   67.933 [0]   |
   81.214 [0]   |
   94.494 [1]   |
  107.775 [1]   |
  121.056 [0]   |
  134.337 [1]   |

Response time distribution:
  10.00% in 9.6408 secs
  25.00% in 11.9302 secs
  50.00% in 13.5109 secs
  75.00% in 16.1896 secs
  90.00% in 22.9395 secs
  95.00% in 24.9108 secs
  99.00% in 98.6602 secs
  99.90% in 134.3369 secs
  99.99% in 134.3369 secs


Details (average, fastest, slowest):
  DNS+dialup:   0.2092 secs, 0.1992 secs, 0.2265 secs
  DNS-lookup:   0.0001 secs, 0.0000 secs, 0.0002 secs

Status code distribution:
  [200] 198 responses

Error distribution:
  [2] error reading a body from connection