FROM python:3.8-slim

WORKDIR /app
COPY .. /app
RUN pip install -r requirements.txt
CMD ["python", "model.py"]

EXPOSE 8080
