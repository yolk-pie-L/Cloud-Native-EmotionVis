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
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/emotions:predict -d @./input.json
```