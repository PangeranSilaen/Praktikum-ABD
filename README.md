# Dashboard Visualisasi Penjualan Produk - Streamlit

Aplikasi Streamlit interaktif untuk visualisasi data penjualan produk elektronik di berbagai kota di Indonesia.

## 📋 Fitur Aplikasi

✅ **5 Jenis Visualisasi Interaktif**:
- Bar Chart - Perbandingan penjualan per kota
- Line Chart - Tren penjualan
- Pie Chart - Distribusi penjualan
- Area Chart - Area penjualan kumulatif
- Map Chart - Peta sebaran penjualan di Indonesia

✅ **Dataset**: 12 kota dengan data penjualan lengkap

✅ **Fitur Tambahan**:
- Judul dan deskripsi aplikasi
- Icon dan emoji untuk visual yang menarik
- Statistik dan metrics interaktif
- Data table yang dapat dilihat
- Insight dan analisis data

## 🚀 Cara Menjalankan Aplikasi

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi

```powershell
streamlit run app.py
```

Aplikasi akan otomatis terbuka di browser pada `http://localhost:8501`

## 📦 Requirements

- Python 3.8+
- streamlit==1.29.0
- pandas==2.1.4
- plotly==5.18.0

## 🌐 Deploy ke Streamlit Cloud

### Langkah-langkah Deploy:

1. **Buat Repository GitHub**
   - Buat repository baru di GitHub
   - Upload semua file (`app.py`, `requirements.txt`, `README.md`)

2. **Akses Streamlit Cloud**
   - Buka https://share.streamlit.io/
   - Login dengan GitHub account

3. **Deploy Aplikasi**
   - Klik "New app"
   - Pilih repository GitHub Anda
   - Pilih branch `main`
   - Set Main file path: `app.py`
   - Klik "Deploy"

4. **Tunggu Deployment**
   - Streamlit akan otomatis install dependencies
   - Aplikasi akan live dalam beberapa menit
   - Anda akan mendapat link publik seperti: `https://username-repo-name.streamlit.app`

## 📊 Struktur Data

Dataset berisi informasi penjualan dari 12 kota:
- **Kota**: Nama kota di Indonesia
- **Penjualan**: Total unit penjualan
- **Produk_Terjual**: Jumlah produk yang terjual
- **Latitude & Longitude**: Koordinat untuk visualisasi map

## 🎯 Checklist Tugas

- ✅ Dropdown dengan 5 pilihan visualisasi
- ✅ Minimal 10 data (12 kota)
- ✅ Implementasi Bar Chart
- ✅ Implementasi Line Chart
- ✅ Implementasi Pie Chart
- ✅ Implementasi Area Chart
- ✅ Implementasi Map Chart
- ✅ Judul aplikasi
- ✅ Deskripsi singkat
- ✅ Visual tambahan (emoji, icon, colors)
- 🔲 Deploy ke Streamlit Cloud (bonus +10)

## 👨‍💻 Informasi

**Mata Kuliah**: Administrasi Basis Data  
**Semester**: 5  
**Tools**: Streamlit, Plotly, Pandas  
**Tahun**: 2025


