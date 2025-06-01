#  Sistem Rekomendasi Anime - Reinhart Jens Robert

## Project Overview

Dalam era digital saat ini, jumlah konten hiburan seperti anime terus meningkat pesat. Dengan ribuan judul anime yang tersedia, pengguna sering mengalami kesulitan dalam menemukan anime yang sesuai dengan preferensi mereka. Fenomena ini dikenal sebagai "information overload" dimana terlalu banyak pilihan justru membuat pengambilan keputusan menjadi sulit.
Sistem rekomendasi telah menjadi solusi yang sangat efektif untuk mengatasi masalah ini. Platform seperti Netflix, Crunchyroll, dan MyAnimeList menggunakan sistem rekomendasi untuk membantu pengguna menemukan konten yang relevan dengan preferensi mereka. Hal ini tidak hanya meningkatkan kepuasan pengguna, tetapi juga meningkatkan engagement dan retention pada platform tersebut.
royek ini penting untuk diselesaikan karena:

1. Meningkatkan User Experience: Membantu pengguna menemukan anime yang sesuai dengan preferensi mereka dengan lebih efisien
2. Mengatasi Information Overload: Mengurangi waktu yang dibutuhkan pengguna untuk mencari anime yang menarik
3. Personalisasi: Memberikan rekomendasi yang dipersonalisasi berdasarkan karakteristik anime dan pola preferensi pengguna
4. Business Value: Sistem rekomendasi yang baik dapat meningkatkan engagement dan monetisasi platform


## Business Understanding
Berdasarkan analisis kebutuhan pengguna dan tantangan dalam industri anime streaming, masalah utama yang ingin diselesaikan adalah:

1. Kesulitan Discovery: Bagaimana cara membantu pengguna menemukan anime baru yang sesuai dengan preferensi mereka dari ribuan judul yang tersedia?
2. Personalisasi Rekomendasi: Bagaimana cara memberikan rekomendasi yang dipersonalisasi berdasarkan karakteristik anime (genre, tipe, rating) dan pola preferensi pengguna?
3. Cold Start Problem: Bagaimana cara memberikan rekomendasi yang relevan untuk pengguna baru yang belum memiliki riwayat rating atau preferensi?

**Goals:**
Tujuan dari proyek ini adalah:

1. Mengembangkan sistem rekomendasi hybrid yang dapat memberikan rekomendasi anime yang akurat dan relevan dengan menggabungkan pendekatan Content-Based Filtering dan Collaborative Filtering.
2. Meningkatkan akurasi rekomendasi dengan memanfaatkan informasi konten anime (genre, tipe) dan pola rating pengguna untuk menghasilkan rekomendasi yang lebih personal dan relevan.
3. Mengatasi keterbatasan masing-masing metode dengan memanfaatkan kelebihan dari kedua pendekatan untuk menciptakan sistem yang lebih robust dan komprehensif.

### Solution Approach
Untuk mencapai goals yang telah ditetapkan, proyek ini akan mengimplementasikan dua pendekatan sistem rekomendasi:
1. Content-Based Filtering
Pendekatan ini merekomendasikan anime berdasarkan kesamaan karakteristik konten dengan anime yang disukai pengguna sebelumnya.

Metode yang digunakan:

- TF-IDF Vectorization: Untuk mengubah fitur kategoris (genre, tipe) menjadi representasi numerik
- Cosine Similarity: Untuk mengukur kesamaan antar anime berdasarkan fitur konten

Kelebihan:

- Tidak memerlukan data dari pengguna lain
- Dapat memberikan rekomendasi untuk anime baru (tidak ada cold start problem untuk item)
- Rekomendasi dapat dijelaskan dengan jelas (explainable)

Kekurangan:

- Terbatas pada fitur yang tersedia dalam dataset
- Cenderung memberikan rekomendasi yang similar (lack of diversity)
- Tidak dapat menangkap preferensi pengguna yang kompleks

2. Collaborative Filtering
Pendekatan ini merekomendasikan anime berdasarkan pola rating dan preferensi pengguna yang memiliki selera similar.

Metode yang digunakan:

- Matrix Factorization dengan SVD (Singular Value Decomposition): Untuk mereduksi dimensi dan mengekstrak faktor laten dari user-item matrix
- Synthetic User Generation: Karena dataset tidak memiliki data user rating, akan dibuat synthetic users berdasarkan popularity dan rating anime

Kelebihan:

