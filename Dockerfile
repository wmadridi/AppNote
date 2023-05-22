FROM ubuntu:latest

# Update the package manager and install Apache2
#RUN apt-get update && apt-get install -y apache2

# Copy the source code to the /var/www/ directory
#COPY ./NoteApp /var/www/
#COPY ./NoteApp/flask-noteapp.conf /etc/apache2/sites-availables
# Expose port 80 for HTTP traffic
#EXPOSE 80

# Start Apache2 service when the container starts
#CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone 
RUN apt update 
RUN apt install apache2 postgresql python3 pip -y
#RUN apt install apache2-utils -y
#RUN apt clean 
COPY --chmod=777 ./app /var/www/app
RUN apt-get install libpq-dev -y
#RUN chmod  0777 -r /var/www/app
WORKDIR /var/www/app/
#COPY /var/www/NoteApp/requirements.txt .
 
RUN pip install -r /var/www/app/requirements.txt 

RUN cp /var/www/app/flask-noteapp.conf /etc/apache2/sites-available/
RUN apt-get install apache2-dev -y
RUN pip install mod_wsgi 
RUN mod_wsgi-express module-config > /etc/apache2/mods-available/wsgi.load
RUN a2enmod wsgi
RUN a2dissite 000-default.conf
RUN a2ensite flask-noteapp.conf
EXPOSE 80
EXPOSE 5432
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
