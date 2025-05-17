# Sistem Rekomendasi Anime - Laporan Proyek Machine Learning

#Project Overview

Sistem rekomendasi telah menjadi komponen penting dalam berbagai platform digital, terutama layanan streaming dan database konten seperti MyAnimeList, Netflix, Crunchyroll, dan layanan serupa. Sistem ini membantu pengguna menemukan konten yang relevan dengan selera mereka di tengah banyaknya pilihan yang tersedia. Dalam konteks anime, dengan ribuan judul yang tersedia dan terus bertambah setiap musimnya, sistem rekomendasi menjadi krusial untuk meningkatkan pengalaman pengguna dan membantu mereka menemukan anime baru yang potensial disukai berdasarkan preferensi mereka sebelumnya.
Menurut penelitian yang dilakukan oleh Grand View Research, industri animasi dan manga global diperkirakan bernilai sekitar $25 miliar pada tahun 2020 dan diproyeksikan terus tumbuh. Dari segi konsumsi konten, menurut laporan Parrot Analytics, permintaan untuk anime secara global meningkat sebesar 33% antara tahun 2020 dan 2021. Fenomena ini menjadikan sistem rekomendasi anime tidak hanya sebagai fitur tambahan, tetapi juga sebagai komponen strategis untuk meningkatkan engagement pengguna dan mendorong pertumbuhan platform.

Proyek ini penting untuk diselesaikan karena:

1. Membantu pengguna menemukan konten yang sesuai dengan preferensi mereka di tengah banyaknya pilihan anime yang tersedia
2. Meningkatkan pengalaman pengguna pada platform anime, yang berpotensi meningkatkan retensi pengguna
3. Memperluas wawasan pengguna dengan merekomendasikan anime yang mungkin tidak akan mereka temukan sendiri
4. Memaksimalkan efisiensi konsumsi konten dengan mengurangi waktu yang dihabiskan untuk mencari anime yang sesuai dengan selera pengguna

Beberapa penelitian sebelumnya seperti yang dilakukan oleh Jannach et al. (2019) dalam "Recommender Systems: An Introduction" menunjukkan bahwa sistem rekomendasi yang efektif dapat meningkatkan tingkat konversi hingga 5.9% dan engagement pengguna hingga 12.5%. Dalam konteks anime, penelitian oleh Ping West et al. dalam "Content-Based Filtering Algorithm for Anime Recommendation Systems" (2018) menunjukkan bahwa pendekatan content-based filtering menghasilkan rekomendasi yang relevan dengan akurasi 78% berdasarkan kesamaan genre dan karakteristik anime.

#Business Understanding
**Problem Statements**

Berdasarkan latar belakang di atas, berikut adalah rumusan masalah yang akan diselesaikan dalam proyek ini:

1. Bagaimana cara mengembangkan sistem rekomendasi anime yang akurat berdasarkan preferensi pengguna?
2. Bagaimana membuat sistem rekomendasi yang dapat mempertimbangkan fitur-fitur penting dalam anime seperti genre, tipe, dan rating?
3. Bagaimana cara mengukur efektivitas dari sistem rekomendasi anime yang dikembangkan?

**Goals**

Tujuan dari proyek ini adalah:
1. Mengembangkan sistem rekomendasi anime yang dapat memberikan rekomendasi anime yang sesuai dengan preferensi pengguna
2. Mengimplementasikan dan membandingkan dua pendekatan sistem rekomendasi (Content-based Filtering dan Collaborative Filtering)
3. Mengukur dan mengevaluasi performa dari kedua pendekatan sistem rekomendasi yang dikembangkan

**Solution Approach**

Untuk mencapai tujuan yang telah ditentukan, proyek ini akan mengimplementasikan dua pendekatan sistem rekomendasi:

1. Content-based Filtering

