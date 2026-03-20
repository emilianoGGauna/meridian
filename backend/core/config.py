from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "properties.json"
CHROMA_DIR = BASE_DIR / ".chroma"
