
FROM node:16

# Set the working directory.
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Build the application.
RUN npm run build

# Start the application.
CMD ["npm", "start"]

EXPOSE 3000



