# Judul : Studi Eksperimental pada Penelitian dan Pengembangan (R&D) Menggunakan Model YOLO untuk Perangkat Heterogen: Studi Kasus Deteksi Sampah di Universitas Teknologi Bandung

# BAB I PENDAHULUAN

### 1.1 Latar Belakang

Permasalahan pengelolaan sampah di Indonesia masih menjadi tantangan serius, baik di tingkat nasional maupun daerah. Dibawah ini adalah hasil dari penginputan data yang dilakukan oleh 334 Kabupaten/kota se-Indonesia pada tahun 2024.

Rincian kondisi pengelolaan sampah di Indonesia adalah sebagai berikut:

* **Pengurangan sampah:** 497.674,99 ton/tahun ( **1,36%** )
* **Penanganan sampah:** 11.453.258,04 ton/tahun ( **31,35%** )
* **Total sampah terkelola:** 11.950.933,03 ton/tahun ( **32,71%** )
* **Sampah tidak terkelola:** 24.587.314,56 ton/tahun ( **67,29%** )

Dari total sampah yang dikelola, sebagian besar masih berakhir di tempat pembuangan akhir ( **TPA** ) dengan sistem:

* **TPA Control/Sanitary:** 5.956.743,84 ton/tahun
* **TPA Open Dumping:** 9.393.130,82 ton/tahun

Data tersebut menunjukkan bahwa  **lebih dari dua pertiga sampah nasional masih belum terkelola dengan baik** , sehingga menimbulkan dampak serius terhadap lingkungan, kesehatan, serta tata kelola perkotaan. Salah satu penyebab rendahnya tingkat pengelolaan adalah  **minimnya sistem pemilahan di sumber.**

Sumber 

Pengelolaan sampah di lingkungan kampus merupakan isu nyata yang memerlukan solusi terukur dan berkelanjutan. Universitas Teknologi Bandung (UTB) telah menunjukkan komitmen untuk membangun *Socio-Creativepreneur University* melalui penggabungan aspek sosial dan teknologi, termasuk dalam sistem pengelolaan sampah yang berorientasi pada peningkatan nilai ekonomi serta pengurangan penumpukan sampah di area kampus. Berdasarkan hasil observasi lapangan, produksi sampah di lingkungan kampus mencapai rata-rata  **7 kantong trash bag per hari** , dengan jadwal  **pengangkutan hanya satu kali dalam seminggu** . Kondisi ini menyebabkan sampah sering menumpuk di beberapa titik apabila terjadi keterlambatan pengangkutan.

Saat ini, sistem pengelolaan yang sudah berjalan di UTB berfokus pada **pemilahan dan pembersihan botol plastik tertentu** untuk kemudian dijual kembali sebagai bentuk  *recycling economy* . Beberapa inisiatif daur ulang juga telah diupayakan, seperti  **pengolahan plastik menjadi paving block** ,  **pemanfaatan tutup botol sebagai bahan pembuatan furnitur** , serta **program daur ulang kertas** yang sempat berjalan namun belum dilanjutkan secara konsisten. Siklus pengelolaan tersebut menunjukkan bahwa upaya menuju sistem pengelolaan sampah berkelanjutan sudah dimulai, tetapi masih memerlukan dukungan teknologi untuk memantau, mengelompokkan, dan mengoptimalkan proses pengolahan agar tidak berhenti di tahap awal pengumpulan.

Sebagai bagian dari transformasi menuju kampus berbasis teknologi, **Universitas Teknologi Bandung (UTB)** memiliki rencana strategis untuk mengintegrasikan pengembangan **Artificial Intelligence (AI)** ke dalam kegiatan akademik dan riset terapan. Langkah ini sejalan dengan arah kebijakan nasional yang mendorong adopsi AI di lingkungan pendidikan tinggi. Dorongan ini diperkuat melalui kegiatan **Seminar AI Connect: *“Artificial Intelligence di Ekosistem Perguruan Tinggi – Membangun Sinergi Kampus dan Industri Menuju Keunggulan Kompetitif Digital”*** yang diadakan oleh  **LLDIKTI Wilayah IV Jawa Barat dan Banten** pada Senin, 20 Oktober 2025.

Dalam seminar tersebut,  **Dr. Lukman, S.T., M.Hum.** , selaku Kepala LLDIKTI Wilayah IV, menekankan pentingnya bagi perguruan tinggi untuk mulai  **mengadopsi teknologi AI dalam sistem pembelajaran dan riset** , serta **memasukkan materi AI ke dalam kurikulum** agar lulusan perguruan tinggi mampu bersaing di era transformasi digital. UTB merespons arahan tersebut dengan mulai merancang program riset terapan yang menggabungkan AI dengan bidang sosial, lingkungan, dan kewirausahaan, termasuk riset pengelolaan sampah berbasis *computer vision* sebagai bentuk implementasi nyata teknologi AI di lingkungan kampus.

