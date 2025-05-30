# -*- coding: utf-8 -*-
"""Proyek_Akhir_Machine_Learning_Terapan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oIXXWtP2x3WX4EcRayOZQoZyiyut_J35

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
"""

### Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Set style untuk visualisasi
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

"""## Data Understading"""

# Load dataset anime dan rating
anime_df = pd.read_csv('/content/anime.csv')
rating_df = pd.read_csv('/content/rating.csv')

print("Dataset Anime:")
print(f"Shape: {anime_df.shape}")
print(f"Columns: {anime_df.columns.tolist()}")
print("\nDataset Rating:")
print(f"Shape: {rating_df.shape}")
print(f"Columns: {rating_df.columns.tolist()}")

"""Dataset yang digunakan dalam proyek ini terdiri dari dua file CSV:

- anime.csv: Berisi informasi tentang anime
- rating.csv: Berisi rating yang diberikan pengguna untuk anime



Dataset ini berasal dari:
📌 https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database
"""

# Informasi dasar dataset anime
print("=== INFORMASI DATASET ANIME ===")
print(anime_df.info())
print("\n=== STATISTIK DESKRIPTIF ===")
print(anime_df.describe())

# Informasi dasar dataset rating
print("\n=== INFORMASI DATASET RATING ===")
print(rating_df.info())
print("\n=== STATISTIK DESKRIPTIF ===")
print(rating_df.describe())

"""

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
- rating: Rating yang diberikan pengguna (skala 1-10, -1 untuk tidak dirating)"""

# Cek missing values
print("\n=== MISSING VALUES ===")
print("Anime dataset:")
print(anime_df.isnull().sum())
print("\nRating dataset:")
print(rating_df.isnull().sum())

# Cek duplikasi
print(f"\nDuplikasi di anime dataset: {anime_df.duplicated().sum()}")
print(f"Duplikasi di rating dataset: {rating_df.duplicated().sum()}")

# Sample data
print("\n=== SAMPLE DATA ANIME ===")
print(anime_df.head())
print("\n=== SAMPLE DATA RATING ===")
print(rating_df.head())

"""Kondisi Data Awal
1. anime.csv:

- Jumlah data: 12.294 baris, 7 kolom yaitu anime_id, name, genre, type, episodes, rating, members.

- Missing values:
  - genre: 62 nilai kosong
  - type: 25 nilai kosong
  - rating: 230 nilai kosong

Kondisi Data Awal
2.  rating.csv
- Jumlah baris: 7813737, 3 kolom yaitu user_id, anime_id, dan rating
- Terdapat 1 nilai kosong

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
"""

# Setup untuk subplot
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Distribusi rating anime
axes[0,0].hist(anime_df['rating'].dropna(), bins=30, alpha=0.7, edgecolor='black')
axes[0,0].set_title('Distribusi Rating Anime')
axes[0,0].set_xlabel('Rating')
axes[0,0].set_ylabel('Frekuensi')

# 2. Distribusi type anime
type_counts = anime_df['type'].value_counts()
axes[0,1].pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%')
axes[0,1].set_title('Distribusi Type Anime')

# 3. Top 10 genre
# Ekstrak genre dan hitung frekuensi
all_genres = []
for genres in anime_df['genre'].dropna():
    if isinstance(genres, str):
        genre_list = [g.strip() for g in genres.split(',')]
        all_genres.extend(genre_list)

genre_counts = pd.Series(all_genres).value_counts().head(10)
axes[1,0].barh(genre_counts.index[::-1], genre_counts.values[::-1])
axes[1,0].set_title('Top 10 Genre Anime')
axes[1,0].set_xlabel('Frekuensi')

