FROM python:3.7-alpine

RUN apk add --no-cache gcc g++ musl-dev libffi-dev make

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt .
ADD requirements-test.txt .

RUN pip install -r requirements.txt -r requirements-test.txt

ADD . .

CMD ["python", "main.py"]
