FROM ubuntu:14.04
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y git build-essential \
                       python3 python3-dev python3-pip \
                       nginx && \
    apt-get clean
ADD . /var/www/application
RUN rm /etc/nginx/sites-enabled/default
ADD nginx.conf /etc/nginx/sites-enabled/default
RUN pip3 install -r /var/www/application/requirements.txt
EXPOSE 80
WORKDIR "/var/www/application"
CMD /etc/init.d/nginx start && uwsgi --socket :8001 --module diploma.wsgi