- Dapat menangkap preferensi kompleks dan pola tersembunyi
- Tidak bergantung pada fitur konten
- Dapat memberikan rekomendasi yang unexpected dan diverse

Kekurangan:

- Memerlukan data rating dari banyak pengguna
- Cold start problem untuk pengguna dan item baru
- Sulit untuk dijelaskan (black box)

3. Hybrid Approach
Menggabungkan kedua pendekatan di atas untuk memanfaatkan kelebihan masing-masing dan mengurangi kelemahan individual.

# Data Understanding
## 1. DATA LOADING DAN EXPLORATORY DATA ANALYSIS

### Informasi Umum Dataset
1. Dataset terdiri dari 12.294 baris dan 7 kolom, artinya ada 12.294 data anime yang dianalisis.

2. Masing-masing baris merepresentasikan satu judul anime dengan informasi terkait seperti genre, tipe, episode, rating, dan jumlah anggota.

### 5 Data Teratas
1. Contoh data teratas mencakup anime populer seperti Kimi no Na wa., Fullmetal Alchemist: Brotherhood, dan Gintama°, Steins;Gate, Gintama&#039;  

2. Informasi yang diberikan meliputi judul anime, genre, tipe (TV/Movie), jumlah episode, rating, dan jumlah anggota yang menambahkan anime ke daftar mereka.


### Struktur dan Tipe Data
1. Kolom anime_id, members bertipe integer.

2. Kolom rating bertipe float.

3. Kolom name, genre, type, dan episodes bertipe object (teks).

4. Jumlah data kosong (missing values) cukup kecil, hanya ada:

  - 62 nilai kosong pada genre (sekitar 0,5%)

  - 25 nilai kosong pada type (sekitar 0,2%)

  - 230 nilai kosong pada rating (sekitar 1,87%)

5. Tidak ada data duplikat

### Statistik Deskriptif
1. Rating anime memiliki nilai rata-rata sekitar 6.47, dengan minimum 1.67 dan maksimum 10.0.

2. Jumlah anggota sangat bervariasi, dengan median sekitar 1.550, tapi bisa mencapai lebih dari 1 juta pada anime yang sangat populer.

3. Distribusi members menunjukkan banyak anime yang kurang dikenal (dengan sedikit anggota) dan segelintir anime yang sangat populer.

## Penjelasan visualisasi 
1. Distribusi Rating Anime
Mayoritas anime memiliki rating antara 6 dan 7, membentuk distribusi normal.

2. Distribusi Tipe Anime
Tipe anime paling banyak adalah TV (30.9%), disusul OVA (27%) dan Movie (19.1%).

3. Top 10 Genre Terpopuler
Genre paling populer adalah Comedy, diikuti Action dan Adventure.

4. Distribusi Jumlah Episode (≤50)
Kebanyakan anime memiliki jumlah episode sedikit, terutama di bawah 10 episode.

5. Rating vs Jumlah Members
Terdapat kecenderungan bahwa anime dengan lebih banyak anggota cenderung memiliki rating yang lebih tinggi.
6. Top 10 Anime Rating Tertinggi
Anime dengan rating tertinggi adalah Gintama, Steins;Gate, dan Yakusoku: Africa Mizu to Midori.

7. Korelasi Antar Variabel Numerik
Terdapat korelasi sedang antara rating dan jumlah members (0.39), sedangkan korelasi dengan jumlah episode sangat lemah.

# 3. DATA PREPARATION
### 3.1 Data Cleaning
Membersihkan data dan menangani missing values untuk persiapan modeling.

1. Handle Missing Values (Menangani Data Kosong)
- Awalnya terdapat 317 data kosong di seluruh kolom.

- Baris dengan nilai rating kosong dihapus karena rating penting untuk sistem rekomendasi (misalnya collaborative filtering).

- Nilai kosong pada kolom genre diisi dengan string "Unknown".

- Kolom episodes yang berisi teks seperti "Unknown" dikonversi ke numerik (episodes_numeric), lalu nilai yang tidak bisa dikonversi (NaN) diganti dengan median dari kolom tersebut.

- Setelah ini, tidak ada lagi missing values.

2. Remove Duplicates (Menghapus Duplikasi)
- Dilakukan penghapusan baris duplikat agar tidak mengganggu proses analisis.

- Setelah proses ini, jumlah data menjadi 12.064 baris dan 8 kolom.

3. Filter Berdasarkan Jumlah Members
- Data difilter agar hanya menyertakan anime yang memiliki minimal 1000 members, untuk menghindari data yang terlalu jarang dinilai.

