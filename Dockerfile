FROM python:3.12-slim

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy the rest of the application
COPY . .

# Expose port
EXPOSE 8000

# Use entrypoint script
ENTRYPOINT ["uv", "run", "app/app.py"]
