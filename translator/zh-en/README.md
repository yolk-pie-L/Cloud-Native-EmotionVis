Build the image
```bash
docker build -t lasylphide/zh-en .
```

Run the image
```bash
docker run -p 8080:8080 lasylphide/zh-en
```

Curl the server
```bash 
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/zh-en:predict -d @./input.json
```