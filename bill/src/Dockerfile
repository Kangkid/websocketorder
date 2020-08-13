FROM python:2.7-alpine
RUN apk update && apk add --virtual build-deps gcc python-dev musl-dev && RUN pip install psycopg2-binary && RUN pip install requests
COPY ./bill.py .
CMD ["python","bill.py"]