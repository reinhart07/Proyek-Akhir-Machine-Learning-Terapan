# Laporan Proyek Machine Learning - Reinhart Jens Robert
## Project Overview
Industri hiburan digital, khususnya anime, telah mengalami pertumbuhan yang signifikan dalam beberapa tahun terakhir. Dengan ribuan judul anime yang tersedia di berbagai platform streaming, pengguna sering menghadapi kesulitan dalam menemukan anime yang sesuai dengan preferensi mereka. Fenomena "choice overload" ini dapat mengurangi kepuasan pengguna dan engagement pada platform.
Sistem rekomendasi telah terbukti efektif dalam mengatasi masalah ini dengan menyediakan saran yang dipersonalisasi berdasarkan preferensi dan perilaku pengguna. Netflix melaporkan bahwa 80% konten yang ditonton pengguna berasal dari sistem rekomendasi mereka, yang menunjukkan pentingnya teknologi ini dalam industri entertainment.
Proyek ini bertujuan untuk mengembangkan sistem rekomendasi anime yang dapat membantu pengguna menemukan anime baru berdasarkan karakteristik konten (content-based filtering) dan preferensi pengguna serupa (collaborative filtering). Implementasi kedua pendekatan ini akan memberikan rekomendasi yang lebih komprehensif dan akurat.

## Business Understanding
### Problem Statements

1. Information Overload: Pengguna menghadapi kesulitan dalam menemukan anime yang sesuai dengan preferensi mereka dari ribuan judul yang tersedia, yang dapat menyebabkan frustrasi dan mengurangi engagement.
2. Personalisasi Rekomendasi: Platform anime membutuhkan sistem yang dapat memberikan rekomendasi yang dipersonalisasi berdasarkan karakteristik anime (genre, tipe) dan perilaku pengguna sebelumnya.
3. Cold Start Problem: Bagaimana memberikan rekomendasi yang relevan untuk anime baru yang belum memiliki banyak rating atau untuk pengguna baru yang belum memiliki riwayat rating.

### Goals

1. Mengembangkan sistem rekomendasi content-based yang dapat merekomendasikan anime berdasarkan kesamaan karakteristik konten seperti genre dan tipe anime.
2. Mengimplementasikan sistem collaborative filtering yang dapat memberikan rekomendasi berdasarkan preferensi pengguna dengan pola rating yang serupa.
3. Menghasilkan Top-N recommendations yang akurat dan relevan untuk meningkatkan pengalaman pengguna dalam menemukan anime baru.

### Solution Statements

1. Content-Based Filtering menggunakan TF-IDF dan Cosine Similarity: Sistem ini akan menganalisis fitur konten anime (genre, tipe) menggunakan TF-IDF vectorization dan menghitung kesamaan menggunakan cosine similarity untuk memberikan rekomendasi berdasarkan karakteristik anime yang disukai pengguna.
2. Collaborative Filtering menggunakan User-User Similarity: Sistem ini akan menggunakan cosine similarity untuk menemukan pengguna dengan preferensi serupa dan memberikan rekomendasi berdasarkan anime yang disukai oleh pengguna serupa tersebut.

## Data Understading
Dataset yang digunakan dalam proyek ini terdiri dari dua file CSV:

- anime.csv: Berisi informasi tentang anime
- rating.csv: Berisi rating yang diberikan pengguna untuk anime

Dataset ini berasal dari:
📌 https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

Variabel-variabel pada dataset adalah sebagai berikut:
Dataset Anime (anime.csv):

- anime_id: ID unik untuk setiap anime
- name: Nama anime
- genre: Genre anime (dapat berupa multiple genre yang dipisahkan koma)
- type: Tipe anime (TV, Movie, OVA, etc.)
- episodes: Jumlah episode
- rating: Rating rata-rata anime
- members: Jumlah anggota komunitas untuk anime tersebut

Dataset Rating (rating.csv):

- user_id: ID unik untuk setiap pengguna
- anime_id: ID anime yang dirating
- rating: Rating yang diberikan pengguna (skala 1-10, -1 untuk tidak dirating)

  Kondisi Data Awal
