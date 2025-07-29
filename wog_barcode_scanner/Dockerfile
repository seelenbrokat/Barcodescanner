FROM ghcr.io/hassio-addons/base:13.2.0

#COPY webapp/ /app/webapp/
COPY barcodescanner.py /app/barcodescanner.py
COPY run.sh /etc/services.d/wog_barcode_scanner/run

RUN chmod +x /etc/services.d/wog_barcode_scanner/run
