FROM subfuzion/netcat

ENV X=1285
ENV Y=365
ENV COLOR=f00af0

ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
CMD []