FROM python:3.9.7-slim

# Set the working directory
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV NAME World

# Run app.py
CMD ["python", "app.py"]
