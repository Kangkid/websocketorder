FROM python:2.7-alpine
RUN RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    pip install psycopg2-binary && \
    pip install requests
COPY ./bill.py .
CMD ["python","bill.py"]