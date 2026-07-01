import os
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]
outputs_dir = base_dir / "outputs"
outputs_dir.mkdir(parents=True, exist_ok=True)

print("Template inference RVC siap.")
print(f"Hasil output akan disimpan di: {outputs_dir}")
