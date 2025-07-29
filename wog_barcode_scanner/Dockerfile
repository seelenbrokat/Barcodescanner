FROM ghcr.io/hassio-addons/base:13.2.0

# Python installieren
RUN apk add --no-cache python3 py3-pip

# Sicherstellen, dass das Dienstverzeichnis existiert
RUN mkdir -p /etc/services.d/barcodescanner

# Scanner-Logik und Startskript einfügen
COPY barcodescanner.py /data/barcodescanner.py
COPY run.sh /etc/services.d/barcodescanner/run

# Ausführbarkeit sicherstellen
RUN chmod +x /etc/services.d/barcodescanner/run