Melihat kondisi nasional di mana sebagian besar sampah di Indonesia masih belum terkelola dengan baik, serta tantangan pengelolaan sampah yang juga terjadi di lingkungan kampus, **Universitas Teknologi Bandung (UTB)** menempatkan isu ini sebagai fokus riset yang relevan dengan visi kampus untuk menjadi  *Socio-Creativepreneur University* . Permasalahan menumpuknya sampah akibat keterbatasan sistem pengangkutan dan belum optimalnya proses daur ulang menjadi dasar penting bagi UTB untuk mencari solusi yang lebih terukur dan efisien. Dalam konteks ini, pengembangan **Artificial Intelligence (AI)** hadir sebagai peluang strategis untuk mendukung otomatisasi pemilahan sampah, analisis data timbulan, serta peningkatan efisiensi pengelolaan lingkungan kampus. Dukungan pemerintah melalui **LLDIKTI Wilayah IV** dan dorongan langsung dari **Dr. Lukman, S.T., M.Hum.** semakin memperkuat komitmen UTB untuk mengintegrasikan AI ke dalam riset dan kurikulum, menjadikan pengelolaan sampah berbasis *computer vision* bukan hanya sebagai proyek teknologis, tetapi juga sebagai langkah nyata menuju transformasi digital kampus yang berkelanjutan dan berdaya saing.

[Alasan menggunakan Yolo]

Data yang digunakan dalam proses *training* model YOLO pada penelitian ini terdiri dari  **sembilan kategori sampah utama** , yaitu: *botol-kaleng, box-kertas, cup-kertas, kertas, plastik, botol-plastik, box-plastik, cup-plastik, organik,* dan  *residu* . Setiap kategori memiliki **200 citra** yang diambil secara langsung dari  **lingkungan kampus Universitas Teknologi Bandung (UTB)** , sehingga dataset ini merepresentasikan **kondisi nyata sampah kampus** yang beragam dari segi bentuk, warna, dan tingkat kebersihan. Data tersebut kemudian dibagi ke dalam dua bentuk pengolahan: pertama,  **teknik klasifikasi berbasis struktur folder** , di mana setiap kategori sampah ditempatkan dalam folder terpisah untuk melatih model mengenali ciri visual khas tiap jenis; dan kedua,  **teknik labeling menggunakan Label Studio** , yang memberikan anotasi langsung pada area objek dalam citra agar YOLO dapat mempelajari posisi dan bentuk sampah secara lebih presisi. Pendekatan ganda ini dirancang untuk mencari metode terbaik dengan melakukan analisis pada nilai Akurasi, Latensi dan Ukuran Model untuk mengoptimalkan model ketika melakukan  **identifikasi dan deteksi objek sampah secara real-time**  pada Perangkat Heterogen, sekaligus memastikan bahwa sistem yang dikembangkan benar-benar relevan dengan konteks lingkungan kampus dan dapat digunakan sebagai dasar pengelolaan sampah berbasis kecerdasan buatan.

karena setiap perangkat memiliki  **kemampuan komputasi dan kebutuhan operasional yang berbeda** , penelitian ini difokuskan pada **eksperimen parameter pelatihan model YOLO** serta **ekspor model ke format ringan** yang dapat dijalankan pada perangkat dengan sumber daya terbatas, seperti **laptop** dan  **perangkat berbasis ARM** . Tujuan dari eksperimen ini adalah untuk **menghasilkan rekomendasi konfigurasi yang optimal dan aplikatif** sesuai karakteristik perangkat target, sehingga proses implementasi dapat berlangsung lebih cepat, efisien, dan mengurangi kebutuhan *trial-and-error* teknis bagi tim pengembang maupun pelaksana di lapangan.

### 1.2 Rumusan Masalah

Rumusan masalah difokuskan pada kendala nyata yang memerlukan solusi teknis AI untuk mendukung pengelolaan sampah di lingkungan kampus:

