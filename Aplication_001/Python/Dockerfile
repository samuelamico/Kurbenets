FROM python:3.6-alpine AS base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt  /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt


FROM base

COPY --from=builder /install /usr/local
WORKDIR /app
COPY src/main.py /app
CMD ["python3.6", "main.py"]
