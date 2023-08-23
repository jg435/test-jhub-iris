FROM jupyter/minimal-notebook

USER root

RUN pip install JayDeBeApi
# Set working directory to app, put everything in there
WORKDIR /app
ADD ./python-project /app

CMD [ "python3", "./pyIris.py"]