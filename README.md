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

Informasi Dataset:

- Dataset Anime: 12,294 rows × 7 columns
- Dataset Rating: 7,813,737 rows × 3 columns

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

## Modeling
### 1. Content-Based Filtering
Algoritma yang digunakan:

TF-IDF Vectorization: Mengubah fitur teks (genre dan tipe) menjadi vektor numerik
Cosine Similarity: Menghitung kesamaan antar anime berdasarkan vektor TF-IDF

Cara Kerja:
python

    class ContentBasedRecommender:

    def fit(self):

        tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
        self.tfidf_matrix = tfidf.fit_transform(self.anime_df['content_features'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

Kelebihan:

- Tidak memerlukan data user lain (mengatasi cold start problem untuk user baru)
- Dapat memberikan penjelasan mengapa anime direkomendasikan
- Tidak terpengaruh oleh sparsity data rating

Kekurangan:

- Terbatas pada fitur yang tersedia (genre, tipe)
- Tidak dapat menemukan pola preferensi yang complex
- Rentan terhadap over-specialization

### 2. Collaborative Filtering (User-User)
Algoritma yang digunakan:

- User-User Similarity: Menghitung kesamaan antar pengguna menggunakan cosine similarity
- Weighted Average Prediction: Prediksi rating berdasarkan rating dari pengguna serupa

Cara Kerja:

python

    def get_user_recommendations(self, user_id, n_recommendations=10):
          # Hitung similarity antar user
          user_sim_scores = self.user_similarity[user_idx]
          
          # Prediksi rating dengan weighted average
          predicted_rating = numerator / denominator

Kelebihan:

- Dapat menemukan pola preferensi yang complex
- Memanfaatkan wisdom of crowds
- Tidak memerlukan analisis konten yang mendalam

Kekurangan:

- Memerlukan data rating yang cukup (cold start problem)
- Komputasi intensive untuk dataset besar
- Terpengaruh oleh sparsity data

### Top-N Recommendation Output:
Kedua sistem berhasil menghasilkan top-5 recommendations:

- Content-Based: Merekomendasikan anime dengan genre serupa dengan "Death Note"
- Collaborative Filtering: Merekomendasikan anime berdasarkan preferensi pengguna serupa

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

