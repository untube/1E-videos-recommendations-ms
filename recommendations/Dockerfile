FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /sa_2A_statistics_ms
 WORKDIR /sa_2A_statistics_ms
 ADD requirements.txt /sa_2A_statistics_ms/
 RUN pip3 install -r requirements.txt
 ADD . /sa_2A_statistics_ms/
