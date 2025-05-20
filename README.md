# Sistem Rekomendasi Anime

Proyek machine learning ini membangun sistem rekomendasi anime menggunakan pendekatan content-based filtering dan collaborative filtering untuk membantu pengguna menemukan anime yang sesuai dengan preferensi mereka.

## Overview Proyek

Sistem rekomendasi telah menjadi komponen penting dalam platform digital seperti MyAnimeList, Netflix, dan Crunchyroll. Dengan ribuan judul anime yang tersedia, sistem rekomendasi membantu pengguna menemukan konten yang relevan dengan selera mereka. Proyek ini mengimplementasikan dua pendekatan sistem rekomendasi dan membandingkan hasilnya untuk memberikan rekomendasi anime yang optimal.

## Latar Belakang

Industri animasi dan manga global bernilai sekitar $25 miliar pada tahun 2020 dan terus berkembang. Permintaan untuk anime secara global meningkat 33% antara 2020-2021. Sistem rekomendasi yang efektif dapat:

- Membantu pengguna menemukan anime yang sesuai dengan preferensi mereka
- Meningkatkan pengalaman dan retensi pengguna pada platform anime
- Memperluas wawasan pengguna dengan merekomendasikan anime yang mungkin tidak mereka temukan sendiri
- Memaksimalkan efisiensi konsumsi konten

## Problem Statements

1. Pengguna kesulitan menemukan anime yang sesuai preferensi mereka di antara ribuan judul yang tersedia
2. Jumlah anime baru yang terus bertambah membuat pengguna kewalahan dan menghabiskan waktu tidak efisien
3. Platform anime menghadapi tantangan untuk mempertahankan dan meningkatkan user retention

## Goals

1. Mengembangkan sistem rekomendasi anime yang sesuai dengan preferensi pengguna
2. Mengimplementasikan dan membandingkan dua pendekatan sistem rekomendasi
3. Mengukur dan mengevaluasi performa dari kedua pendekatan sistem rekomendasi

## Dataset

Dataset berasal dari Kaggle, terdiri dari dua file:

1. **Anime Dataset (anime.csv)**:
   - `anime_id`: ID unik untuk setiap anime
   - `name`: Judul anime
   - `genre`: Genre anime yang dipisahkan dengan koma
   - `type`: Format anime (TV, Movie, OVA, dll)
   - `episodes`: Jumlah episode anime
   - `rating`: Rating rata-rata anime pada skala 1-10
   - `members`: Jumlah anggota komunitas yang telah menambahkan anime ke daftar mereka

2. **Rating Dataset (rating.csv)**:
   - `user_id`: ID unik untuk setiap pengguna
   - `anime_id`: ID anime yang sesuai dengan anime dataset
   - `rating`: Rating yang diberikan pengguna (skala 1-10, nilai -1 menandakan anime yang ditonton tetapi tidak diberi rating)

Dataset dapat diakses di: [Anime Recommendations Database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

## Pendekatan

### 1. Content-based Filtering

- Menganalisis konten atau atribut dari anime yang disukai pengguna
- Menggunakan fitur seperti genre, tipe, dan rating sebagai basis
- Mengimplementasikan teknik TF-IDF untuk fitur genre
- Menggunakan cosine similarity untuk menghitung kesamaan antar anime

### 2. Collaborative Filtering

- Merekomendasikan anime berdasarkan preferensi pengguna lain dengan pola rating serupa
- Menggunakan matrix factorization dengan teknik Singular Value Decomposition (SVD)
- Membangun model dengan library Surprise

### 3. Hybrid Approach

- Menggabungkan kedua pendekatan dengan pembobotan
- Menyeimbangkan kelebihan kedua metode untuk rekomendasi optimal

## Hasil Evaluasi

### Content-based Filtering

- Berhasil merekomendasikan anime dengan genre serupa dengan anime referensi
- Transparansi dalam menjelaskan rekomendasi

### Collaborative Filtering

- RMSE: 1.1431
- MAE: 0.8625
- Akurasi prediksi cukup baik (nilai kompetitif dalam skala industri)

### Hybrid Approach

- Menunjukkan performa yang lebih baik dalam keragaman dan ketepatan rekomendasi
- Mengkompensasi kekurangan masing-masing pendekatan individual

## Kesimpulan

- Content-based Filtering efektif merekomendasikan anime dengan karakteristik serupa, tetapi terbatas pada fitur yang tersedia
- Collaborative Filtering lebih akurat dalam memprediksi preferensi pengguna dan menemukan rekomendasi implisit
- Pendekatan hybrid memberikan hasil terbaik dengan menggabungkan kelebihan kedua metode

## Pengembangan Masa Depan

- Menambahkan fitur seperti sinopsis anime, studio produksi, atau informasi karakter
- Mengimplementasikan pendekatan deep learning (neural collaborative filtering)
- Mengembangkan context-aware recommendation system
- Menambahkan real-time feedback dan explanation engine
- Melakukan A/B testing dengan pengguna nyata

## Requirements

```
numpy==1.26.4
pandas
matplotlib
seaborn
scikit-learn
surprise
```

## Cara Penggunaan

1. Clone repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Jalankan notebook atau script Python:
   ```
   python proyek_akhir_machine_learning_terapan.py
   ```

## Author

Reinhart Jens Robert
