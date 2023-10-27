# Use the specified Node.js version as the base image
FROM node:16.6.1

# Set environment variables
ENV X=1285
ENV Y=725
ENV COLOR=f00af0

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Compile TypeScript code (assuming you have TypeScript files)
RUN npx tsc src/first.ts

# Specify the command to run your application
CMD ["node", "src/first.js"]
