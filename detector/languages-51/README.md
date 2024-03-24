Build the image
```bash
docker build -t lasylphide/languages-51 .
```

Run the image
```bash
docker run -p 8080:8080 lasylphide/languages-51
```

Curl the server
```bash 
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/languages-51:predict -d @./input.json
```