# ========================================
# Stage 1: Build stage
# ========================================
FROM python:3.10-slim AS builder

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies in a virtualenv
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# ========================================
# Stage 2: Production (Distroless - NO SHELL!)
# ========================================
FROM gcr.io/distroless/python3-debian11:nonroot

WORKDIR /app

# Copy the virtualenv from builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy app code from builder stage
COPY --from=builder /app/app.py /app/

# Set environment to find Python packages
ENV PYTHONPATH="/opt/venv/lib/python3.10/site-packages:/app"

# Already running as non-root (nonroot user from distroless)
EXPOSE 5000

# NO SHELL ACCESS POSSIBLE!
ENTRYPOINT ["python", "/app/app.py"]
