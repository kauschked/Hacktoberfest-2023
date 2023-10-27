FROM node:16.6.1

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npx tsc src/first.ts

CMD ["node", "src/first.js"]
