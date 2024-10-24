# Make sure to check bin/run_services.sh, which can be used here

# Do not forget to expose the right ports! (Check the PR_4.md)
# Use an official Python runtime as a base image
FROM python:3.12-slim as base

# Set the working directory in the container
WORKDIR /xhec-mlops-project-student

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code into the container
COPY . .

RUN chmod +x ./bin/run_services.sh

RUN pip install pip-tools

# Install dependencies
RUN pip-compile requirements.in
RUN pip-compile requirements-dev.in

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

EXPOSE 8001
EXPOSE 4002

# Health check to ensure the application is running
HEALTHCHECK CMD curl --fail http://localhost:4201/_stcore/health || exit 1 && curl --fail http://localhost:8001/_stcore/health || exit 1

ENTRYPOINT ["./bin/run_services.sh"]