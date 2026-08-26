FROM python:3.12-slim
WORKDIR /src
COPY pyproject.toml .
COPY shoppable_extract ./shoppable_extract
RUN pip install --no-cache-dir .
WORKDIR /data
ENTRYPOINT ["shoppable-extract"]
