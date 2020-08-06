FROM python:2.7-alpine
ENV host="130.211.240.105" port="5432" user="postgres" password="123456789" dbname="test"
COPY ./get_shop_info.py .
CMD ["python", "./get_shop_info.py"]