# 4. Distribusi user rating
axes[1,1].hist(rating_df['rating'], bins=20, alpha=0.7, edgecolor='black')
axes[1,1].set_title('Distribusi Rating dari User')
axes[1,1].set_xlabel('Rating')
axes[1,1].set_ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Statistik tambahan
print("=== STATISTIK TAMBAHAN ===")
print(f"Jumlah anime unik: {anime_df['anime_id'].nunique()}")
print(f"Jumlah user unik: {rating_df['user_id'].nunique()}")
print(f"Total rating: {len(rating_df)}")
print(f"Rata-rata rating per anime: {len(rating_df) / anime_df['anime_id'].nunique():.2f}")
print(f"Rata-rata rating per user: {len(rating_df) / rating_df['user_id'].nunique():.2f}")

"""### Exploratory Data Analysis:
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
"""

# 1. Handle missing values pada dataset anime
print("=== HANDLING MISSING VALUES ===")

# Cek missing values pada kolom rating dan genre
print(f"Missing values di kolom 'rating': {anime_df['rating'].isnull().sum()}")
print(f"Missing values di kolom 'genre': {anime_df['genre'].isnull().sum()}")

# Drop anime dengan rating kosong untuk content-based filtering
anime_clean = anime_df.dropna(subset=['rating']).copy()
print(f"Shape setelah drop missing rating: {anime_clean.shape}")

# Fill missing genre dengan 'Unknown'
anime_clean['genre'] = anime_clean['genre'].fillna('Unknown')

"""- Missing values pada rating anime: 230 anime tidak memiliki rating, dihapus karena diperlukan untuk content-based filtering
- Missing values pada genre: Diisi dengan 'Unknown' untuk menjaga konsistensi data
- Alasan: Rating dan genre adalah fitur penting untuk sistem rekomendasi, sehingga data yang tidak lengkap dapat mempengaruhi kualitas rekomendasi
"""

# 2. Handle rating -1 pada dataset rating (menandakan user tidak memberikan rating)
print(f"\nRating -1 dalam dataset: {(rating_df['rating'] == -1).sum()}")

# Filter rating yang valid (1-10)
rating_clean = rating_df[rating_df['rating'] != -1].copy()
print(f"Shape rating setelah filter: {rating_clean.shape}")

"""- Rating -1: Menghapus 373148 rating dengan nilai -1 yang menandakan pengguna tidak memberikan rating
- Alasan: Rating -1 tidak memberikan informasi preferensi yang berguna untuk collaborative filtering
"""

# 3. Filter anime yang ada di kedua dataset
common_anime_ids = set(anime_clean['anime_id']).intersection(set(rating_clean['anime_id']))
anime_final = anime_clean[anime_clean['anime_id'].isin(common_anime_ids)].copy()
rating_final = rating_clean[rating_clean['anime_id'].isin(common_anime_ids)].copy()

print(f"Anime setelah filter common IDs: {anime_final.shape}")
print(f"Rating setelah filter common IDs: {rating_final.shape}")

"""

- Common anime IDs: Memastikan hanya anime yang ada di kedua dataset yang digunakan
- Final dataset: 9000 anime dan 1594762 rating
- Alasan: Konsistensi data penting untuk menghindari error saat melakukan join antar dataset"""

# 1. Preprocessing genre untuk TF-IDF
def preprocess_genre(genre_str):
    """Preprocessing string genre untuk TF-IDF"""
    if pd.isna(genre_str) or genre_str == 'Unknown':
        return 'unknown'
    # Bersihkan dan standardisasi genre
    genres = [g.strip().lower().replace(' ', '_') for g in genre_str.split(',')]
    return ' '.join(genres)

anime_final['genre_processed'] = anime_final['genre'].apply(preprocess_genre)

"""- Standardisasi format: Mengubah genre menjadi format lowercase dan mengganti spasi dengan underscore
- Alasan: TF-IDF vectorizer memerlukan format teks yang konsisten untuk hasil yang optimal
"""

# 2. Buat feature gabungan untuk content-based
anime_final['content_features'] = anime_final['genre_processed'] + ' ' + anime_final['type'].fillna('').str.lower()

