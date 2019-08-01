FROM python

RUN pip install psycopg2

CMD app.py
