FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy server script
COPY server.py .

# Expose port 3000
EXPOSE 3000

# Run the server
CMD ["python3", "server.py"]
