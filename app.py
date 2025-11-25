import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Penjualan Produk",
    page_icon="📊",
    layout="wide"
)

# Judul dan Deskripsi Aplikasi
st.title("📊 Dashboard Visualisasi Penjualan Produk")
st.markdown("""
### Selamat Datang di Dashboard Interaktif!
Dashboard ini menampilkan data penjualan produk elektronik dari berbagai kota di Indonesia.
Anda dapat memilih jenis visualisasi yang diinginkan menggunakan dropdown di bawah ini.
""")

st.divider()

# Data penjualan produk (minimal 10 baris)
data = {
    'Kota': ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang', 
             'Makassar', 'Palembang', 'Tangerang', 'Depok', 'Bekasi',
             'Yogyakarta', 'Malang'],
    'Penjualan': [450, 380, 320, 280, 250, 220, 200, 190, 180, 170, 160, 150],
    'Produk_Terjual': [120, 95, 85, 70, 65, 58, 52, 48, 45, 42, 40, 38],
    'Latitude': [-6.2088, -7.2575, -6.9175, 3.5952, -6.9932,
                 -5.1477, -2.9761, -6.1781, -6.4025, -6.2383, -7.7956, -7.9666],
    'Longitude': [106.8456, 112.7521, 107.6191, 98.6722, 110.4203,
                  119.4327, 104.7754, 106.6300, 106.7942, 106.9925, 110.3695, 112.6326]
}

df = pd.DataFrame(data)

# Menampilkan data dalam expander
with st.expander("📋 Lihat Data Lengkap"):
    st.dataframe(df, use_container_width=True)
    st.info(f"Total data: {len(df)} kota")

st.divider()

# Dropdown untuk memilih jenis visualisasi
st.subheader("🎯 Pilih Jenis Visualisasi")
jenis_chart = st.selectbox(
    "Pilih visualisasi yang ingin ditampilkan:",
    ["Bar Chart", "Line Chart", "Pie Chart", "Area Chart", "Map Chart"],
    index=0
)

st.divider()

# Menampilkan visualisasi berdasarkan pilihan
if jenis_chart == "Bar Chart":
    st.subheader("📊 Bar Chart - Penjualan per Kota")
    st.markdown("Grafik batang menunjukkan perbandingan penjualan produk di setiap kota.")
    
    fig = px.bar(
        df, 
        x='Kota', 
        y='Penjualan',
        color='Penjualan',
        color_continuous_scale='Blues',
        labels={'Penjualan': 'Total Penjualan (Unit)'},
        title='Perbandingan Penjualan Produk per Kota'
    )
    fig.update_layout(
        xaxis_title="Kota",
        yaxis_title="Penjualan (Unit)",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistik tambahan
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏆 Kota Tertinggi", df.loc[df['Penjualan'].idxmax(), 'Kota'], 
                 f"{df['Penjualan'].max()} unit")
    with col2:
        st.metric("📈 Rata-rata", f"{df['Penjualan'].mean():.0f} unit")
    with col3:
        st.metric("📉 Kota Terendah", df.loc[df['Penjualan'].idxmin(), 'Kota'], 
                 f"{df['Penjualan'].min()} unit")

elif jenis_chart == "Line Chart":
    st.subheader("📈 Line Chart - Tren Penjualan")
    st.markdown("Grafik garis menunjukkan tren penjualan dari kota dengan penjualan tertinggi ke terendah.")
    
    df_sorted = df.sort_values('Penjualan', ascending=False).reset_index(drop=True)
    
    fig = px.line(
        df_sorted, 
        x='Kota', 
        y='Penjualan',
        markers=True,
        title='Tren Penjualan Produk (Dari Tertinggi ke Terendah)'
    )
    fig.update_traces(
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=10, color='#ff7f0e')
    )
    fig.update_layout(
        xaxis_title="Kota",
        yaxis_title="Penjualan (Unit)",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Insight tambahan
    st.info(f"📊 **Insight**: Terdapat perbedaan {df['Penjualan'].max() - df['Penjualan'].min()} unit antara kota dengan penjualan tertinggi dan terendah.")

elif jenis_chart == "Pie Chart":
    st.subheader("🥧 Pie Chart - Distribusi Penjualan")
    st.markdown("Diagram lingkaran menunjukkan proporsi kontribusi penjualan dari setiap kota.")
    
    fig = px.pie(
        df, 
        values='Penjualan', 
        names='Kota',
        title='Distribusi Penjualan Produk per Kota',
        hole=0.4,  # Membuat donut chart
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Menampilkan top 3 kota
    st.markdown("### 🏆 Top 3 Kota dengan Penjualan Tertinggi")
    top_3 = df.nlargest(3, 'Penjualan')
    for idx, row in top_3.iterrows():
        percentage = (row['Penjualan'] / df['Penjualan'].sum()) * 100
        st.success(f"**{row['Kota']}**: {row['Penjualan']} unit ({percentage:.1f}% dari total)")

elif jenis_chart == "Area Chart":
    st.subheader("📊 Area Chart - Area Penjualan")
    st.markdown("Grafik area menunjukkan volume penjualan kumulatif dari setiap kota.")
    
    df_sorted = df.sort_values('Penjualan', ascending=False).reset_index(drop=True)
    
    fig = px.area(
        df_sorted, 
        x='Kota', 
        y='Penjualan',
        title='Area Chart Penjualan Produk',
        color_discrete_sequence=['#17becf']
    )
    fig.update_layout(
        xaxis_title="Kota",
        yaxis_title="Penjualan (Unit)",
        height=500,
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistik distribusi
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📊 Total Penjualan", f"{df['Penjualan'].sum()} unit")
        st.metric("📦 Total Produk Terjual", f"{df['Produk_Terjual'].sum()} item")
    with col2:
        st.metric("🏙️ Jumlah Kota", f"{len(df)} kota")
        st.metric("📏 Standar Deviasi", f"{df['Penjualan'].std():.1f}")

elif jenis_chart == "Map Chart":
    st.subheader("🗺️ Map Chart - Peta Sebaran Penjualan")
    st.markdown("Peta interaktif menunjukkan lokasi dan volume penjualan di setiap kota di Indonesia.")
    
    # Membuat peta dengan Plotly
    fig = px.scatter_mapbox(
        df,
        lat='Latitude',
        lon='Longitude',
        size='Penjualan',
        color='Penjualan',
        hover_name='Kota',
        hover_data={
            'Penjualan': ':,',
            'Produk_Terjual': ':,',
            'Latitude': False,
            'Longitude': False
        },
        color_continuous_scale='Viridis',
        size_max=30,
        zoom=4,
        title='Peta Sebaran Penjualan Produk di Indonesia'
    )
    
    fig.update_layout(
        mapbox_style="open-street-map",
        height=600,
        margin={"r":0,"t":50,"l":0,"b":0}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Penjelasan peta
    st.info("""
    💡 **Cara membaca peta**:
    - Ukuran lingkaran menunjukkan volume penjualan
    - Warna menunjukkan intensitas penjualan (lebih terang = lebih tinggi)
    - Hover pada lingkaran untuk melihat detail informasi
    """)


