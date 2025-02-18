# frontend/Dockerfile

# Use an official Node.js runtime as the base image
FROM node:18 AS build-stage

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY . .

# Install dependencies
RUN npm install

# Install Quasar CLI globally
RUN npm install -g @quasar/cli

# Build the Quasar application
RUN quasar build

# Use a lightweight Nginx image to serve the built files
FROM nginx:alpine AS production-stage

# Copy the built files from the build-stage
COPY --from=build-stage /app/dist/spa /usr/share/nginx/html

# Expose port 80 for the Nginx server
EXPOSE 80

# Command to run the Nginx server
CMD ["nginx", "-g", "daemon off;"]