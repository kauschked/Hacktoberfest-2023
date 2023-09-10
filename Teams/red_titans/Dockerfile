FROM subfuzion/netcat

ENV X=645
ENV Y=725
ENV COLOR=e07224

ENTRYPOINT sh -c "echo -en 'PX ${X} ${Y} ${COLOR}\n' | nc -q1 localhost 1234"
CMD []