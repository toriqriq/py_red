# So-VITS Project

Proyek ini dipersiapkan untuk mengubah suara A menjadi suara B dengan So-VITS.

## Struktur folder

- [dataset](dataset): tempat menyimpan audio suara A dan B
  - [dataset/A](dataset/A): suara sumber
  - [dataset/B](dataset/B): suara target
- [models](models): tempat hasil training model
- [outputs](outputs): tempat hasil inference dan konversi suara
- [scripts](scripts): tempat skrip pendukung

## Alur kerja

1. Siapkan audio suara A dan suara B.
2. Tempatkan audio ke folder [dataset/A](dataset/A) dan [dataset/B](dataset/B).
3. Jalankan preprocessing data.
4. Jalankan training model.
5. Jalankan inference untuk menghasilkan suara target.

## Catatan penting

- Gunakan audio dengan kualitas baik dan bersih.
- Pilih audio yang cukup panjang agar hasil training lebih baik.
- Simpan file dengan nama yang rapi dan konsisten.

## Langkah berikutnya

- Clone repositori So-VITS ke folder proyek atau ke subfolder terpisah.
- Siapkan environment Python di Windows.
- Jalankan preprocessing setelah dataset siap.
