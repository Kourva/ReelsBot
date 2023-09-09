# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/
COPY bot.py /app/
COPY Token.env /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define the command to run your bot when the container starts
CMD ["python", "bot.py"]