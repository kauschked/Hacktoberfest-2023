FROM subfuzion/netcat
FROM python:3.12

ENV X=645
ENV Y=725
ENV COLOR=e07224
# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/
#ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
RUN python3 -m venv .venv/
RUN . .venv/bin/activate && pip install --upgrade Pillow

COPY src/ src/

#CMD [ "python", "./Challenge1.py"]
CMD [ "/usr/app/.venv/bin/python3", "/usr/app/src/simple_client.py"]

