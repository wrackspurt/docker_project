FROM python:3.8
WORKDIR /docker_project
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./requests_1.py" ]