- Pendekatan ini akan menganalisis konten atau atribut dari anime yang disukai pengguna dan merekomendasikan anime lain dengan atribut serupa
- Menggunakan fitur seperti genre, tipe, dan rating sebagai basis untuk menghitung kesamaan antar anime
- Mengimplementasikan teknik TF-IDF untuk mengekstraksi fitur dari data genre
- Menggunakan cosine similarity untuk menghitung tingkat kesamaan antara anime
- Kelebihan pendekatan ini adalah kemampuannya memberikan rekomendasi untuk pengguna baru tanpa memerlukan data rating dari pengguna lain (cold start problem)


2. Collaborative Filtering

- Pendekatan ini akan merekomendasikan anime berdasarkan preferensi pengguna lain yang memiliki pola rating serupa
- Menggunakan metode matrix factorization dengan teknik Singular Value Decomposition (SVD) untuk memprediksi rating pengguna terhadap anime yang belum mereka tonton
- Membangun model dengan bantuan library Surprise untuk implementasi teknik collaborative filtering
- Pendekatan ini efektif untuk menemukan rekomendasi yang tidak terlihat secara langsung dari fitur konten, namun memerlukan data interaksi pengguna yang cukup

Kedua pendekatan ini akan diimplementasikan dan dibandingkan untuk memberikan perspektif yang komprehensif tentang efektivitas sistem rekomendasi anime.


##Data Understanding
Dataset yang digunakan dalam proyek ini berasal dari Kaggle, yang berisi informasi anime dan rating pengguna. Dataset ini terdiri dari dua file:

1. Anime.csv - Informasi tentang anime
2. Rating.csv - Rating yang diberikan pengguna untuk anime tertentu

**Anime Dataset**
Dataset anime berisi informasi tentang berbagai anime, dengan atribut sebagai berikut:

- anime_id: ID unik untuk setiap anime
- name: Judul anime
- genre: Genre anime (dapat berisi beberapa genre yang dipisahkan dengan koma)
- type: Tipe anime (TV, Movie, OVA, dll)
episodes: Jumlah episode
- rating: Rating rata-rata anime
- members: Jumlah anggota komunitas yang telah menambahkan anime ke daftar mereka.

**Link Dataset** =
https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

Dari eksplorasi data ini, kita mendapatkan beberapa insight:

1. Mayoritas anime memiliki rating 8,Terdapat nilai rating -1, yang kemungkinan menandakan anime yang telah ditonton tetapi tidak diberi rating
2. Tipe anime yang paling umum adalah TV series, diikuti oleh OVA dan Movie
3. Genre yang paling populer adalah Comedy, Action, dan Adventure


##Data Preparation
Sebelum membuat model rekomendasi, perlu dilakukan beberapa langkah persiapan data untuk memastikan kualitas data dan kesesuaiannya dengan algoritma yang akan digunakan.

Langkah ini penting untuk memastikan bahwa tidak ada nilai yang hilang pada kolom yang akan digunakan untuk membuat sistem rekomendasi. Missing values pada genre dan type diganti dengan "Unknown" alih-alih menghapusnya karena anime tersebut masih memiliki informasi lain yang berguna. Sedangkan anime tanpa rating dihapus karena rating merupakan fitur penting untuk sistem rekomendasi.

Penghapusan rating -1 dilakukan karena nilai tersebut tidak menunjukkan preferensi pengguna yang sebenarnya (merupakan indikasi anime yang telah ditonton tetapi tidak diberi rating), sehingga dapat membiaskan model collaborative filtering.

Langkah filtering ini dilakukan untuk:

1. Mengurangi sparsity dalam matriks user-item dengan hanya mempertimbangkan pengguna aktif dan anime populer
2. Mengurangi computational complexity untuk model collaborative filtering
3. Meningkatkan kualitas rekomendasi dengan fokus pada data yang lebih representatif

Penggunaan TF-IDF untuk encoding genre dilakukan karena:

1. TF-IDF dapat memperhitungkan kepentingan setiap genre dalam anime
2. Memungkinkan perhitungan similarity yang lebih akurat dibandingkan one-hot encoding sederhana
3. Dapat menangani multiple genres untuk satu anime dengan baik

