# ---- Base image ----
FROM python:3.11-slim

# Install Node + Chrome + drivers
RUN apt-get update && apt-get install -y curl gnupg unzip \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs chromium chromium-driver \
    && npm install -g newman \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy project
COPY . .

# Install Python deps
RUN pip install -r requirements.txt && pip install pip-audit

# Set Chrome path for Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

# Default command: run UI + API tests
CMD pytest -n auto --html=report.html --self-contained-html && newman run api_tests.json