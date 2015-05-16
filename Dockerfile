FROM ubuntu:14.04
MAINTAINER Oleg Vasilev <omrigann@gmail.com>
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y tar \
                   git \
                   curl \
                   nano \
                   wget \
                   dialog \
                   net-tools \
                   build-essential
RUN apt-get install -y python3 python3-dev python3-pip
RUN apt-get install -y apache2 apache2-mpm-prefork apache2-utils libexpat1 ssl-cert libapache2-mod-python libapache2-mod-wsgi
RUN /etc/init.d/apache2 restart
ADD . /var/www/omrigan
ADD omrigan.cf.conf /etc/apache2/sites-available/omrigan.cf.conf
RUN a2ensite omrigan.cf
RUN a2dissite 000-default
RUN pip3 install -r /var/www/omrigan/requirements.txt
RUN /etc/init.d/apache2 restart
EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND