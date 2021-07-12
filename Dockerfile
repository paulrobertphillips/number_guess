FROM python:3.8

# Set timezone on container
ENV TZ=America/Detroit

# Add user: app
RUN useradd --user-group --create-home --shell /bin/false app

# Set Home directory on container
ENV HOME=/user/app

#WORKDIR /usr/src/app
WORKDIR /home/app

COPY . /home/app

RUN mkdir /data && chmod 777 /data

# Enable userdir
#RUN a2enmod userdir

CMD ["number_guess.py"]

ENTRYPOINT [ "python3" ]