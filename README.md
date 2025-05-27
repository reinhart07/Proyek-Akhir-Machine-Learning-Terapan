# Laporan Proyek Akhir Machine Learning Terapan - Sistem Rekomendasi Anime

## Business Understanding

### Problem Statements
1. Bagaimana membangun sistem rekomendasi anime berdasarkan kemiripan konten seperti genre?
2. Bagaimana membangun sistem rekomendasi berdasarkan perilaku pengguna lain yang memiliki kesamaan preferensi?
3. Bagaimana mengevaluasi performa sistem rekomendasi yang dibangun?

### Goals
1. Mengembangkan sistem rekomendasi berbasis konten (Content-Based Filtering).
2. Mengembangkan sistem rekomendasi berbasis kolaboratif (Collaborative Filtering).
3. Mengukur performa model menggunakan metrik evaluasi seperti RMSE.

## Solution Approach
Untuk menjawab tujuan proyek, pendekatan berikut digunakan:

1. Content-Based Filtering
Sistem akan merekomendasikan anime berdasarkan kemiripan konten, seperti genre, type (TV, OVA, movie), dan jumlah episode. Pendekatan ini memanfaatkan teknik TF-IDF dan cosine similarity untuk mengukur kemiripan antar anime berdasarkan genre-nya.

**Kelebihan:**

- Tidak tergantung pada aktivitas pengguna lain.

- Cocok untuk pengguna baru (cold-start user problem).

**Kekurangan:**

- Rekomendasi cenderung terbatas pada konten yang mirip.

- Kurang adaptif terhadap perubahan selera pengguna.

2. Collaborative Filtering

Menggunakan pendekatan user-based collaborative filtering, sistem mencari pengguna lain dengan preferensi yang mirip untuk memberikan rekomendasi.

**Kelebihan:**

- Rekomendasi lebih bervariasi dan personal.

- Bisa menemukan anime yang di luar preferensi eksplisit pengguna.

**Kekurangan:**


- Tidak bekerja optimal untuk pengguna baru atau item yang belum pernah dirating (cold-start item problem).

- Butuh data rating yang cukup banyak dan bersih.
---

## Data Understanding

### Dataset
Sumber data terdiri dari dua file utama:

- `anime.csv`: berisi metadata tentang anime seperti judul, genre, rating, jumlah member, dll.
- `rating.csv`: berisi data rating dari pengguna terhadap anime.

