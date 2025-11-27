# Studi Eksperimental pada Penelitian dan Pengembangan (R&D) Sistem Deteksi Jenis Sampah Menggunakan Model YOLO: Studi Kasus pada Universitas Teknologi Bandung

Konfigurasi Experimen di bawah merupakan Referensi dari Hasil Review Jurnal

## Metode

| No | Metode      |
| -- | ----------- |
| 1  | Klasifikasi |
| 2  | Labeling    |

dari hasil review jurnal menunjukan semuanya menggunakan Labeling, akan tetapi akan di uji ketika menggunakan Klasifikasi

## Devices

| No | Device      | Note |
| -- | ----------- | ---- |
| 1  | SBC ARM     |      |
| 2  | Laptop x64 |      |
| 3  | Server      |      |
| 4  | Smartphone  |      |

## Models

| Model                | Karakteristik                 | Alasan Relevan                 |
| -------------------- | ----------------------------- | ------------------------------ |
| YOLOv8-n, YOLOv8-s   | Cepat & ringan                | Cocok untuk ARM/edge device    |
| YOLOv11-n, YOLOv11-s | Generasi terbaru              | Akurasi lebih tinggi           |
| LEAF-YOLO            | Lightweight untuk objek kecil | Cocok sampah kecil             |
| VBP-YOLO-prune       | Pruned model                  | Ukuran kecil untuk TFLite      |
| YOLO-FCAP            | Lightweight + akurat          | Bagus pada kompleksitas sedang |
| CMD-YOLO             | 0.674M parameters             | Bisa berjalan di CPU rendah    |
| YOLO-SS-tiny         | 2.35M params                  | FPS tinggi                     |
| CD-ViT-YOLO          | Hybrid ViT                    | Untuk akurasi tinggi           |

## Epochs

| Jurnal         | Epoch           |
| -------------- | --------------- |
| VBP-YOLO-prune | 300 epochs      |
| Hybrid-YOLO    | 150 epochs      |
| YOLO-ARM       | 200–300 epochs |
| CMD-YOLO       | 200 epochs      |
| YOLO-FCAP      | 300 epochs      |
| YOLO-MEST      | 200 epochs      |
| WTAD-YOLO      | 150 epochs      |

## Batch

| Device                              | Rekomendasi Batch |
| ----------------------------------- | ----------------- |
| Laptop i5/i7                        | 8–16             |
| GPU ringan (GTX1650–3050)          | 16–32            |
| ARM board (Banana Pi / Jetson Nano) | 4–8              |
| TFLite Training                     | 4–8              |

## Tflite (untuk device sumberdaya rendah)

- FP32 (baseline)
- FP16 (kompatibel ARM)
- INT8 (paling kecil, mungkin turun akurasi)
