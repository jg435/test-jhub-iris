FROM jupyter/minimal-notebook

USER root

#conda to install JayDeBeApi as pip installing it fails to build JPype1
RUN pip install conda
RUN conda install JayDeBeApi

# Set working directory to app, put everything in there
WORKDIR /app
ADD ./python-project /app

CMD [ "python3", "./pyIris.py"]