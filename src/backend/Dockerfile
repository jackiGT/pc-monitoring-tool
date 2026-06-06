# Base image (using python-slim)
FROM python:slim

# Set work directory (app)
WORKDIR /app

# Copies dependencies file to the working directory
COPY requirements.txt .
# Install dependencies
RUN pip install -r requirements.txt

# Copy rest of backend to co+ntainer
COPY . .

# Port environment variable
#ENV Port=8000
# Expose port so computer can access it
#EXPOSE 8000

# Run application
CMD ["fastapi", "run", "mainAPI.py"]