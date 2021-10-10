FROM python:3.8
WORKDIR /docker_project/webimage
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./web.py", "0.0.0.0:8000" ]