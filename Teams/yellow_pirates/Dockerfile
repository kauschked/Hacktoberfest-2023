FROM subfuzion/netcat

ENV X=5
ENV Y=365
ENV COLOR=dede04

ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
CMD []
