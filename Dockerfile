FROM python:3

RUN pip install psycopg2

CMD app.py
