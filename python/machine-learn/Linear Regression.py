#Library yang dibutuhkan
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
 # 1. MEMBACA  DATA DARI CSV
df = pd.read_csv('data_update.csv')
# Hilangkan spasi di awal/akhir nama kolom
df.columns = df.columns.str.strip()
# Rename kolom agar mudah
df = df.rename(columns={
    'X': 'Jam Belajar',
    'Y': 'Commit'
})
# Fungsi konversi jam belajar ke float (menit jadi jam, koma jadi titik, hapus teks)
def parse_jam_belajar(x):
    x = str(x).strip().lower()
    if 'menit' in x:
        angka = ''.join([c for c in x if c.isdigit() or c == ',' or c == '.'])
        angka = angka.replace(',', '.')
        try:
            return float(angka) / 60
        except:
            return np.nan
    if ',' in x:
        x = x.replace(',', '.')
    try:
        return float(x)
    except:
        return np.nan
# Fungsi konversi commit ke int (jika tidak bisa, jadi NaN)
def parse_commit(x):
    try:
        return int(x)
    except:
        return np.nan

df['Jam Belajar'] = df['Jam Belajar'].apply(parse_jam_belajar)
df['Commit'] = df['Commit'].apply(parse_commit)
# Hapus baris yang tidak valid
df = df.dropna(subset=['Jam Belajar', 'Commit'])

# 2. PERSIAPAN DATA
x = df[['Jam Belajar']]
y = df['Commit']

# 3. TRAIN MODEL REGRESI
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

# 4. VISUALISASI HASIL
plt.scatter(x, y, color='blue', label='Data Asli')
plt.plot(x, y_pred, color='red', label='Garis Regresi')
plt.title('Hubungan Jam Belajar vs Commit GitHub')
plt.xlabel('Jam Belajar (jam/hari)')
plt.ylabel('Commit GitHub (minggu)')
plt.legend()
plt.show()

# 5. EVALUASI MODEL
mse = mean_squared_error(y, y_pred)
print(f"Koefisien Regresi (Slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")