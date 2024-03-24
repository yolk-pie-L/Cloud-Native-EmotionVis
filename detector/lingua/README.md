Build the image
```bash
docker build -t lasylphide/lingua .
```

Run the image
```bash
docker run -p 8080:8080 lasylphide/lingua
```

Curl the server
```bash 
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/lingua:predict -d @./input.json
```