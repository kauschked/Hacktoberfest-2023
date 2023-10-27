FROM subfuzion/netcat
FROM python:3.12

ENV X=645
ENV Y=725
ENV COLOR=e07224
# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src
#ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
#to COPY the remote file at working directory in container
COPY Challenge1.py ./
COPY simple_client.py ./
COPY rgb.png ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./Challenge1.py"]
CMD [ "python", "./simple_client.py"]
