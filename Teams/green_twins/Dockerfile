FROM subfuzion/netcat

ENV X=1285
ENV Y=5
ENV COLOR=02d10c

ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
CMD []
