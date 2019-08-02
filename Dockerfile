FROM python:3

RUN pip install psycopg2

COPY app.py .

CMD app.py