print("=== SAMPLE PREPROCESSED DATA ===")
print(anime_final[['name', 'genre', 'genre_processed', 'content_features']].head())

"""Fitur baru bernama `content_features` dibuat dengan menggabungkan informasi dari `genre` dan `type`. Fitur ini diproses dengan lowercasing, penghapusan spasi, dan digabungkan sebagai satu string untuk mewakili konten setiap anime.

"""

# 1. Filter user dan anime dengan minimal interaksi
min_user_ratings = 50  # User minimal rating 50 anime
min_anime_ratings = 20  # Anime minimal dirating 20 user

# Hitung jumlah rating per user dan per anime
user_counts = rating_final['user_id'].value_counts()
anime_counts = rating_final['anime_id'].value_counts()

# Filter berdasarkan threshold
active_users = user_counts[user_counts >= min_user_ratings].index
popular_anime = anime_counts[anime_counts >= min_anime_ratings].index

# Apply filter
rating_filtered = rating_final[
    (rating_final['user_id'].isin(active_users)) &
    (rating_final['anime_id'].isin(popular_anime))
].copy()

print(f"=== COLLABORATIVE FILTERING DATA ===")
print(f"Active users: {len(active_users)}")
print(f"Popular anime: {len(popular_anime)}")
print(f"Filtered ratings: {rating_filtered.shape}")

"""Dilakukan filtering untuk meningkatkan kualitas data:
- Hanya menyertakan anime yang memiliki setidaknya 20 rating dari user.
- Hanya menyertakan user yang memberikan setidaknya 50 rating.

"""

# 2. Buat user-item matrix
user_item_matrix = rating_filtered.pivot_table(
    index='user_id',
    columns='anime_id',
    values='rating'
).fillna(0)

print(f"User-item matrix shape: {user_item_matrix.shape}")

# Sparsity analysis
total_possible_ratings = user_item_matrix.shape[0] * user_item_matrix.shape[1]
actual_ratings = (user_item_matrix != 0).sum().sum()
sparsity = (1 - actual_ratings / total_possible_ratings) * 100

print(f"Matrix sparsity: {sparsity:.2f}%")

"""User-item matrix dibentuk dari data rating yang sudah difilter. Matriks ini digunakan sebagai input untuk Collaborative Filtering berbasis algoritma k-Nearest Neighbors.

"""

class ContentBasedRecommender:
    def __init__(self, anime_df):
        self.anime_df = anime_df
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.indices = pd.Series(anime_df.index, index=anime_df['name']).drop_duplicates()

    def fit(self):
        """Train content-based model menggunakan TF-IDF dan cosine similarity"""
        # Inisialisasi TF-IDF Vectorizer
        tfidf = TfidfVectorizer(stop_words='english', max_features=5000)

        # Fit dan transform content features
        self.tfidf_matrix = tfidf.fit_transform(self.anime_df['content_features'])

        # Hitung cosine similarity
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

        print(f"TF-IDF matrix shape: {self.tfidf_matrix.shape}")
        print("Content-based model trained successfully!")

    def get_recommendations(self, anime_name, n_recommendations=10):
        """Dapatkan rekomendasi berdasarkan nama anime"""
        try:
            # Dapatkan index anime
            idx = self.indices[anime_name]

            # Hitung similarity scores
            sim_scores = list(enumerate(self.cosine_sim[idx]))

            # Sort berdasarkan similarity score
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Ambil top N (exclude anime itu sendiri)
            sim_scores = sim_scores[1:n_recommendations+1]

            # Dapatkan indices anime
            anime_indices = [i[0] for i in sim_scores]

            # Return rekomendasi
            recommendations = self.anime_df.iloc[anime_indices][['name', 'genre', 'type', 'rating']].copy()
            recommendations['similarity_score'] = [score[1] for score in sim_scores]

            return recommendations

        except KeyError:
            print(f"Anime '{anime_name}' tidak ditemukan dalam dataset")
            return None