1. anime.csv:

- Jumlah data: 12.294 baris, 7 kolom yaitu anime_id, name, genre, type, episodes, rating, members.

- Missing values:
  - genre: 62 nilai kosong
  - type: 25 nilai kosong
  - rating: 230 nilai kosong

Kondisi Data Awal 
2.  rating.csv
- Jumlah baris: 1.963.739, 3 kolom yaitu user_id, anime_id, dan rating
- Tidak ada nilai kosong

**Dataset Rating:**

Terdapat dua versi data rating yang digunakan dalam analisis:

1. **Data Rating Lengkap**:
   - Jumlah baris: 7.813.737
   - Jumlah kolom: 3
   - Kolom: user_id, anime_id, rating

2. **Data Rating yang Digunakan untuk Analisis**:
   - Jumlah baris: 1.967.911  
   - Jumlah kolom: 3
   - Kolom: user_id, anime_id, rating
   - Keterangan: [Subset dari data lengkap/file terpisah]

Untuk keperluan analisis dan efisiensi komputasi, digunakan dataset rating dengan 1.967.911 baris.


### Exploratory Data Analysis:
Dari analisis eksploratori data, diperoleh insight sebagai berikut:

- Distribusi rating anime cenderung normal dengan puncak sekitar rating 7-8
- Tipe anime didominasi oleh TV series (sekitar 60%), diikuti Movie dan OVA
- Genre paling populer adalah Comedy, Action, dan Drama
- Distribusi rating dari user menunjukkan bias positif, dengan kebanyakan - pengguna memberikan rating tinggi (8-10)
- Matrix sparsity sangat tinggi (99.98%), yang merupakan tantangan umum dalam collaborative filtering

Statistik Dataset:

- Jumlah anime unik: 12294
- Jumlah user unik: 19094
- Total rating: 1967911
- Rata-rata rating per anime: 160.07
- Rata-rata rating per user: 103.06

## Data Preparation

- Missing values pada rating anime: 230 anime tidak memiliki rating, dihapus karena diperlukan untuk content-based filtering
- Missing values pada genre: Diisi dengan 'Unknown' untuk menjaga konsistensi data
- Alasan: Rating dan genre adalah fitur penting untuk sistem rekomendasi, sehingga data yang tidak lengkap dapat mempengaruhi kualitas rekomendasi

- Rating -1: Menghapus 373148 rating dengan nilai -1 yang menandakan pengguna tidak memberikan rating
- Alasan: Rating -1 tidak memberikan informasi preferensi yang berguna untuk collaborative filtering



- Common anime IDs: Memastikan hanya anime yang ada di kedua dataset yang digunakan
- Final dataset: 9000 anime dan 1594762 rating
- Alasan: Konsistensi data penting untuk menghindari error saat melakukan join antar dataset

- Standardisasi format: Mengubah genre menjadi format lowercase dan mengganti spasi dengan underscore
- Alasan: TF-IDF vectorizer memerlukan format teks yang konsisten untuk hasil yang optimal

Fitur baru bernama `content_features` dibuat dengan menggabungkan informasi dari `genre` dan `type`. Fitur ini diproses dengan lowercasing, penghapusan spasi, dan digabungkan sebagai satu string untuk mewakili konten setiap anime.

Dilakukan filtering untuk meningkatkan kualitas data:
- Hanya menyertakan anime yang memiliki setidaknya 20 rating dari user.
- Hanya menyertakan user yang memberikan setidaknya 50 rating.

User-item matrix dibentuk dari data rating yang sudah difilter. Matriks ini digunakan sebagai input untuk Collaborative Filtering berbasis algoritma k-Nearest Neighbors.

#### Transformasi Fitur Teks untuk Content-Based Filtering

Untuk membangun sistem Content-Based Filtering, dilakukan penggabungan kolom `genre` dan `type` menjadi fitur baru bernama `content_features`. Kolom ini menyimpan informasi deskriptif tentang anime yang akan digunakan dalam pemodelan berbasis konten.

