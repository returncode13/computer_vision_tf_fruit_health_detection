FROM tensorflow/tensorflow:latest-gpu
RUN echo "creating workdir called cv"
WORKDIR cv
RUN pwd
RUN /usr/bin/python3 -m pip install --upgrade pip
RUN apt-get update
RUN echo "copy requirements.txt"
COPY requirements.txt .
RUN ls
RUN echo "pip install "
RUN pip install -r requirements.txt
RUN mkdir /progs 
RUN ls
RUN echo "volume mount at /progs"
VOLUME /progs
RUN ls
RUN mkdir /data
RUN ls
RUN echo "volume mounting at /data"
VOLUME /data
RUN echo "expose port 6999"
EXPOSE 6999
