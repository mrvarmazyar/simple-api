FROM docker.mirrors.alibaba.ir/library/python:3.5

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY src .

EXPOSE 8080

CMD ["python3", "-u" , "app.py"]
