# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get update
RUN apt-get install -y build-essential 

RUN mkdir /tmp/{{ cookiecutter.project_slug }}
COPY ./ /tmp/{{ cookiecutter.project_slug }}/
RUN pip install /tmp/{{ cookiecutter.project_slug }}

RUN rm -rf /tmp/{{ cookiecutter.project_slug }}

RUN mkdir /{{ cookiecutter.project_slug }}
WORKDIR /{{ cookiecutter.project_slug }}

CMD /bin/echo "To use run: {{ cookiecutter.loader_name }}.py"
