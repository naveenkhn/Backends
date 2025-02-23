# Use an Alpine-based image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside
EXPOSE 5000

# Set the command to run the application
CMD ["python", "app.py"]