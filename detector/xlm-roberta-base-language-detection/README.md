Build the image
```bash
docker build -t lasylphide/xlm-roberta-base-language-detection-roberta-base-language-detection .
```

Run the image
```bash
docker run -p 8080:8080 lasylphide/xlm-roberta-base-language-detection-roberta-base-language-detection
```

Curl the server
```bash 
curl -H "Content-Type: application/json" http://localhost:8080/v1/models/xlm-roberta-base-language-detection:predict -d @./input.json
```