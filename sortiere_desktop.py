import os
import shutil
from pathlib import Path

# Desktop erkennen
possible_desktops = [
    Path.home() / "Desktop",
    Path.home() / "OneDrive" / "Desktop"
]
desktop_path = next((p for p in possible_desktops if p.exists()), None)

if not desktop_path:
    print("❌ Kein Desktop-Verzeichnis gefunden.")
    exit()

print(f"📂 Desktop gefunden: {desktop_path}\n")

# Dateitypen-Kategorien
file_type_folders = {
    "PDF": [".pdf"],
    "Programme": [".exe", ".msi", ".bat"],
    "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Dokumente": [".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Tabellen": [".xls", ".xlsx", ".ods", ".csv"],
    "Präsentationen": [".ppt", ".pptx", ".odp"],
    "Archive": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Musik": [".mp3", ".wav", ".flac"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Weblinks": [".url", ".htm", ".html", ".webloc", "lnk", ".webp"],
    # .lnk behandeln wir separat
}

extension_to_folder = {ext: folder for folder, extensions in file_type_folders.items() for ext in extensions}

def categorize_lnk_file(file_path: Path) -> str:
    """Heuristik für .lnk-Dateien: Weblink oder Verknüpfung"""
    name_lower = file_path.name.lower()
    if any(keyword in name_lower for keyword in ["chrome", "firefox", "edge", "web", "www", "http"]):
        return "Weblinks"
    try:
        with open(file_path, "rb") as f:
            content = f.read(2048)
            if b"http" in content or b"www" in content:
                return "Weblinks"
    except:
        pass
    return "Verknuepfungen"

# Durchgehen
for item_path in desktop_path.iterdir():
    if item_path.is_dir():
        print(f"📁 Ordner ignoriert: {item_path.name}")
        continue
    if item_path.name.lower().startswith(("papierkorb", "recycle bin")):
        print(f"🗑️  Papierkorb ignoriert: {item_path.name}")
        continue

    ext = item_path.suffix.lower()

    if ext == ".lnk":
        target_folder_name = categorize_lnk_file(item_path)
    else:
        target_folder_name = extension_to_folder.get(ext)

    if target_folder_name:
        target_folder = desktop_path / target_folder_name
        target_folder.mkdir(exist_ok=True)
        try:
            shutil.move(str(item_path), str(target_folder / item_path.name))
            print(f"✅ {item_path.name} → {target_folder_name}/")
        except Exception as e:
            print(f"❌ Fehler bei {item_path.name}: {e}")
    else:
        print(f"❓ Keine Kategorie für {item_path.name} ({ext})")

print("\n✅ Sortierung abgeschlossen.")
