ARG BUILD_FROM
FROM $BUILD_FROM

# Labels
LABEL maintainer="seelenbrokat"

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install Python and dependencies
RUN apk add --no-cache python3 py3-pip

# Copy all relevant files into the container
COPY barcodescanner.py /opt/barcodescanner.py
COPY run.sh /etc/services.d/wog_barcode_scanner/run

# Make script executable
RUN chmod +x /etc/services.d/wog_barcode_scanner/run

# Home Assistant s6-overlay expects no CMD or ENTRYPOINT here
