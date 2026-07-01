import os
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]
dataset_dir = base_dir / "dataset"
for folder in ["A", "B"]:
    target = dataset_dir / folder
    target.mkdir(parents=True, exist_ok=True)

print(f"Folder dataset siap di: {dataset_dir}")
print("Letakkan file audio suara A di folder dataset/A")
print("Letakkan file audio suara B di folder dataset/B")
