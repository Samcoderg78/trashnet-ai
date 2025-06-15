FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt google-auth

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
