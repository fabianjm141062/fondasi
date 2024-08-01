import streamlit as st

# Fungsi untuk menghitung daya dukung tiang pancang
def hitung_daya_dukung_tiang(c, phi, gamma, diameter, panjang_tiang):
    # Konstanta untuk rumus daya dukung
    Nq = (1 + 0.4 * phi) * (1 + 0.4 * c)
    Nc = (1 + 0.4 * phi) * (1 + 0.4 * c)
    Ngamma = 0.5 * gamma * (1 + 0.4 * phi)

    # Perhitungan area tiang
    area_tiang = 3.14 * (diameter / 2) ** 2
    
    # Perhitungan daya dukung
    daya_dukung = (Nc * c * area_tiang) + (Nq * gamma * panjang_tiang * area_tiang) + (Ngamma * gamma * panjang_tiang)
    return daya_dukung

# Judul aplikasi
st.title('Perhitungan Daya Dukung Tiang Pancang')

# Input dari pengguna
c = st.number_input('Masukkan kohesi tanah (c) dalam kPa', min_value=0.0, value=25.0)
phi = st.number_input('Masukkan sudut geser dalam tanah (phi) dalam derajat', min_value=0.0, value=30.0)
gamma = st.number_input('Masukkan berat jenis tanah (γ) dalam kN/m³', min_value=0.0, value=18.0)
diameter = st.number_input('Masukkan diameter tiang (m)', min_value=0.0, value=0.5)
panjang_tiang = st.number_input('Masukkan panjang tiang (m)', min_value=0.0, value=10.0)

# Tombol untuk menghitung daya dukung
if st.button('Hitung Daya Dukung'):
    daya_dukung = hitung_daya_dukung_tiang(c, phi, gamma, diameter, panjang_tiang)
    st.write(f'Daya Dukung Tiang Pancang: {daya_dukung:.2f} kN')

# Tambahan informasi
st.write('Perhitungan ini menggunakan formula sederhana dan mungkin memerlukan penyesuaian berdasarkan kondisi lapangan yang sebenarnya.')
