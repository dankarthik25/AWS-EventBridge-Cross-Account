FROM 548593215839.dkr.ecr.us-east-1.amazonaws.com/python:latest
COPY . /home/usr/app
WORKDIR /home/usr/app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