Selanjutnya, `content_features` diubah menjadi representasi numerik menggunakan **TF-IDF Vectorizer**. Teknik ini mengubah teks menjadi vektor berdasarkan frekuensi kata, dengan mengurangi bobot kata-kata umum (stopwords). Parameter `max_features=5000` digunakan untuk membatasi jumlah fitur.

Hasil akhir dari proses ini adalah **TF-IDF matrix**, yaitu representasi vektor dari setiap anime berdasarkan kontennya. Matrix ini akan digunakan dalam perhitungan cosine similarity pada algoritma Content-Based Filtering.


## Modeling
### 1. Content-Based Filtering

Model Content-Based Filtering memanfaatkan hasil transformasi `content_features` (yang telah diubah menjadi vektor melalui TF-IDF) untuk menghitung kemiripan antar anime berdasarkan cosine similarity. Dengan demikian, sistem dapat merekomendasikan anime yang mirip dengan anime yang disukai user.

#### Contoh Hasil Rekomendasi:

Berikut adalah contoh Top-5 rekomendasi anime berdasarkan input anime *"Death Note"*:

1. Otaku no Seiza  
2. Lupin Shanshei  
3. Mobile Police Patlabor: MiniPato 
4. Scramble Wars: Tsuppashire! Genom Trophy Rally  
5. CB Chara Go Nagai World

#### Kelebihan:
- Tidak memerlukan data user lain (mengatasi cold start untuk user baru)
- Dapat menjelaskan mengapa suatu anime direkomendasikan
- Tidak bergantung pada sparsity rating

#### Kekurangan:
- Terbatas pada fitur yang tersedia (genre, type)
- Kurang mampu menangkap preferensi kompleks
- Rentan terhadap over-specialization


### 2. Collaborative Filtering (User-User)

Model Collaborative Filtering ini menggunakan pendekatan berbasis user-user similarity. Setelah data rating difilter (anime minimal dirating 20 user, user minimal memberi 50 rating), sistem membentuk **user-item matrix**. Kemudian, digunakan algoritma k-Nearest Neighbors (kNN) untuk mencari user yang memiliki pola rating serupa.

Dari user serupa ini, sistem merekomendasikan anime yang disukai user lain tapi belum pernah ditonton oleh user target.

#### Contoh Hasil Rekomendasi:

Berikut contoh top-5 rekomendasi anime untuk user dengan ID **12345**:

1. Kimi no Na wa. 
2. Gintama°  
3. Ginga Eiyuu Densetsu  
4.  Steins;Gate  
5.  Hunter x Hunter (2011)

#### Kelebihan:
- Mampu menangkap preferensi pengguna yang kompleks
- Rekomendasi bersifat personal

#### Kekurangan:
- Mengalami masalah cold start untuk user baru
- Performa tergantung pada jumlah data interaksi yang tersedia

## Keluaran untuk Content-Based Filtering dan Collaborative Filtering tidak bisa memiliki format yang sama dalam hal menampilkan "Predicted Rating"/"Similarity Score" Kenapa?
 karena kedua model menghasilkan jenis output yang berbeda:

Content-Based Filtering: Model ini menghitung kesamaan (similarity) antara anime berdasarkan fitur-fitur kontennya (genre, tipe). Outputnya adalah skor yang menunjukkan seberapa mirip anime rekomendasi dengan anime yang menjadi input. Model ini tidak memprediksi rating yang mungkin diberikan user terhadap anime rekomendasi. Oleh karena itu, kolom yang relevan untuk ditampilkan adalah similarity_score.

Collaborative Filtering: Model ini memprediksi rating yang mungkin diberikan seorang user terhadap anime yang belum ditonton, berdasarkan preferensi user lain yang serupa. Outputnya adalah nilai prediksi rating (predicted rating). Oleh karena itu, kolom yang relevan untuk ditampilkan adalah predicted_rating.

Menggunakan "Predicted Rating" untuk output Content-Based Filtering akan menyebabkan error karena kolom tersebut memang tidak ada dalam hasil rekomendasi Content-Based Filtering. Setiap model memberikan informasi yang berbeda, sehingga format tampilan outputnya pun perlu disesuaikan dengan informasi yang diberikan oleh model tersebut.

Content-Based = Similarity (kemiripan fitur)