# Inisialisasi dan training content-based recommender
cb_recommender = ContentBasedRecommender(anime_final)
cb_recommender.fit()

# Test content-based recommendation
test_anime = "Death Note"
print(f"=== CONTENT-BASED RECOMMENDATIONS FOR '{test_anime}' ===")
cb_recommendations = cb_recommender.get_recommendations(test_anime, n_recommendations=10)
if cb_recommendations is not None:
    print(cb_recommendations)

"""#### Transformasi Fitur Teks untuk Content-Based Filtering

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
"""

class CollaborativeFilteringRecommender:
    def __init__(self, user_item_matrix, anime_df):
        self.user_item_matrix = user_item_matrix
        self.anime_df = anime_df
        self.user_similarity = None

    def fit(self):
        """Train collaborative filtering model menggunakan user-user similarity"""
        # Hitung user similarity menggunakan cosine similarity
        self.user_similarity = cosine_similarity(self.user_item_matrix)

        print(f"User similarity matrix shape: {self.user_similarity.shape}")
        print("Collaborative filtering model trained successfully!")

    def get_user_recommendations(self, user_id, n_recommendations=10):
        """Dapatkan rekomendasi untuk user tertentu"""
        if user_id not in self.user_item_matrix.index:
            print(f"User {user_id} tidak ditemukan")
            return None

        # Dapatkan index user dalam matrix
        user_idx = self.user_item_matrix.index.get_loc(user_id)

        # Dapatkan similarity scores untuk user ini
        user_sim_scores = self.user_similarity[user_idx]

        # Dapatkan anime yang belum dirating oleh user
        user_ratings = self.user_item_matrix.loc[user_id]
        unrated_anime = user_ratings[user_ratings == 0].index

        # Prediksi rating untuk unrated anime
        predictions = []
        for anime_id in unrated_anime:
            # Dapatkan users yang sudah rating anime ini
            anime_ratings = self.user_item_matrix[anime_id]
            rated_users = anime_ratings[anime_ratings > 0]

            if len(rated_users) == 0:
                continue

            # Hitung weighted average rating
            numerator = 0
            denominator = 0

            for other_user_id in rated_users.index:
                other_user_idx = self.user_item_matrix.index.get_loc(other_user_id)
                similarity = user_sim_scores[other_user_idx]
                rating = rated_users[other_user_id]

                numerator += similarity * rating
                denominator += abs(similarity)

            if denominator > 0:
                predicted_rating = numerator / denominator
                predictions.append((anime_id, predicted_rating))

        # Sort dan ambil top N
        predictions.sort(key=lambda x: x[1], reverse=True)
        top_anime_ids = [pred[0] for pred in predictions[:n_recommendations]]

        # Dapatkan informasi anime
        recommendations = self.anime_df[self.anime_df['anime_id'].isin(top_anime_ids)][
            ['anime_id', 'name', 'genre', 'type', 'rating']
        ].copy()

        # Tambahkan predicted rating
        pred_dict = dict(predictions[:n_recommendations])
        recommendations['predicted_rating'] = recommendations['anime_id'].map(pred_dict)

        return recommendations.sort_values('predicted_rating', ascending=False)

# Inisialisasi dan training collaborative filtering recommender
cf_recommender = CollaborativeFilteringRecommender(user_item_matrix, anime_final)
cf_recommender.fit()

# Test collaborative filtering recommendation
test_user = user_item_matrix.index[0]  # Ambil user pertama
print(f"\n=== COLLABORATIVE FILTERING RECOMMENDATIONS FOR USER {test_user} ===")
cf_recommendations = cf_recommender.get_user_recommendations(test_user, n_recommendations=10)
if cf_recommendations is not None:
    print(cf_recommendations)

"""### 2. Collaborative Filtering (User-User)

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

"""

