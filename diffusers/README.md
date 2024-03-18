Build the image
```bash
docker build -t lasylphide/diffusers .
```

Run the image
```bash
docker run -p 8080:8080 diffusers
```

Curl the server
```bash 
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/sdxl-turbo:predict -d @./input.json
```