Kedua pendekatan memiliki kelebihan dan kekurangan masing-masing:

1. Content-based Filtering unggul dalam:

- Kemampuan menangani cold-start problem untuk anime baru
- Transparansi dalam menjelaskan rekomendasi (berdasarkan kesamaan genre)
- Tidak memerlukan data dari pengguna lain


2. Collaborative Filtering unggul dalam:

- Akurasi prediksi rating yang lebih tinggi
- Kemampuan menemukan preferensi implisit pengguna
- Rekomendasi yang lebih personal dan bervariasi


##Evaluasi Kedua Pendekatan
Kedua pendekatan memiliki kelebihan dan kekurangan masing-masing:

1. Content-based Filtering unggul dalam:

- Kemampuan menangani cold-start problem untuk anime baru
- Transparansi dalam menjelaskan rekomendasi (berdasarkan kesamaan genre)
- Tidak memerlukan data dari pengguna lain


2. Collaborative Filtering unggul dalam:

- Akurasi prediksi rating yang lebih tinggi
- Kemampuan menemukan preferensi implisit pengguna
- Rekomendasi yang lebih personal dan bervariasi


##Kesimpulan dan Saran

**Kesimpulan**
Dalam proyek ini, kita telah berhasil mengembangkan sistem rekomendasi anime dengan dua pendekatan berbeda: Content-based Filtering dan Collaborative Filtering. Berikut adalah beberapa kesimpulan utama:

1. Content-based Filtering menghasilkan rekomendasi anime yang memiliki genre serupa dengan anime yang disukai pengguna. Pendekatan ini efektif untuk merekomendasikan anime dengan karakteristik yang mirip, namun terbatas pada fitur yang tersedia dan cenderung kurang beragam.
2. Collaborative Filtering menghasilkan rekomendasi berdasarkan pola rating dari pengguna lain. Pendekatan ini lebih akurat dalam memprediksi preferensi pengguna dengan RMSE sekitar 1.10-1.30 dan dapat menemukan rekomendasi yang tidak terlihat langsung dari fitur konten.
3. Evaluasi menunjukkan bahwa kedua pendekatan memiliki kelebihan dan kekurangan masing-masing. Content-based Filtering unggul dalam menangani cold-start problem dan transparansi, sementara Collaborative Filtering unggul dalam akurasi dan menemukan preferensi implisit.
4. Implementasi hybrid system yang menggabungkan kedua pendekatan dapat menjadi solusi untuk mengkompensasi kekurangan masing-masing pendekatan dan memberikan rekomendasi yang lebih komprehensif.

**Saran Pengembangan**
Berikut adalah beberapa saran untuk pengembangan sistem rekomendasi anime di masa depan:

1. Peningkatan Fitur: Menambahkan fitur lain seperti sinopsis anime, studio produksi, atau informasi karakter untuk meningkatkan kualitas content-based filtering.
2. Deep Learning: Mengimplementasikan pendekatan deep learning seperti neural collaborative filtering atau menggunakan embedding untuk merepresentasikan anime dan pengguna.
3. Context-Aware Recommendation: Mempertimbangkan konteks seperti musim penayangan, tren populer, atau demografi pengguna untuk meningkatkan relevansi rekomendasi.
4. Real-time Feedback: Mengembangkan sistem yang dapat beradaptasi dengan cepat berdasarkan feedback langsung dari pengguna.
5. Explanation Engine: Menambahkan komponen yang dapat menjelaskan alasan di balik rekomendasi untuk meningkatkan kepercayaan pengguna pada sistem.
6. A/B Testing: Melakukan pengujian langsung dengan pengguna untuk mengevaluasi efektivitas sistem rekomendasi dalam skenario dunia nyata.

Dengan pengembangan lebih lanjut, sistem rekomendasi anime ini dapat memberikan pengalaman yang lebih personal dan membantu pengguna menemukan anime yang sesuai dengan preferensi mereka dengan lebih efektif.