1. Bagaimana memilih konfigurasi pelatihan (jumlah  **epoch** ,  **batch size** , dan  **jenis model** ) yang memberikan *trade-off* terbaik antara akurasi deteksi, latensi dan ukuran model pada P**erangkat Heterogen** ?
2. Bagaimana menyesuaikan konfigurasi pelatihan dan metode ekspor ke model yang lebih ringan agar model tetap akurat namun efisien saat di-*deploy* pada **Perangkat Sumberdaya Terbatas**?
3. Bagaimana melakukan ***deployment*** ke perangkat Heterogen sehingga model dapat berjalan baik terutama pada **Perangkat Sumberdaya Terbatas** tanpa penurunan performa yang signifikan?
4. Bagaimana pengaruh **perbedaan metode pelabelan dan klasifikasi** terhadap akurasi, latensi dan ukuran model?
5. Bagaimana hasil akurasi, latensi dan ukuran model yang relevan untuk mendukung program  **Smart Kampus pada Bank Sampah UTB** ?

### **1.3 Tujuan Penelitian**

Penelitian ini bertujuan untuk: minimal 2 baris

1. **Menentukan konfigurasi pelatihan terbaik** (jumlah  *epoch* ,  *batch size* , dan jenis model YOLO) yang mampu memberikan *trade-off* optimal antara **akurasi deteksi, latensi, dan ukuran model** pada berbagai **perangkat heterogen** seperti laptop dan perangkat berbasis ARM.
2. **Menganalisis performa model hasil pelatihan yang diekspor ke format ringan** , seperti TFLite atau model terkuantisasi, agar dapat dijalankan secara efisien pada **perangkat dengan sumber daya terbatas** tanpa mengorbankan akurasi secara signifikan.
3. **Menguji proses *deployment*** model deteksi sampah ke **berbagai jenis perangkat heterogen** untuk memastikan model tetap stabil dan cepat saat dijalankan di lingkungan nyata, khususnya pada sistem berbasis  *edge computing* .
4. **Membandingkan pengaruh metode klasifikasi dan labeling** terhadap performa model YOLO dalam hal akurasi, latensi, dan ukuran model guna menentukan pendekatan yang paling efektif untuk deteksi sampah di lingkungan kampus.
5. **Menghasilkan rekomendasi konfigurasi model YOLO** yang relevan dan aplikatif sebagai dasar pengembangan sistem  **Smart Kampus Bank Sampah UTB** , yang mendukung otomatisasi pemilahan sampah dan efisiensi pengelolaan lingkungan kampus.

---

### **1.4 Manfaat Penelitian - dibuat lebih banyak**

Hasil penelitian ini diharapkan memberikan manfaat bagi berbagai pihak, baik secara akademik, institusional, maupun sosial-lingkungan, sebagai berikut:

**a. Akademisi dan Peneliti**

Memberikan kontribusi ilmiah dalam bentuk  **eksperimen parameter pelatihan model YOLO untuk perangkat heterogen** , serta menjadi **referensi penelitian lanjutan** di bidang  *computer vision* ,  *edge AI* , dan  *environmental informatics* . Penelitian ini juga membuka peluang bagi pengembangan riset terapan di bidang **AI for Sustainability** dan penerapan teknologi cerdas di sektor pendidikan.

**b. Lingkungan Kampus**

Mendukung terwujudnya **Smart Kampus Universitas Teknologi Bandung (UTB)** melalui sistem  **pengelolaan sampah otomatis berbasis kecerdasan buatan** , yang dapat membantu proses **pemilahan, pemantauan, dan pengumpulan data timbulan sampah** secara efisien. Implementasi hasil penelitian juga dapat menjadi **model awal integrasi AI dalam kegiatan riset dan pembelajaran lintas disiplin** di kampus.

**c. Masyarakat dan Lingkungan**

Menjadi langkah nyata dalam **peningkatan kesadaran dan efisiensi pengelolaan sampah** di lingkungan masyarakat melalui contoh penerapan teknologi berbasis AI yang ramah lingkungan. Penelitian ini diharapkan dapat menginspirasi lembaga lain untuk  **mengadopsi pendekatan teknologi cerdas dalam mendukung ekonomi sirkular** , serta membantu mengurangi volume sampah yang tidak terkelola melalui sistem deteksi dan pemilahan yang lebih efektif.

### 1.5 Ruang Lingkup Penelitian

1. Dataset: citra sampah di lingkungan kampus (kelas inti: *botol-kaleng, box-kertas, cup-kertas, kertas, plastik, botol-plastik, box-plastik, cup-plastik, organik,* dan  *residu*.).
2. Model: varian YOLO (dari nano/compact sampai large) dan ekspor ke TFLite dengan beberapa skema kuantisasi.
3. Eksperimen: variasi epoch, batch size, jenis model dan kuantisasi; pengujian inferensi pada perangkat uji representatif.
4. Implementasi sistem end-to-end (mekanisme sorting fisik) **tidak** menjadi fokus; penelitian berfokus pada model dan rekomendasi konfigurasi.

### 1.6 Sistematika Penulisan
