FROM python:3.11-slim
# Update apt
RUN apt update
RUN apt upgrade -y
# Install build tooling
RUN apt install -y nano build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
    libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
# Copy and install dependencies first (changes rarely)
COPY src/requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
# Copy the rest of the source code after (changes often)
COPY . /PySSED
WORKDIR /PySSED/src
