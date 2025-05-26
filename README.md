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

### Solution Statements
- Untuk Content-Based Filtering, digunakan representasi teks genre dengan TF-IDF dan cosine similarity.
- Untuk Collaborative Filtering, digunakan pendekatan matrix factorization (SVD).
- Evaluasi dilakukan menggunakan metrik RMSE.

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

Evaluation
Content-Based Filtering
Tidak dapat dievaluasi dengan metrik prediktif seperti RMSE.

Evaluasi dilakukan secara visual dan logis berdasarkan kesamaan genre.

Rekomendasi terlihat cukup relevan dan sesuai dengan konten.

Collaborative Filtering
Evaluasi menggunakan RMSE (Root Mean Squared Error).

Hasil evaluasi:

ini
Copy code
RMSE = 1.3178
Nilai ini menunjukkan bahwa prediksi model cukup akurat (semakin kecil RMSE semakin baik).

Kesimpulan
Sistem rekomendasi berhasil dibangun menggunakan dua pendekatan:

Content-Based Filtering menggunakan genre anime.

Collaborative Filtering menggunakan teknik matrix factorization (SVD).

Content-Based menghasilkan rekomendasi yang relevan secara konten.

Collaborative Filtering memberikan prediksi rating dengan RMSE 1.3178.

Sistem dapat dikembangkan lebih lanjut menggunakan pendekatan hybrid untuk menggabungkan kedua metode dan meningkatkan performa sistem rekomendasi.
