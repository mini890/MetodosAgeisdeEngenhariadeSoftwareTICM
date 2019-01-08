FROM python:latest
RUN mkdir /django
WORKDIR /django
RUN python -m venv tdd
RUN ls tdd/bin
RUN /bin/bash -c "source tdd/bin/activate"
RUN apt-get install git -y
RUN git clone https://gitlab.com/mini890/djangodocker.git
RUN ls djangodocker
RUN