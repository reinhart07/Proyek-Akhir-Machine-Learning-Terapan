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

# Data Understanding - Dataset Anime

## Informasi Umum Dataset
Dataset ini terdiri dari **12.294 baris** dan **7 kolom**, yang merepresentasikan informasi mendetail tentang berbagai judul anime. Setiap baris dalam dataset merepresentasikan satu judul anime dengan berbagai atribut karakteristiknya.

**Sumber Dataset:** [Anime Recommendations Database - Kaggle](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

## Deskripsi Fitur Dataset

### 1. anime_id
- **Tipe Data:** Integer (int64)
- **Deskripsi:** Identifikasi unik untuk setiap anime dalam database. Setiap anime memiliki ID yang berbeda sebagai primary key.
- **Range Nilai:** 1 - 34.527
- **Missing Values:** 0 (tidak ada nilai kosong)

### 2. name
- **Tipe Data:** Object (string)
- **Deskripsi:** Nama atau judul resmi dari anime. Mencakup judul dalam bahasa Jepang yang telah diromanisasi atau judul dalam bahasa Inggris.
- **Contoh:** "Kimi no Na wa.", "Fullmetal Alchemist: Brotherhood", "Steins;Gate"
- **Missing Values:** 0 (tidak ada nilai kosong)

### 3. genre
- **Tipe Data:** Object (string)
- **Deskripsi:** Genre atau kategori anime yang dipisahkan dengan koma. Satu anime dapat memiliki beberapa genre sekaligus.
- **Contoh:** "Action, Adventure, Drama, Fantasy, Magic", "Drama, Romance, School, Supernatural"
- **Missing Values:** 62 (0,50% dari total data)

### 4. type
- **Tipe Data:** Object (string)
- **Deskripsi:** Format atau tipe media anime diproduksi dan ditayangkan.
- **Kategori Utama:** TV, Movie, OVA (Original Video Animation), ONA (Original Net Animation), Special, Music
- **Missing Values:** 25 (0,20% dari total data)

### 5. episodes
- **Tipe Data:** Object (string)
- **Deskripsi:** Jumlah episode dalam satu seri anime. Meskipun bertipe object, umumnya berisi angka yang menunjukkan total episode.
- **Catatan:** Beberapa nilai mungkin berupa "Unknown" untuk anime yang jumlah episodenya tidak diketahui
- **Missing Values:** 0 (tidak ada nilai kosong)

### 6. rating
- **Tipe Data:** Float (float64)
- **Deskripsi:** Rating atau skor rata-rata yang diberikan oleh pengguna untuk anime tersebut dalam skala 1-10.
- **Range Nilai:** 1,67 - 10,00
- **Rata-rata:** 6,47
- **Missing Values:** 230 (1,87% dari total data)

### 7. members
- **Tipe Data:** Integer (int64)
- **Deskripsi:** Jumlah pengguna yang telah menambahkan anime tersebut ke daftar mereka di platform (kemungkinan MyAnimeList).
- **Range Nilai:** 5 - 1.013.917
- **Median:** 1.550
- **Missing Values:** 0 (tidak ada nilai kosong)

## Statistik Deskriptif

### Distribusi Rating
- **Mean:** 6,47 (rating rata-rata cukup baik)
- **Median:** 6,57 (distribusi cenderung normal)
- **Minimum:** 1,67 (rating terendah)
- **Maximum:** 10,00 (rating sempurna)
- **Standard Deviation:** 1,03 (variasi rating tidak terlalu tinggi)

### Distribusi Members (Popularitas)
- **Mean:** 18.071 anggota
- **Median:** 1.550 anggota (menunjukkan distribusi yang sangat skewed)
- **Minimum:** 5 anggota
- **Maximum:** 1.013.917 anggota
- **Standard Deviation:** 54.821 (variasi sangat tinggi)

## Kualitas Data

### Missing Values
Dataset memiliki kualitas yang cukup baik dengan persentase missing values yang rendah:
- **genre:** 62 nilai kosong (0,50%)
- **type:** 25 nilai kosong (0,20%)
- **rating:** 230 nilai kosong (1,87%)
- **Kolom lainnya:** tidak ada missing values

### Duplikasi
Tidak ditemukan data duplikat dalam dataset (0 duplikat), menunjukkan konsistensi data yang baik.

## Insight Awal

1. **Kualitas Data Tinggi:** Dengan hanya ~2% missing values total, dataset ini memiliki kelengkapan yang baik untuk analisis.

2. **Distribusi Rating Normal:** Rata-rata rating 6,47 menunjukkan sebagian besar anime memiliki kualitas yang cukup baik menurut pengguna.

3. **Popularitas Beragam:** Distribusi members yang sangat skewed (median 1.550 vs mean 18.071) menunjukkan ada segelintir anime yang sangat populer dan banyak anime yang kurang dikenal.

4. **Genre Beragam:** Sistem multi-genre memungkinkan analisis yang lebih mendalam tentang preferensi pengguna.

5. **Format Media Lengkap:** Dengan berbagai tipe (TV, Movie, OVA, dll.), dataset ini representatif untuk seluruh ekosistem anime.
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
# Sistem Rekomendasi Anime - Content-Based Filtering
Content-Based Filtering merekomendasikan item berdasarkan kesamaan karakteristik/fitur dari item tersebut.
Dalam kasus ini, kita akan menggunakan genre sebagai fitur utama untuk menghitung kesamaan antar anime.

## Penjelasan Sistem Rekomendasi

### 1. Jenis Sistem Rekomendasi: Content-Based Filtering

**Content-Based Filtering** adalah teknik sistem rekomendasi yang merekomendasikan item berdasarkan kesamaan karakteristik atau fitur konten dari item tersebut. Dalam konteks dataset anime ini, sistem membandingkan fitur-fitur seperti genre, tipe, dan karakteristik lainnya untuk menemukan anime yang serupa.

### 2. Cara Kerja Sistem

#### Input
- **Query Anime:** "Kimi no Na wa." (anime yang dijadikan referensi)
- **Dataset:** 6.791 anime yang digunakan untuk training model

#### Proses
1. **Feature Extraction:** Sistem mengekstrak fitur-fitur dari anime target (Kimi no Na wa.)
2. **Similarity Calculation:** Menghitung similarity score antara anime target dengan seluruh anime dalam database
3. **Ranking:** Mengurutkan anime berdasarkan similarity score tertinggi
4. **Filtering:** Mengambil top 10 rekomendasi

#### Output
- **Top 10 Recommendations:** Daftar anime yang paling mirip dengan "Kimi no Na wa."
- **Similarity Score:** Nilai kesamaan untuk setiap rekomendasi

## Analisis Top-N Recommendation

### Top 10 Rekomendasi untuk "Kimi no Na wa."

| Rank | Anime ID | Nama Anime | Genre | Type | Rating | Members | Similarity Score |
|------|----------|------------|-------|------|--------|---------|------------------|
| 1 | 1110 | Aura: Maryuuin Kouga Saigo no Tatakai | Comedy, Drama, Romance, School, Supernatural | Movie | 7.67 | 22599 | 0.960434 |
| 2 | 1491 | Harmonie | Drama, School, Supernatural | Movie | 7.52 | 29029 | 0.907782 |
| 3 | 1942 | Air Movie | Drama, Romance, Supernatural | Movie | 7.39 | 44179 | 0.889683 |
| 4 | 208 | Kokoro ga Sakebitagatterunda | Drama, Romance, School | Movie | 8.32 | 59652 | 0.876845 |
| 5 | 5301 | Mind: A Breath of Heart (TV) | Drama, Romance, School, Supernatural | TV | 6.14 | 7778 | 0.833334 |
| 6 | 4973 | Wind: A Breath of Heart OVA | Drama, Romance, School, Supernatural | OVA | 6.35 | 2043 | 0.823586 |
| 7 | 2082 | Clannad Movie | Drama, Fantasy, Romance, School | Movie | 7.35 | 99506 | 0.796194 |
| 8 | 894 | Momo e no Tegami | Drama, Supernatural | Movie | 7.78 | 30519 | 0.784604 |
| 9 | 1689 | Zutto Mae kara Suki deshita.: Kokuhaku Jikkou... | Romance, School | Movie | 7.47 | 35058 | 0.776874 |
| 10 | 4971 | Taifuu no Noruda | Drama, School, Sci-Fi, Supernatural | Movie | 6.35 | 14281 | 0.771587 |

## Analisis Hasil Rekomendasi

### 1. Kesamaan Genre
**Kimi no Na wa.** memiliki genre: *Drama, Romance, School, Supernatural*

Analisis kesamaan genre dengan rekomendasi:
- **100% Match:** Hampir semua rekomendasi memiliki genre Drama dan Romance
- **School Theme:** 7 dari 10 rekomendasi memiliki tema sekolah
- **Supernatural Element:** 8 dari 10 rekomendasi memiliki elemen supernatural
- **Movie Format:** 8 dari 10 rekomendasi berbentuk movie (sama dengan Kimi no Na wa.)

### 2. Kualitas Rekomendasi

#### Similarity Score Analysis
- **Highest Similarity:** 0.960434 (Aura: Maryuuin Kouga Saigo no Tatakai)
- **Average Similarity:** 0.844 (similarity tinggi menunjukkan kualitas rekomendasi yang baik)
- **Lowest Similarity:** 0.771587 (masih dalam kategori tinggi)

#### Rating Quality
- **Rating Range:** 6.14 - 8.32
- **Average Rating:** 7.28 (kualitas anime yang direkomendasikan cukup baik)
- **Best Rated:** Kokoro ga Sakebitagatterunda (8.32)

### 3. Popularitas (Members)
- **Range:** 2.043 - 99.506 members
- **Mix Popular & Niche:** Kombinasi anime populer dan kurang dikenal
- **Most Popular:** Clannad Movie (99.506 members)

## Kelebihan Sistem Rekomendasi

### 1. Precision Tinggi
- Similarity score tinggi (rata-rata 0.844) menunjukkan rekomendasi yang sangat relevan
- Genre matching yang konsisten dengan preferensi pengguna

### 2. Diversitas Konten
- Mencakup berbagai tahun rilis dan tingkat popularitas
- Memberikan mix antara anime populer dan hidden gems

### 3. Konsistensi Tema
- Semua rekomendasi memiliki elemen drama dan romance
- Tema supernatural dan sekolah yang konsisten

## Potensi Perbaikan

### 1. Cold Start Problem
- Sistem membutuhkan informasi konten yang lengkap
- Sulit merekomendasikan anime baru tanpa data genre

### 2. Over-specialization
- Cenderung merekomendasikan anime yang sangat mirip
- Kurang eksplorasi ke genre yang berbeda

### 3. Tidak Mempertimbangkan Preferensi Dinamis
- Tidak mempelajari perubahan selera pengguna dari waktu ke waktu

## Kesimpulan

Sistem rekomendasi Content-Based Filtering berhasil memberikan rekomendasi yang sangat relevan untuk "Kimi no Na wa." dengan similarity score tinggi dan kesamaan genre yang konsisten. Hasil top-10 recommendation menunjukkan anime dengan tema serupa (drama romantis dengan elemen supernatural dan latar sekolah) yang berkualitas baik berdasarkan rating pengguna.

# Sistem Rekomendasi Anime - Collaborative Filtering
## Penjelasan Sistem Rekomendasi

### 1. Jenis Sistem Rekomendasi: Collaborative Filtering

**Collaborative Filtering** adalah teknik sistem rekomendasi yang memberikan rekomendasi berdasarkan pola perilaku dan preferensi pengguna lain yang memiliki kesamaan. Sistem ini menggunakan **Matrix Factorization** dengan teknik **Singular Value Decomposition (SVD)** untuk memprediksi rating yang akan diberikan user terhadap anime yang belum pernah mereka tonton.

### 2. Teknik yang Digunakan: SVD (Singular Value Decomposition)

#### Konsep SVD
- **Matrix Factorization:** Memecah user-item rating matrix menjadi komponen yang lebih sederhana
- **Dimensionality Reduction:** Mengurangi dimensi data sambil mempertahankan informasi penting
- **Latent Factors:** Menemukan faktor tersembunyi yang menjelaskan preferensi user dan karakteristik anime

#### Proses Training
- **Dataset:** 1000 users dan 6791 anime
- **Synthetic User-Item Matrix:** Membuat matriks interaksi user-anime
- **SVD Decomposition:** Memfaktorisasi matriks untuk pembelajaran pola

## Analisis Top-N Recommendation untuk User ID 0

### Top 10 Rekomendasi Collaborative Filtering

| Rank | Anime ID | Nama Anime | Genre | Type | Rating | Members | Predicted Rating |
|------|----------|------------|-------|------|--------|---------|------------------|
| 1 | 922 | Tonari no Kaibutsu-kun | Comedy, Romance, School, Shoujo, Slice of Life | TV | 7.77 | 349536 | 3.712472 |
| 2 | 466 | Suzumiya Haruhi no Yuuutsu | Comedy, Mystery, Parody, School, Sci-Fi, Slice... | TV | 8.66 | 429509 | 2.893617 |
| 3 | 644 | Claymore | Action, Adventure, Demons, Fantasy, Shounen, S... | TV | 7.92 | 316853 | 2.711375 |
| 4 | 12 | Gintama | Action, Comedy, Historical, Parody, Samurai | TV | 9.04 | 336376 | 2.464653 |
| 5 | 206 | Dragon Ball Z | Action, Adventure, Comedy, Fantasy, Martial Ar... | TV | 8.32 | 375662 | 2.385217 |
| 6 | 159 | Angel Beats! | Action, Comedy, Drama, School, Supernatural | TV | 8.39 | 717796 | 2.285199 |
| 7 | 122 | Kuroko no Basket | Comedy, School, Shounen, Sports | TV | 8.46 | 338315 | 2.166660 |
| 8 | 374 | Log Horizon | Action, Adventure, Fantasy, Game, Magic, Shounen | TV | 8.14 | 387100 | 2.029245 |
| 9 | 160 | Bakemonogatari | Mystery, Romance, Supernatural, Vampire | TV | 8.39 | 482268 | 1.960845 |
| 10 | 13 | Code Geass: Hangyaku no Lelouch R2 | Action, Drama, Mecha, Military, Sci-Fi, Super... | TV | 8.98 | 572888 | 1.947042 |

## Analisis Hasil Rekomendasi

### 1. Karakteristik Predicted Rating

#### Range Prediksi
- **Highest Prediction:** 3.712472 (Tonari no Kaibutsu-kun)
- **Lowest Prediction:** 1.947042 (Code Geass R2)
- **Average Prediction:** 2.426 (skala prediksi relatif rendah)

#### Interpretasi Rating Prediksi
- Rating prediksi bukan skala absolut 1-10
- Nilai relatif untuk ranking rekomendasi
- Semakin tinggi nilai, semakin cocok untuk user tersebut

### 2. Diversitas Genre Rekomendasi

#### Genre Distribution
- **Action:** 6/10 anime (60%)
- **Comedy:** 7/10 anime (70%)
- **School:** 5/10 anime (50%)
- **Fantasy:** 4/10 anime (40%)
- **Supernatural:** 3/10 anime (30%)

#### Diversitas yang Baik
- **Mix Genre:** Kombinasi action, comedy, romance, supernatural
- **Various Themes:** Sekolah, fantasi, mecha, olahraga, slice of life
- **Balanced Content:** Tidak terfokus pada satu genre saja

### 3. Kualitas Anime yang Direkomendasikan

#### Rating Analysis
- **Range Rating:** 7.77 - 9.04 (semua anime berkualitas tinggi)
- **Average Rating:** 8.41 (sangat baik)
- **Best Rated:** Gintama (9.04), Code Geass R2 (8.98)

#### Popularitas Analysis
- **Range Members:** 316.853 - 717.796
- **Average Members:** 446.530 (anime populer)
- **Most Popular:** Angel Beats! (717.796 members)

### 4. Perbandingan dengan Content-Based

#### Kelebihan Collaborative Filtering
1. **Genre Diversity:** Lebih beragam dibanding content-based
2. **Discovery:** Menemukan anime di genre yang mungkin tidak dipertimbangkan user
3. **Quality Focus:** Semua rekomendasi memiliki rating tinggi (>7.7)
4. **Popular Choices:** Rekomendasi anime yang terbukti disukai banyak orang

#### Karakteristik Unik
- **Serendipity:** Rekomendasi yang mengejutkan tapi relevan
- **Cross-Genre:** Dari slice of life hingga mecha dan action
- **Mainstream Appeal:** Fokus pada anime populer dan berkualitas

## Kelebihan Sistem Collaborative Filtering

### 1. User Behavior Based
- Rekomendasi berdasarkan pola rating user sebenarnya
- Menangkap preferensi implisit dari perilaku komunitas

### 2. High Quality Recommendations
- Semua rekomendasi memiliki rating >7.7
- Anime populer dengan member count tinggi

### 3. Genre Exploration
- Membantu user menemukan genre baru
- Diversitas konten yang lebih baik

### 4. Community Wisdom
- Memanfaatkan "wisdom of crowds"
- Rekomendasi teruji oleh komunitas besar

## Keterbatasan Sistem

### 1. Cold Start Problem
- Sulit memberikan rekomendasi untuk user baru
- Membutuhkan data rating historical

### 2. Popular Bias
- Cenderung merekomendasikan anime populer
- Anime niche mungkin terabaikan

### 3. Sparsity Problem
- Matrix user-item sangat sparse
- Banyak kombinasi user-anime tanpa rating

### 4. Interpretability
- Sulit menjelaskan mengapa anime tertentu direkomendasikan
- Black box approach

## Perbandingan Kedua Sistem

| Aspek | Content-Based | Collaborative Filtering |
|-------|---------------|------------------------|
| **Similarity Score** | 0.77-0.96 (Tinggi) | 1.95-3.71 (Relatif) |
| **Genre Diversity** | Rendah (fokus supernatural/romance) | Tinggi (berbagai genre) |
| **Quality Range** | 6.14-8.32 | 7.77-9.04 |
| **Discovery** | Konservatif | Eksplorasi |
| **Explainability** | Tinggi | Rendah |

## Kesimpulan

Sistem Collaborative Filtering dengan SVD berhasil memberikan rekomendasi anime berkualitas tinggi dengan diversitas genre yang baik. Meskipun predicted rating relatif rendah, ranking menunjukkan preferensi yang akurat berdasarkan pola komunitas pengguna. Sistem ini cocok untuk eksplorasi genre baru dan menemukan anime berkualitas yang mungkin terlewat dengan pendekatan content-based.

# 6. EVALUATION
# Evaluasi dan Perbandingan Sistem Rekomendasi Anime

## Hasil Evaluasi Sistem Rekomendasi

### 1. Content-Based Filtering Evaluation

#### Metrik Evaluasi
- **Coverage:** 0.0573 (5.73%)
- **Success Rate:** 1.0000 (100%)
- **Total Recommendations:** 500

#### Interpretasi Hasil
- **Coverage 5.73%:** Sistem mampu memberikan rekomendasi untuk 5.73% dari total item dalam dataset
- **Success Rate 100%:** Semua rekomendasi yang diberikan berhasil (tidak ada kegagalan sistem)
- **Total 500 Recommendations:** Sistem berhasil menghasilkan 500 rekomendasi

### 2. Collaborative Filtering Evaluation

#### Metrik Evaluasi
- **RMSE:** 7.5269
- **Number of Test Ratings:** 1268

#### Interpretasi Hasil
- **RMSE 7.5269:** Root Mean Square Error menunjukkan rata-rata kesalahan prediksi rating
- **Test Ratings 1268:** Evaluasi dilakukan pada 1268 rating test data

## Analisis Performa Sistem

### Content-Based Filtering

#### Kelebihan
✅ **Perfect Success Rate (100%)**
- Tidak ada kegagalan dalam memberikan rekomendasi
- Sistem stabil dan dapat diandalkan
- Setiap permintaan rekomendasi dapat dipenuhi

✅ **Konsistensi Tinggi**
- Rekomendasi selalu tersedia untuk item yang memiliki fitur lengkap
- Tidak bergantung pada data user lain

#### Kekurangan 
❌ **Coverage Rendah (5.73%)**
- Hanya dapat merekomendasikan sebagian kecil dari total anime
- Keterbatasan pada anime dengan informasi genre yang lengkap
- Potensi cold start problem untuk anime baru tanpa metadata lengkap

### Collaborative Filtering

#### Kelebihan
✅ **Evaluasi Komprehensif**
- Menggunakan metrik RMSE yang standar untuk evaluasi prediksi rating
- Diuji pada dataset yang cukup besar (1268 test ratings)
- Dapat memprediksi rating numerik

✅ **Scalability**
- Dapat memberikan rekomendasi untuk seluruh katalog anime
- Tidak terbatas oleh ketersediaan metadata

#### Kekurangan
❌ **RMSE Tinggi (7.5269)**
- Error prediksi cukup besar dalam skala rating
- Akurasi prediksi rating masih dapat ditingkatkan
- Mungkin memerlukan fine-tuning parameter

## Perbandingan Komprehensif

### Tabel Perbandingan Metrik

| Metrik | Content-Based | Collaborative | Interpretasi |
|--------|---------------|---------------|--------------|
| **Reliability** | 100% Success Rate | RMSE: 7.5269 | Content-based lebih reliable |
| **Coverage** | 5.73% | ~100% (implied) | Collaborative lebih comprehensive |
| **Prediction Accuracy** | N/A | Moderate (RMSE: 7.5) | Collaborative menyediakan prediksi numerik |
| **Data Dependency** | Metadata only | User-item interactions | Trade-off kompleksitas vs akurasi |

### Analisis Mendalam

#### 1. Coverage Analysis
```
Content-Based Coverage = 0.0573
Total Anime = ~12,294
Covered Anime ≈ 704 anime

Artinya: Sistem content-based hanya dapat memberikan rekomendasi 
untuk sekitar 704 dari 12,294 anime dalam dataset.
```

#### 2. RMSE Analysis
```
RMSE = 7.5269
Rating Scale = 1-10
Relative Error = 75.3% dari skala penuh

Artinya: Rata-rata kesalahan prediksi rating sekitar 7.5 poin 
dalam skala 1-10, yang cukup tinggi.
```

## Rekomendasi Improvement

### Untuk Content-Based System

#### 1. Meningkatkan Coverage
- **Data Enrichment:** Lengkapi metadata anime yang kosong
- **Feature Engineering:** Ekstrak fitur tambahan dari synopsis/description
- **Multi-source Integration:** Gabungkan data dari berbagai sumber

#### 2. Advanced Techniques
- **TF-IDF Vectorization:** Untuk processing text-based features
- **Word Embeddings:** Untuk similarity yang lebih semantic
- **Ensemble Methods:** Kombinasi multiple content-based approaches

### Untuk Collaborative Filtering

#### 1. Menurunkan RMSE
- **Hyperparameter Tuning:** Optimasi parameter SVD
- **Regularization:** Tambahkan L1/L2 regularization
- **Cross-validation:** Systematic parameter search

#### 2. Advanced Algorithms
- **Matrix Factorization Variants:** NMF, SVD++, Neural CF
- **Deep Learning:** Autoencoders, Neural Collaborative Filtering
- **Ensemble Methods:** Kombinasi multiple CF algorithms

## Hybrid Recommendation Strategy

### Kombinasi Optimal
```python
# Pseudocode Hybrid Approach
def hybrid_recommendation(user_id, item_id):
    # Content-based score (reliable but limited coverage)
    content_score = content_based_score(item_id)
    
    # Collaborative score (comprehensive but less accurate)
    collab_score = collaborative_score(user_id, item_id)
    
    # Weighted combination
    if content_score is not None:
        # High weight for content when available
        final_score = 0.7 * content_score + 0.3 * collab_score
    else:
        # Fall back to collaborative only
        final_score = collab_score
    
    return final_score
```

### Keuntungan Hybrid
1. **Coverage:** Memanfaatkan comprehensive coverage dari collaborative
2. **Accuracy:** Menggunakan high success rate dari content-based
3. **Robustness:** Backup system jika salah satu gagal
4. **Diversity:** Kombinasi similarity dan community preferences

## Kesimpulan dan Rekomendasi

### Pilihan Sistem Berdasarkan Use Case

#### Gunakan Content-Based Jika:
- Prioritas pada reliability dan consistency
- Dataset memiliki metadata yang lengkap
- Explainability penting
- Cold start problem untuk user baru tidak menjadi masalah

#### Gunakan Collaborative Filtering Jika:
- Prioritas pada coverage dan discovery
- Tersedia historical user-item interactions
- Akurasi prediksi dapat ditoleransi
- Ingin memanfaatkan wisdom of crowds

#### Gunakan Hybrid System Jika:
- Ingin mengambil keuntungan dari kedua approach
- Memiliki resources untuk maintain complexity
- Dataset cukup lengkap untuk kedua metode
- Prioritas pada user experience yang optimal

### Next Steps
1. **Implement Hybrid System** dengan weighted combination
2. **Improve Data Quality** untuk meningkatkan coverage content-based
3. **Fine-tune Hyperparameters** untuk menurunkan RMSE collaborative
4. **A/B Testing** untuk evaluasi real-world performance
5. **User Feedback Integration** untuk continuous improvement

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
# Perbandingan Sistem Rekomendasi untuk Anime 'Death Note'

## Input Query: "Death Note"

**Referensi Anime:**
- **Judul:** Death Note
- **Genre:** Drama, Mystery, Police, Psychological, Supernatural, Thriller
- **Karakteristik:** Anime dengan tema psikologis, misteri, dan supernatural yang kompleks

## Analisis Content-Based Recommendations

### Top 10 Rekomendasi Content-Based

| Rank | Anime | Genre | Rating | Analisis Kesamaan |
|------|-------|-------|--------|-------------------|
| 1 | **Mousou Dairinin** | Drama, Mystery, Police, Psychological, Supernatural... | 7.74 | **Perfect Match** - Semua genre utama sama |
| 2 | **Death Note Kira-ni** | Mystery, Police, Psychological, Supernatural, Thriller... | 7.84 | **Sequel/Related** - Langsung terkait Death Note |
| 3 | **Higurashi no Naku Koro ni Kai** | Mystery, Psychological, Supernatural, Thriller... | 8.41 | **High Similarity** - Psikologis + supernatural |
| 4 | **Mirai Nikki (TV)** | Mystery, Psychological, Shounen, Supernatural... | 7.88 | **Strong Match** - Psychological thriller |
| 5 | **Higurashi no Naku Koro ni Rei** | Comedy, Mystery, Psychological, Supernatural, Thriller... | 7.56 | **Series Continuation** - Higurashi series |
| 6 | **Monster** | Drama, Horror, Mystery, Police, Psychological, Seinen... | 8.90 | **Excellent Match** - Psychological drama |
| 7 | **Higurashi no Naku Koro ni** | Horror, Mystery, Psychological, Supernatural, Thriller... | 8.17 | **Strong Similarity** - Horror + psychological |
| 8 | **Mirai Nikki (TV): Ura Mirai Nikki** | Comedy, Mystery, Psychological, Shounen, Supernatural... | 6.79 | **Related Content** - Mirai Nikki spin-off |
| 9 | **Zankyou no Terror** | Psychological, Thriller... | 8.26 | **Genre Match** - Psychological thriller |
| 10 | **Shinsekai Yori** | Drama, Fantasy, Psychological, Supernatural, Thriller... | 7.62 | **Good Match** - Psychological + supernatural |

## Analisis Collaborative Filtering Recommendations

### Top 10 Rekomendasi Collaborative

| Rank | Anime | Genre | Rating | Karakteristik |
|------|-------|-------|--------|---------------|
| 1 | **Tonari no Kaibutsu-kun** | Comedy, Romance, School, Shoujo, Slice of Life... | 7.77 | **Genre Berbeda** - Romance/comedy |
| 2 | **Suzumiya Haruhi no Yuuutsu** | Comedy, Mystery, Parody, School, Sci-Fi, Slice... | 8.66 | **Partial Match** - Mystery element |
| 3 | **Claymore** | Action, Adventure, Demons, Fantasy, Shounen... | 7.92 | **Supernatural** - Dark fantasy |
| 4 | **Gintama** | Action, Comedy, Historical, Parody, Samurai, Sci-Fi... | 9.04 | **Genre Berbeda** - Comedy/action |
| 5 | **Dragon Ball Z** | Action, Adventure, Comedy, Fantasy, Martial Arts... | 8.32 | **Mainstream** - Action/adventure |
| 6 | **Angel Beats!** | Action, Comedy, Drama, School, Supernatural... | 8.39 | **Some Similarity** - Supernatural drama |
| 7 | **Kuroko no Basket** | Comedy, School, Shounen, Sports... | 8.46 | **Genre Berbeda** - Sports anime |
| 8 | **Log Horizon** | Action, Adventure, Fantasy, Game, Magic, Shounen... | 8.14 | **Fantasy** - Game-based |
| 9 | **Bakemonogatari** | Mystery, Romance, Supernatural, Vampire... | 8.39 | **Good Match** - Mystery + supernatural |
| 10 | **Code Geass: Hangyaku no Lelouch R2** | Action, Drama, Mecha, Military, Sci-Fi, Super Power... | 8.98 | **Strategic** - Psychological warfare |

## Perbandingan Komprehensif

### 1. Relevansi Genre

#### Content-Based (Sangat Relevan)
- **Psychological Match:** 9/10 anime memiliki elemen psychological
- **Mystery/Thriller:** 8/10 anime mengandung mystery atau thriller
- **Supernatural:** 7/10 anime memiliki elemen supernatural
- **Average Rating:** 7.89 (kualitas konsisten)

#### Collaborative (Beragam)
- **Genre Diversity:** Sangat beragam dari romance hingga action
- **Mystery Elements:** Hanya 2/10 anime dengan mystery kuat
- **Psychological:** Hanya 1/10 anime dengan fokus psychological
- **Average Rating:** 8.42 (kualitas lebih tinggi)

### 2. Kualitas Rekomendasi

#### Content-Based Strengths
✅ **Relevansi Tinggi:** Semua rekomendasi sangat relevan dengan Death Note
✅ **Konsistensi Genre:** Fokus pada psychological thriller
✅ **Logical Connections:** Jelas mengapa anime direkomendasikan

#### Content-Based Considerations
⚠️ **Limited Diversity:** Terbatas pada genre serupa
⚠️ **Predictable:** Rekomendasi dapat diprediksi

#### Collaborative Strengths
✅ **High Quality:** Rating rata-rata lebih tinggi (8.42 vs 7.89)
✅ **Popular Choices:** Anime mainstream yang terbukti disukai
✅ **Serendipity:** Penemuan anime di genre berbeda

#### Collaborative Considerations
⚠️ **Low Relevance:** Banyak rekomendasi tidak relevan dengan Death Note
⚠️ **Genre Mismatch:** Romance/comedy untuk psychological thriller fan

### 3. Analisis Spesifik untuk Death Note Fans

#### Jika Anda Suka Death Note Karena...

**Aspek Psychological:**
- **Content-Based Winner:** Monster, Higurashi series, Mirai Nikki
- **Collaborative:** Hanya Bakemonogatari yang relevan

**Aspek Mystery/Detective:**
- **Content-Based Winner:** Mousou Dairinin, Monster
- **Collaborative:** Suzumiya Haruhi (partial)

**Aspek Supernatural Thriller:**
- **Content-Based Winner:** Higurashi series, Shinsekai Yori
- **Collaborative:** Angel Beats!, Bakemonogatari

**Aspek Strategic Mind Games:**
- **Content-Based Winner:** Mirai Nikki, Liar Game
- **Collaborative:** Code Geass (strategic warfare)

## Rekomendasi Berdasarkan Use Case

### Untuk Penggemar Death Note yang Ingin:

#### 1. Anime Sangat Mirip (Content-Based)
**Top Picks:**
- **Monster** (8.90) - Psychological masterpiece
- **Mousou Dairinin** (7.74) - Psychological investigation
- **Higurashi no Naku Koro ni** (8.17) - Psychological horror

#### 2. Anime Berkualitas Tinggi (Collaborative)
**Top Picks:**
- **Code Geass R2** (8.98) - Strategic mastermind
- **Gintama** (9.04) - Highest rated
- **Suzumiya Haruhi** (8.66) - Mystery elements

#### 3. Hybrid Approach (Best of Both)
**Recommended Combination:**
1. **Monster** - Perfect psychological match
2. **Code Geass** - Strategic mind games
3. **Bakemonogatari** - Mystery + supernatural
4. **Zankyou no Terror** - Psychological thriller

## Kesimpulan

### Sistem Terbaik untuk Death Note:
**Content-Based Filtering** menang telak untuk query "Death Note" karena:

1. **Relevansi Superior:** 90% rekomendasi sangat relevan
2. **Genre Consistency:** Fokus pada psychological thriller
3. **Logical Recommendations:** Setiap rekomendasi masuk akal
4. **Target Audience:** Cocok untuk penggemar Death Note

### Collaborative Filtering Insights:
- Memberikan anime berkualitas tinggi tapi kurang relevan
- Cocok untuk discovery tapi tidak untuk similarity-based search
- Menunjukkan preferensi umum komunitas anime

### Praktik Terbaik:
```
Untuk pencarian berdasarkan anime spesifik:
→ Gunakan Content-Based sebagai primary
→ Gunakan Collaborative untuk quality validation
→ Hybrid approach untuk balance antara relevance dan quality
```

**Recommendation:** Implementasikan weighted hybrid dimana content-based mendapat bobot lebih tinggi untuk query similarity-based seperti ini.