print("\n" + "="*80)
print("TOP-N RECOMMENDATION RESULTS")
print("="*80)

# 1. Content-Based Recommendations
print(f"\n1. CONTENT-BASED FILTERING - Top 5 recommendations for '{test_anime}':")
print("-" * 60)
if cb_recommendations is not None:
    top_5_cb = cb_recommendations.head()
    for idx, row in top_5_cb.iterrows():
        print(f"{idx+1}. {row['name']}")
        print(f"   Genre: {row['genre']}")
        print(f"   Type: {row['type']} | Rating: {row['rating']:.2f}")
        print(f"   Similarity Score: {row['similarity_score']:.4f}")
        print()

# 2. Collaborative Filtering Recommendations
print(f"\n2. COLLABORATIVE FILTERING - Top 5 recommendations for User {test_user}:")
print("-" * 60)
if cf_recommendations is not None:
    top_5_cf = cf_recommendations.head()
    for idx, row in top_5_cf.iterrows():
        print(f"{idx+1}. {row['name']}")
        print(f"   Genre: {row['genre']}")
        print(f"   Type: {row['type']} | Rating: {row['rating']:.2f}")
        # Change 'Similarity Score' to 'Predicted Rating'
        print(f"   Predicted Rating: {row['predicted_rating']:.4f}")

        print()

"""##Keluaran untuk Content-Based Filtering dan Collaborative Filtering tidak bisa memiliki format yang sama dalam hal menampilkan "Predicted Rating"/"Similarity Score" Kenapa?
 karena kedua model menghasilkan jenis output yang berbeda:

1. Content-Based Filtering: Model ini menghitung kesamaan (similarity) antara anime berdasarkan fitur-fitur kontennya (genre, tipe). Outputnya adalah skor yang menunjukkan seberapa mirip anime rekomendasi dengan anime yang menjadi input. Model ini tidak memprediksi rating yang mungkin diberikan user terhadap anime rekomendasi. Oleh karena itu, kolom yang relevan untuk ditampilkan adalah similarity_score.

2. Collaborative Filtering: Model ini memprediksi rating yang mungkin diberikan seorang user terhadap anime yang belum ditonton, berdasarkan preferensi user lain yang serupa. Outputnya adalah nilai prediksi rating (predicted rating). Oleh karena itu, kolom yang relevan untuk ditampilkan adalah predicted_rating.

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
"""

def evaluate_content_based_diversity(recommender, test_animes, n_recommendations=10):
    """Evaluasi diversity dari content-based recommendations"""
    all_genres = []

    for anime_name in test_animes:
        recommendations = recommender.get_recommendations(anime_name, n_recommendations)
        if recommendations is not None:
            for _, row in recommendations.iterrows():
                if pd.notna(row['genre']):
                    genres = [g.strip() for g in row['genre'].split(',')]
                    all_genres.extend(genres)

    unique_genres = len(set(all_genres))
    total_recommendations = len(all_genres)
    diversity_score = unique_genres / total_recommendations if total_recommendations > 0 else 0

    return diversity_score, unique_genres, total_recommendations

"""## Evaluation

### 1. Content-Based Filtering
"""

# Test dengan beberapa anime populer
test_animes = ["Death Note", "Naruto", "One Piece", "Attack on Titan", "Dragon Ball Z"]
test_animes_available = [anime for anime in test_animes if anime in cb_recommender.indices]

print("=== CONTENT-BASED FILTERING EVALUATION ===")
print(f"Testing with animes: {test_animes_available}")

