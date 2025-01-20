FROM python:3.12-slim
COPY . /usr/src/app/
WORKDIR /usr/src/app/
RUN pip install -r requirements.txt
CMD [ "python", "src/main.py" ]