#Base image: stable Python slim variant
FROM python:3.11.15-slim-trixie

#Set working directory
WORKDIR /app

#Upgrade system packages & clean cache (reduces vulnerabilities)
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

#Create non-root user
RUN useradd -m appuser
USER appuser

#Copy application files
COPY --chown=appuser:appuser main.py .
COPY --chown=appuser:appuser requirements.txt .

#Upgrade pip and install pinned dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

#Expose port (matches Azure Container App ingress)
EXPOSE 8080

#Default command
CMD ["python", "main.py"]