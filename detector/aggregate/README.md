Build the image
```bash
docker build -t lasylphide/aggregate:v1 .
```

Run the image
```bash
docker run -p 8080:8080 lasylphide/aggregate:v1
```

Curl the server
```bash 
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/aggregate:predict -d @./input.json
```