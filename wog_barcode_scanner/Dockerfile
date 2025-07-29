ARG BUILD_FROM
FROM $BUILD_FROM

# Add-on metadata
LABEL \
    org.opencontainers.image.title="WOG Barcode Scanner" \
    org.opencontainers.image.description="Barcode-Scanner Add-on mit Weboberfläche" \
    org.opencontainers.image.source="https://github.com/seelenbrokat/barcodescanner" \
    org.opencontainers.image.licenses="MIT"

# Install Python
RUN apk add --no-cache python3 py3-pip

# Add App
COPY barcodescanner.py /app/barcodescanner.py
COPY run.sh /etc/services.d/wog_barcode_scanner/run

# Optional: Webapp
#COPY webapp/ /app/webapp/

# Make script executable
RUN chmod a+x /etc/services.d/wog_barcode_scanner/run

# Set workdir
WORKDIR /app
