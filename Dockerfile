FROM python:3.9-slim-buster
COPY . /home/usr/app
WORKDIR /home/usr/app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
