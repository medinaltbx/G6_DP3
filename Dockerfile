FROM jupyter/scipy-notebook
COPY notebooks ./notebooks
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt