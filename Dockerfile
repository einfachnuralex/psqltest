FROM python:3

WORKDIR /srv/app

RUN pip install psycopg2

COPY app.py .

CMD /srv/app/app.py
