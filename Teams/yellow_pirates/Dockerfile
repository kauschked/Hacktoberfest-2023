FROM python:3.11.4

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir  numpy pillow

RUN mkdir /app

COPY ./src/* /app

# ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
ENTRYPOINT ["python", "/app/c2.py"]
