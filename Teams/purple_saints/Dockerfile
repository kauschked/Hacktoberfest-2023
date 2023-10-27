FROM node:16

ENV X=1285
ENV Y=725
ENV COLOR=f00af0

RUN npm install

RUN npx tsc src/first.ts

# Führen Sie das kompilierte JavaScript-Programm aus
ENTRYPOINT [ "node", "src/first.js" ]
