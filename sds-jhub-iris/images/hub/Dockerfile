FROM jupyter/minimal-notebook

USER root

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get install ca-certificates-java && \
    apt-get install -y --no-install-recommends python3 && \
    apt-get install -y python3-pip && \
    apt-get clean && \ 
    update-ca-certificates -f;

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN pip install --upgrade pip
#conda to install JayDeBeApi as pip installing it fails to build JPype1
#RUN pip install conda
RUN pip install JayDeBeApi

# Set working directory to app, put everything in there
#WORKDIR /app
#ADD ./python-project /app

#CMD [ "python3", "./pyIris.py"]