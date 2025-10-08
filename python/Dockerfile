# Use slim Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies in a virtualenv
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Create non-root user
RUN useradd -ms /bin/bash appuser

# Set ownership and permissions
RUN chown -R appuser:appuser /app && chmod -R 755 /app

# Set environment PATH for virtualenv
ENV PATH="/opt/venv/bin:$PATH"

# Run as non-root user
USER appuser

# Expose port
EXPOSE 5000

# Default command
CMD ["python", "app.py"]
