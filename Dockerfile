FROM python:3.9
COPY . /app
WORKDIR /app

RUN pip install

ENV PYTHONUNBEFFERD 1

EXPOSE 8001
CMD python3 ./mail.py
