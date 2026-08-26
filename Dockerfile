FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir git+https://github.com/bennyj121/hospital-price-series.git
WORKDIR /data
ENTRYPOINT ["shoppable-extract"]