**Sumber**: [Kaggle - Anime Recommendation Database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

### Jumlah Data
- `anime.csv`: 12.294 baris × 7 kolom
- `rating.csv`: 7.813.737 baris × 3 kolom

### Pemeriksaan Data
- **Missing values**:
  - `anime.csv`: terdapat nilai kosong pada kolom `genre`, `episodes`, dan `rating`.
  - `rating.csv`: tidak memiliki missing values, namun terdapat rating dengan nilai `-1` yang dianggap noise.
- **Duplikat**: tidak ditemukan data duplikat.
- **Outlier**: rating `-1` dianggap sebagai noise dan dihapus saat preprocessing.

### Deskripsi Fitur

#### anime.csv

| Kolom      | Deskripsi                                     |
|------------|-----------------------------------------------|
| anime_id   | ID unik untuk setiap anime                    |
| name       | Nama anime                                    |
| genre      | Genre dari anime                              |
| type       | Jenis anime (TV, Movie, OVA, dll.)            |
| episodes   | Jumlah episode                                |
| rating     | Rata-rata rating dari pengguna                |
| members    | Jumlah pengguna yang menyimpan anime ke daftar|

#### rating.csv

| Kolom    | Deskripsi                                            |
|----------|------------------------------------------------------|
| user_id  | ID unik pengguna                                     |
| anime_id | ID anime yang dirating                               |
| rating   | Nilai rating dari pengguna (nilai -1 = belum dirating)|

---

## Data Preparation

### Alasan Preprocessing
1. Membersihkan rating tidak valid (nilai `-1`).
2. Mengisi genre kosong agar dapat diolah menggunakan TF-IDF.
3. Melakukan filtering user dan anime untuk mengurangi sparsity dan meningkatkan performa.
4. Melakukan penggabungan dataset jika dibutuhkan (misalnya pada Collaborative Filtering).

### Content-Based Filtering
- Genre diolah dengan TF-IDF setelah di-preprocess.
- Genre kosong diisi `'Unknown'`.
- Token genre diubah menjadi lowercase dan mengganti spasi dengan underscore.

```python
def preprocess_genre(genre_str):
    if pd.isna(genre_str) or genre_str == 'Unknown':
        return 'unknown'
    genres = [g.strip().lower().replace(' ', '_') for g in genre_str.split(',')]
    return ' '.join(genres)

Collaborative Filtering
Data rating difilter:

Hanya mempertahankan anime yang memiliki minimal 50 rating.

Hanya mempertahankan pengguna yang memberi lebih dari 10 rating.

Digunakan untuk melatih model SVD dari library Surprise.

Modeling and Results
1. Content-Based Filtering
Genre diolah dengan TF-IDF Vectorizer.

Kemiripan antar anime dihitung menggunakan cosine similarity.

Sistem memberikan rekomendasi anime berdasarkan kemiripan genre.

Contoh Output Rekomendasi untuk Death Note:

name                      genre  \
1. Otaku no Seiza  =         Comedy, Parody   
2. Lupin Shanshei = Comedy, Parody
3. Mobile Police Patlabor: MiniPato = Parody
4. Scramble Wars: Tsuppashire! Genom Trophy Rally = Parody
5. CB Chara Go Nagai World = Action, Comedy, Parody

2. Collaborative Filtering
Model: Singular Value Decomposition (SVD) dari library Surprise.

Data dibagi menjadi training dan testing set.

Model dilatih untuk memprediksi rating pengguna.

Contoh Output Rekomendasi untuk user_id = 3:


Anime	Predicted Rating

- Kimi no Na wa.	9.37

- Gintama°	9.25

- Ginga Eiyuu Densetsu	9.11

- Steins;Gate	9.17

- Hunter x Hunter (2011)	9.13

# Evaluation

Evaluasi dilakukan untuk menilai performa sistem rekomendasi berdasarkan dua pendekatan.

1. Content-Based Filtering
- Anime Coverage: 73.21% dari total anime

- Average Precision: 0.6667

- Diversity Score: 0.0877

Metode ini berhasil mencakup lebih dari 70% anime yang tersedia dan memiliki precision yang cukup baik. Diversity Score mengindikasikan variasi rekomendasi, meskipun masih cenderung rendah (karena kesamaan genre).

2. Collaborative Filtering
- Anime Coverage: 35.85%

- User Coverage: 44.36%

- RMSE: 1.3178

- MAE: 1.0320

RMSE dan MAE menunjukkan tingkat kesalahan prediksi rating. Nilai RMSE 1.3178 dan MAE 1.0320 cukup umum dalam domain ini dan bisa ditingkatkan dengan pendekatan hybrid atau model yang lebih kompleks.


# KESIMPULAN
Dalam proyek ini, dua pendekatan sistem rekomendasi telah berhasil dikembangkan:

- Content-Based Filtering memiliki cakupan lebih luas terhadap koleksi anime dan precision yang tinggi, namun variasi rekomendasinya masih terbatas.

- Collaborative Filtering memberikan rekomendasi berdasarkan preferensi pengguna serupa, dengan performa prediksi yang cukup akurat (RMSE = 1.3178).

Kedua sistem dapat menghasilkan Top-N recommendation yang relevan. Ke depan, sistem ini dapat dikembangkan dengan:

- Pendekatan Hybrid yang menggabungkan keunggulan kedua metode.

- Integrasi fitur tambahan seperti sinopsis, review teks, atau skor popularitas.

- Peningkatan diversity agar rekomendasi lebih bervariasi dan tidak hanya fokus pada genre yang sama.


