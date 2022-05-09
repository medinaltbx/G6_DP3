FROM jupyter/scipy-notebook
USER root
COPY notebooks ./notebooks
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt