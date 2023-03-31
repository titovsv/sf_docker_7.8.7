FROM python:3.9-slim-bullseye

WORKDIR /app

COPY ./app ./

RUN pip install --no-cache-dir -r requirements.txt

VOLUME /tmp/favicons

ENTRYPOINT ["python", "./app.py"]

CMD ["http://google.com"]

