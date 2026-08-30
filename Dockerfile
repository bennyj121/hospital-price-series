FROM python:3.12-slim
LABEL org.opencontainers.image.description="$$40 hospital MRF-change extract (not a quote). Primary order path: https://github.com/bennyj121/hospital-price-series/issues/new?template=mrf-extract-request.yml SAMPLE at examples/sample-mrf-change/"
LABEL org.opencontainers.image.documentation="https://bennyj121.github.io/hospital-price-series/offer.html"
WORKDIR /src
COPY pyproject.toml .
COPY shoppable_extract ./shoppable_extract
RUN pip install --no-cache-dir .
WORKDIR /data
ENTRYPOINT ["shoppable-extract"]
