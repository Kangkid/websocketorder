FROM python:2.7-alpine
RUN pip install psycopg2-binary
COPY ./get_shop_info.py .
CMD ["python -c "import get_shop_info;get_shop_info.main_handler()""]