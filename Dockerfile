FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /sa_1E_recommendations_ms
 WORKDIR /sa_1E_recommendations_ms
 ADD requirements.txt /sa_1E_recommendations_ms/
 RUN pip3 install -r requirements.txt
 ADD . /sa_1E_recommendations_ms/
 EXPOSE 3003