Collaborative = Prediction (prediksi preferensi user)
Ini konsep fundamental yang berbeda:

- CBF: "Anime ini mirip dengan yang kamu suka"
- CF: "Kamu akan suka anime ini dengan rating X"

### Top-N Recommendation Output:
Kedua sistem berhasil menghasilkan top-5 recommendations:

- Content-Based: Merekomendasikan anime dengan genre serupa dengan "Death Note"
- Collaborative Filtering: Merekomendasikan anime berdasarkan preferensi pengguna serupa

Top 5 hasil rekomendasi Content-Based Filtering anime dengan genre serupa dengan "Death Note":
1. Otaku no Seiza
2. Lupin Shanshei
3. Mobile Police Patlabor: MiniPato
4. Scramble Wars: Tsuppashire! Genom Trophy Rally
5. CB Chara Go Nagai World

Top 5 hasil rekomendasi Collaborative Filtering untuk user 3:
1.  Kimi no Na wa.
2. Gintama°
3. Ginga Eiyuu Densetsu
4. Steins;Gate
5. Hunter x Hunter (2011)


## Evaluation
### 1. Content-Based Filtering
Precision berdasarkan Genre Similarity:

      Precision = (Jumlah rekomendasi dengan genre serupa) / (Total rekomendasi)

- Hasil: Average Precision = 0.6667
- Interpretasi: 66% rekomendasi memiliki setidaknya satu genre yang sama dengan anime referensi

Diversity Score:
      Diversity = (Jumlah genre unik) / (Total rekomendasi)

- Hasil: Diversity Score = 0.0877
- Interpretasi: Sistem dapat memberikan variasi genre yang cukup baik

### 2. COLLABORATIVE FILTERING EVALUATION
Root Mean Square Error (RMSE):

    RMSE = √(Σ(actual_rating - predicted_rating)² / n)

- Hasil: RMSE = 1.3178
- Interpretasi: Rata-rata error prediksi adalah 1.71 poin pada skala 1-10

Mean Absolute Error (MAE):
    MAE = Σ|actual_rating - predicted_rating| / n

- Hasil: MAE = 1.0320
- Interpretasi: Rata-rata absolut error adalah 1.03 poin

### Coverage Analysis
**Content-Based Coverage:** 73.21% (9,000/12,294 anime)

- Dapat memberikan rekomendasi untuk mayoritas anime dalam dataset

**Collaborative Filtering Coverage:**

- Anime Coverage: 35.85% (4.407/12,294 anime)
- User Coverage: 44.36% (8471/19,094 users)
- Coverage rendah karena filtering untuk mengurangi sparsity

================================================================================
EVALUATION SUMMARY
================================================================================

1. CONTENT-BASED FILTERING:
   ✓ Dapat memberikan rekomendasi berdasarkan konten anime
   ✓ Coverage: 73.21% dari total anime
   ✓ Average Precision: 0.6667
   ✓ Diversity Score: 0.0877

2. COLLABORATIVE FILTERING:
   ✓ Dapat memberikan rekomendasi berdasarkan preferensi user serupa
   ✓ Anime Coverage: 35.85%
   ✓ User Coverage: 44.36%
   ✓ RMSE: 1.3178
   ✓ MAE: 1.0320

3. SYSTEM CHARACTERISTICS:
   • Total Anime in Dataset: 12,294
   • Total Users: 19,094
   • Total Ratings: 1,967,911
   • Matrix Sparsity: 96.25%

4. RECOMMENDATION CAPABILITIES:
   • Content-based: Merekomendasikan anime dengan genre/karakteristik serupa
   • Collaborative: Merekomendasikan anime berdasarkan user dengan preferensi serupa
   • Kedua sistem dapat memberikan Top-N recommendations

## Kesimpulan:
Kedua sistem memberikan pendekatan yang complementary. Content-based filtering unggul dalam coverage dan mengatasi cold start, sedangkan collaborative filtering memberikan rekomendasi berdasarkan preferensi komunitas. Implementasi hybrid system dapat menggabungkan kelebihan kedua pendekatan untuk hasil yang optimal.

