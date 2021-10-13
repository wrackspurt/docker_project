FROM python:3.8
WORKDIR /docker_project/arsnewsimage
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./requests_ars.py" ]