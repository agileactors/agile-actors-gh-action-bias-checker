FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download required NLTK data to lemmatize and tokenize text
RUN python -m nltk.downloader wordnet omw-1.4

COPY bias_detector/ /app/bias_detector/
COPY config/gender_pairs.json /app/config/
WORKDIR /app

ENV PYTHONPATH=/app

ENTRYPOINT ["python", "-m", "bias_detector.main"]
