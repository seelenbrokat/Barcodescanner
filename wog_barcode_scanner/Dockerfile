FROM ghcr.io/hassio-addons/base:13.2.0

RUN apk add --no-cache python3 py3-pip

COPY barcodescanner.py /data/barcodescanner.py
COPY run.sh /etc/services.d/barcodescanner/run
RUN chmod +x /etc/services.d/barcodescanner/run
