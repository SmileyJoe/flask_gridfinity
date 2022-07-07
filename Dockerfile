FROM python:3-alpine

COPY requirements.txt .
COPY setup.py .
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 5000 

CMD python setup.py & python app/app.py
