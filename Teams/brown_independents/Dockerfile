FROM subfuzion/netcat

ENV X=5
ENV Y=5
ENV COLOR=692f05

ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
CMD []