- Setelah filter ini, jumlah data berkurang menjadi 6.791 baris.

4. Normalisasi Rating
- Kolom rating dinormalisasi ke skala 0–1, yang berguna untuk algoritma yang sensitif terhadap skala (seperti KNN atau cosine similarity).

- Hasilnya disimpan di kolom baru: rating_normalized.

5. Membuat Fitur Konten (Content Features)
- Untuk keperluan content-based filtering, dibuat fitur content_features dengan menggabungkan isi kolom genre dan type menjadi satu string teks.

- Ini mempermudah transformasi teks ke vektor fitur seperti TF-IDF.

Output Akhir
- Setelah semua proses, dataset akhir memiliki bentuk (shape): 6.791 baris dan 10 kolom.

- Artinya, data kini bersih, terfilter, dan siap dipakai untuk model rekomendasi baik berbasis konten maupun kolaboratif.

# Modeling
##  CONTENT-BASED FILTERING
Content-Based Filtering merekomendasikan item berdasarkan kesamaan karakteristik/fitur dari item tersebut.
Dalam kasus ini, kita akan menggunakan genre sebagai fitur utama untuk menghitung kesamaan antar anime.

1. Model & Dataset
- Model content-based dilatih menggunakan 6.791 data anime yang telah dibersihkan dan disiapkan sebelumnya.

2. Anime Uji (Testing Input)
- Anime yang dijadikan acuan: "Kimi no Na wa.", sebuah film drama romantis dengan elemen school dan supernatural.

3. 10 Rekomendasi Teratas
- Model merekomendasikan anime lain yang memiliki kemiripan genre dan tipe dengan anime input.

- Beberapa rekomendasi yang muncul:

  - "Aura: Maryuuin Kouga Saigo no Tatakai" dan "Kokoro ga Sakebitagatterunda.", sama-sama bertema drama, romance, school dan berjenis Movie.

  - "Clannad Movie" dan "Air Movie" juga direkomendasikan karena kesamaan nuansa emosional dan genre.

- Nilai similarity_score menunjukkan seberapa mirip kontennya dengan anime input, dengan skor tertinggi 0.96.

**Kesimpulan**

- Sistem content-based berhasil merekomendasikan anime yang secara konten mirip dengan "Kimi no Na wa.", terutama dari sisi tema, genre, dan tipe (Movie).

- Hasil ini menunjukkan bahwa model cukup efektif dalam mengenali pola konten yang disukai pengguna.

## COLLABORATIVE FILTERING
Model & Dataset
- Dibuat user-item matrix sintetis sebagai dasar collaborative filtering.

- Model dilatih menggunakan 1000 pengguna dan 6791 anime.

- Teknik yang digunakan adalah SVD (Singular Value Decomposition), umum untuk collaborative filtering.

Pengujian (Testing)
- Dilakukan pengujian untuk User ID 0.

- Sistem menghasilkan 10 rekomendasi anime teratas berdasarkan prediksi kesukaan pengguna terhadap anime lain.

10 Rekomendasi Teratas
- Rekomendasi mencakup berbagai genre populer, seperti:

  - Tonari no Kaibutsu-kun (romance, school)

  - Suzumiya Haruhi no Yuuutsu (mystery, school, sci-fi)

  - Angel Beats!, Kuroko no Basket, Bakemonogatari, dan Code Geass R2 — anime populer yang secara historis banyak disukai.

- Kolom predicted_rating menunjukkan skor prediksi sistem, yang merepresentasikan seberapa besar kemungkinan pengguna akan menyukai anime tersebut.

  - Skor tertinggi: ~3.71, yang menunjukkan preferensi relatif dibandingkan item lain (bukan skala 1–10).

Kesimpulan
- Collaborative filtering mampu menghasilkan rekomendasi yang dipersonalisasi berdasarkan pola rating pengguna lain.

- Rekomendasi yang muncul umumnya terdiri dari anime dengan rating tinggi dan jumlah members besar, yang menunjukkan model cenderung mengutamakan anime populer namun relevan.

- Meskipun tidak memperhatikan konten langsung, pendekatan ini efektif untuk mengenali pola kesukaan pengguna yang mirip.

# 6. EVALUATION
### 1. Evaluasi Content-Based Filtering
- Coverage: 0.0673

  - Artinya, hanya sekitar 6.73% (457 dari 6791 anime) yang berhasil direkomendasikan oleh model.

  - Coverage rendah umum terjadi di content-based filtering karena model hanya merekomendasikan anime yang mirip dengan yang sudah dikenal.

