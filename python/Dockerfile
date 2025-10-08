# ========================================
# Stage 1: BUILDER (Shared dependencies)
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
# Stage 2: DEBUG IMAGE (For Owner - HAS BASH!)
# ========================================
FROM python:3.10-slim AS debug

WORKDIR /app

# Copy virtualenv and app from builder stage
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app/app.py /app/

# Set environment
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/app"

# Create non-root user but keep bash available
RUN useradd -ms /bin/bash appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 5000
CMD ["python", "app.py"]

# ========================================
# Stage 3: PRODUCTION IMAGE (For Public - NO BASH!)
# ========================================
FROM gcr.io/distroless/python3-debian11:nonroot AS production

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