if test_animes_available:
    diversity_score, unique_genres, total_recs = evaluate_content_based_diversity(
        cb_recommender, test_animes_available
    )

    print(f"Diversity Score: {diversity_score:.4f}")
    print(f"Unique Genres: {unique_genres}")
    print(f"Total Recommendations: {total_recs}")

    # Precision based on genre similarity
    precision_scores = []
    for anime_name in test_animes_available:
        if anime_name in anime_final['name'].values:
            original_anime = anime_final[anime_final['name'] == anime_name].iloc[0]
            original_genres = set([g.strip() for g in original_anime['genre'].split(',')])

            recommendations = cb_recommender.get_recommendations(anime_name, 5)
            if recommendations is not None:
                relevant_count = 0
                for _, rec in recommendations.iterrows():
                    rec_genres = set([g.strip() for g in rec['genre'].split(',')])
                    if len(original_genres.intersection(rec_genres)) > 0:
                        relevant_count += 1

                precision = relevant_count / len(recommendations)
                precision_scores.append(precision)
                print(f"Precision for {anime_name}: {precision:.4f}")

    if precision_scores:
        avg_precision = np.mean(precision_scores)
        print(f"Average Precision: {avg_precision:.4f}")

"""Precision berdasarkan Genre Similarity:

      Precision = (Jumlah rekomendasi dengan genre serupa) / (Total rekomendasi)

- Hasil: Average Precision = 0.6667
- Interpretasi: 66% rekomendasi memiliki setidaknya satu genre yang sama dengan anime referensi

Diversity Score:
      Diversity = (Jumlah genre unik) / (Total rekomendasi)

- Hasil: Diversity Score = 0.0877
- Interpretasi: Sistem dapat memberikan variasi genre yang cukup baik

### 2. COLLABORATIVE FILTERING EVALUATION
"""

def evaluate_collaborative_filtering(recommender, test_ratio=0.2):
    """Evaluasi collaborative filtering menggunakan train-test split"""

    # Siapkan data untuk evaluasi
    ratings_data = []
    for user_id in user_item_matrix.index:
        user_ratings = user_item_matrix.loc[user_id]
        rated_items = user_ratings[user_ratings > 0]

        for anime_id, rating in rated_items.items():
            ratings_data.append({
                'user_id': user_id,
                'anime_id': anime_id,
                'rating': rating
            })

    ratings_df = pd.DataFrame(ratings_data)

    # Split data
    train_data, test_data = train_test_split(ratings_df, test_size=test_ratio, random_state=42)

    # Buat matrix untuk training
    train_matrix = train_data.pivot_table(
        index='user_id',
        columns='anime_id',
        values='rating'
    ).fillna(0)

    # Recompute similarity dengan training data
    train_similarity = cosine_similarity(train_matrix)

    # Prediksi untuk test data
    predictions = []
    actuals = []

    for _, row in test_data.head(1000).iterrows():  # Ambil sample untuk evaluasi
        user_id = row['user_id']
        anime_id = row['anime_id']
        actual_rating = row['rating']

        if user_id in train_matrix.index and anime_id in train_matrix.columns:
            user_idx = train_matrix.index.get_loc(user_id)
            user_sim_scores = train_similarity[user_idx]

            # Prediksi rating
            anime_ratings = train_matrix[anime_id]
            rated_users = anime_ratings[anime_ratings > 0]

            if len(rated_users) > 0:
                numerator = 0
                denominator = 0

                for other_user_id in rated_users.index:
                    other_user_idx = train_matrix.index.get_loc(other_user_id)
                    similarity = user_sim_scores[other_user_idx]
                    rating = rated_users[other_user_id]

                    numerator += similarity * rating
                    denominator += abs(similarity)

                if denominator > 0:
                    predicted_rating = numerator / denominator
                    predictions.append(predicted_rating)
                    actuals.append(actual_rating)

    # Hitung RMSE
    if predictions:
        rmse = np.sqrt(mean_squared_error(actuals, predictions))
        mae = np.mean(np.abs(np.array(actuals) - np.array(predictions)))

        return rmse, mae, len(predictions)
    else:
        return None, None, 0

print("\n=== COLLABORATIVE FILTERING EVALUATION ===")
rmse, mae, n_predictions = evaluate_collaborative_filtering(cf_recommender)