- Success Rate: 1.0000

  - Semua rekomendasi berhasil diberikan untuk user yang diuji (tidak ada error saat mencocokkan konten).

  - Angka 1.0000 menunjukkan bahwa sistem selalu dapat memberikan rekomendasi sesuai input kontennya.

- Total Recommendations: 500

  - Jumlah total rekomendasi yang dihasilkan selama evaluasi.

### 2.  Evaluasi Collaborative Filtering
- RMSE: 7.5269

  - Root Mean Square Error (RMSE) digunakan untuk mengukur selisih antara rating sebenarnya dan prediksi sistem.

  - RMSE 7.52 cukup tinggi, tapi hal ini bisa terjadi karena:

    - Dataset memiliki rating dalam skala kecil tapi nilai prediksi dalam skala berbeda.

    - Bisa juga karena rating aslinya sparse atau noise cukup besar.

- Number of test ratings: 1268

  - Jumlah pasangan user-anime yang digunakan untuk menguji model collaborative filtering.

  - Angka ini menunjukkan ukuran data uji yang dipakai menghitung RMSE.

 Kesimpulan Sementara
- Content-based filtering: Stabil dan selalu berhasil merekomendasikan, tapi cakupannya terbatas.

- Collaborative filtering: Lebih luas secara potensi rekomendasi, tapi prediksinya masih bisa ditingkatkan (RMSE tinggi).

# 7. FINAL RECOMMENDATIONS DEMO
#### Rekomendasi untuk Anime: 'Death Note'
1.  Content-Based Filtering:

Berikut 10 anime yang mirip dengan Death Note berdasarkan kesamaan genre dan tipe:

- Mousou Dairinin – Drama psikologis penuh misteri dan supranatural (Rating: 7.74)

- Death Note Rewrite – Versi alternatif dari Death Note dengan nuansa serupa (Rating: 7.84)

- Higurashi no Naku Koro ni Kai – Thriller misteri dan supranatural (Rating: 8.41)

- Mirai Nikki (TV) – Aksi dan psikologi yang tegang dengan tema kematian (Rating: 8.07)

- Higurashi no Naku Koro ni Rei – Gabungan misteri dan humor gelap (Rating: 7.56)

- Monster – Kisah kriminal psikologis intens (Rating: 8.72)

- Higurashi no Naku Koro ni – Atmosfer horor dan penuh teka-teki (Rating: 8.17)

- Mirai Nikki: Ura Mirai Nikki – Tambahan cerita untuk Mirai Nikki (Rating: 6.79)

- Zankyou no Terror – Tema psikologis dan ketegangan (Rating: 8.26)

- Shigofumi – Drama fantasi dengan sentuhan kematian dan emosional (Rating: 7.62)

2. Collaborative Filtering:

Rekomendasi berdasarkan kesamaan preferensi pengguna (user-based):

Tonari no Kaibutsu-kun – Komedi romantis sekolah (Rating: 7.77)

- Suzumiya Haruhi no Yuuutsu – Campuran misteri dan fiksi ilmiah sekolah (Rating: 8.06)

- Claymore – Aksi fantasi gelap dengan unsur supranatural (Rating: 7.92)

- Gintama – Komedi dan aksi parodi (Rating: 9.04)

- Dragon Ball Z – Pertarungan epik penuh aksi klasik (Rating: 8.32)

- Angel Beats! – Cerita sekolah penuh drama dan kehidupan setelah mati (Rating: 8.39)

- Kuroko no Basket – Anime olahraga dengan elemen persaingan seru (Rating: 8.46)

- Log Horizon – Dunia virtual dan petualangan fantasi (Rating: 8.14)

- Bakemonogatari – Dialog cepat dan atmosfer supernatural (Rating: 8.39)

- Code Geass R2 – Konflik politik dan kekuatan super (Rating: 8.98)

✅ Kesimpulan Akhir Proyek
Sistem rekomendasi anime berhasil dibangun dengan dua pendekatan utama:

1. Content-Based Filtering
Menggunakan informasi konten seperti genre dan tipe anime untuk menemukan kesamaan antar anime.

2. Collaborative Filtering
Mengandalkan perilaku rating pengguna (user-item matrix) untuk memprediksi preferensi berdasarkan pola rating.

Keduanya saling melengkapi: content-based cocok untuk pengguna baru, sedangkan collaborative bekerja baik dengan data rating yang cukup.
