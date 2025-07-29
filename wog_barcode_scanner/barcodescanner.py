import json

print("[INFO] Barcode Scanner wird gestartet...")

with open("/data/options.json", "r") as f:
    config = json.load(f)

print("[INFO] Konfiguration geladen:")
for k, v in config.items():
    print(f"  {k}: {v}")

# TODO: MariaDB- und FTP-Logik hier einbauen
if config.get("xml_editing"):
    print("[INFO] XML-Bearbeitung ist aktiviert.")
