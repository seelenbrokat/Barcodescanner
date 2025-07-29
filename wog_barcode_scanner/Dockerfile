ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:10.4.2
FROM $BUILD_FROM

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Copy add-on files
COPY barcodescanner.py /app/barcodescanner.py
COPY run.sh /etc/services.d/wog_barcode_scanner/run

# Optional: WebApp bereitstellen (falls wieder aktiviert)
COPY webapp/ /app/webapp/

# Make script executable
RUN chmod +x /etc/services.d/wog_barcode_scanner/run

# Expose the web interface port (falls WebUI verwendet wird)
EXPOSE 8099
