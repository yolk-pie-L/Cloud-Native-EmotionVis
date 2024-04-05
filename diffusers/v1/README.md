Build the image
```bash
docker build -t lasylphide/diffusers:v1 .
```

Run the image
```bash
docker run -p 8080:8080 lasylphide/diffusers:v1
```

Curl the server
```bash 
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/diffusers-v1:predict -d @./input.json
```