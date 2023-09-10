FROM subfuzion/netcat

ENV X=5
ENV Y=725
ENV COLOR=e6e3e6

ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
CMD []