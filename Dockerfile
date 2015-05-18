FROM ubuntu:14.04
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y git build-essential
RUN apt-get install -y python3 python3-dev python3-pip
RUN apt-get install -y apache2 apache2-mpm-prefork apache2-utils libexpat1 ssl-cert libapache2-mod-python libapache2-mod-wsgi
RUN /etc/init.d/apache2 restart
ADD . /var/www/application
RUN rm etc/apache2/sites-available/000-default.conf
ADD apache2.conf /etc/apache2/sites-available/000-default.conf
RUN pip3 install -r /var/www/application/requirements.txt
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN /etc/init.d/apache2 restart
EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND