# Use a base image
FROM alpine:latest

# Set the working directory in the container
WORKDIR /app

# Copy the JSON file into the container
COPY data.json /app/data.json