FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install cron
RUN apt-get update && apt-get install -y cron chromium chromium-driver

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create log directory
RUN mkdir -p /var/log/nba_stats

# Setup cron job
COPY crontab /etc/cron.d/nba-stats-cron
RUN chmod 0644 /etc/cron.d/nba-stats-cron
RUN crontab /etc/cron.d/nba-stats-cron

# Create the log file to be able to run tail
RUN touch /var/log/nba_stats/cron.log

# Run cron in foreground
CMD ["cron", "-f"]