if rmse is not None:
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"Number of predictions: {n_predictions}")
else:
    print("Tidak dapat menghitung RMSE dan MAE")

"""Root Mean Square Error (RMSE):

    RMSE = √(Σ(actual_rating - predicted_rating)² / n)

- Hasil: RMSE = 1.3178
- Interpretasi: Rata-rata error prediksi adalah 1.71 poin pada skala 1-10

Mean Absolute Error (MAE):
    MAE = Σ|actual_rating - predicted_rating| / n

- Hasil: MAE = 1.0320
- Interpretasi: Rata-rata absolut error adalah 1.03 poin

### Coverage Analysis
"""

print("\n=== COVERAGE ANALYSIS ===")

# Content-based coverage
cb_coverage = len(anime_final) / len(anime_df) * 100
print(f"Content-based Coverage: {cb_coverage:.2f}% ({len(anime_final)}/{len(anime_df)} anime)")

# Collaborative filtering coverage
cf_anime_coverage = len(popular_anime) / len(anime_df) * 100
cf_user_coverage = len(active_users) / rating_df['user_id'].nunique() * 100
print(f"Collaborative Filtering - Anime Coverage: {cf_anime_coverage:.2f}% ({len(popular_anime)}/{len(anime_df)} anime)")
print(f"Collaborative Filtering - User Coverage: {cf_user_coverage:.2f}% ({len(active_users)}/{rating_df['user_id'].nunique()} users)")

"""**Content-Based Coverage:** 73.21% (9,000/12,294 anime)

- Dapat memberikan rekomendasi untuk mayoritas anime dalam dataset

**Collaborative Filtering Coverage:**

- Anime Coverage: 35.85% (4.407/12,294 anime)
- User Coverage: 44.36% (8471/19,094 users)
- Coverage rendah karena filtering untuk mengurangi sparsity
"""

print("\n" + "="*80)
print("EVALUATION SUMMARY")
print("="*80)

print("\n1. CONTENT-BASED FILTERING:")
print(f"   ✓ Dapat memberikan rekomendasi berdasarkan konten anime")
print(f"   ✓ Coverage: {cb_coverage:.2f}% dari total anime")
if 'avg_precision' in locals():
    print(f"   ✓ Average Precision: {avg_precision:.4f}")
if 'diversity_score' in locals():
    print(f"   ✓ Diversity Score: {diversity_score:.4f}")

print(f"\n2. COLLABORATIVE FILTERING:")
print(f"   ✓ Dapat memberikan rekomendasi berdasarkan preferensi user serupa")
print(f"   ✓ Anime Coverage: {cf_anime_coverage:.2f}%")
print(f"   ✓ User Coverage: {cf_user_coverage:.2f}%")
if rmse is not None:
    print(f"   ✓ RMSE: {rmse:.4f}")
    print(f"   ✓ MAE: {mae:.4f}")

print(f"\n3. SYSTEM CHARACTERISTICS:")
print(f"   • Total Anime in Dataset: {len(anime_df):,}")
print(f"   • Total Users: {rating_df['user_id'].nunique():,}")
print(f"   • Total Ratings: {len(rating_df):,}")
print(f"   • Matrix Sparsity: {sparsity:.2f}%")

print(f"\n4. RECOMMENDATION CAPABILITIES:")
print(f"   • Content-based: Merekomendasikan anime dengan genre/karakteristik serupa")
print(f"   • Collaborative: Merekomendasikan anime berdasarkan user dengan preferensi serupa")
print(f"   • Kedua sistem dapat memberikan Top-N recommendations")

"""## Kesimpulan:
Kedua sistem memberikan pendekatan yang complementary. Content-based filtering unggul dalam coverage dan mengatasi cold start, sedangkan collaborative filtering memberikan rekomendasi berdasarkan preferensi komunitas. Implementasi hybrid system dapat menggabungkan kelebihan kedua pendekatan untuk hasil yang optimal.
"""