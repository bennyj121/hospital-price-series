FROM python:3.12-slim
LABEL org.opencontainers.image.description="$$40 hospital MRF-change extract (not a quote). https://bennyj121.github.io/hospital-price-series/offer.html SAMPLE at examples/sample-mrf-change/"
WORKDIR /src
COPY pyproject.toml .
COPY shoppable_extract ./shoppable_extract
RUN pip install --no-cache-dir .
WORKDIR /data
ENTRYPOINT ["shoppable-extract"]
