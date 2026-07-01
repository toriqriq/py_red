# Instalasi RVC di Windows

## 1. Persiapan

- Install Python 3.10 atau 3.11
- Install Git
- Install FFmpeg

## 2. Buat environment Python

```powershell
py -3.11 -m venv venv
venv\Scripts\activate
```

## 3. Clone repositori RVC

```powershell
git clone <url-repo-rvc>
cd <folder-repo-rvc>
```

## 4. Install dependensi

```powershell
pip install -r requirements.txt
```

## 5. Siapkan dataset

Letakkan audio suara A di folder dataset/A dan suara B di folder dataset/B.

## 6. Jalankan training dan inference

Ikuti instruksi resmi dari repositori RVC yang Anda gunakan.
