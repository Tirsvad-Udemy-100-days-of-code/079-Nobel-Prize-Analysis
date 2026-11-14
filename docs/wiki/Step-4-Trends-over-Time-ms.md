[English](Step-4-Trends-over-Time) · [Dansk](Step-4-Trends-over-Time-da) · **Bahasa Malaysia**

# Langkah 4: Aliran dari masa ke masa dengan Matplotlib

**Soalan:** Adakah lebih banyak hadiah diberikan kebelakangan ini berbanding semasa hadiah diwujudkan, dan adakah hadiah dikongsi lebih ramai?

## Ringkasan kuliah

Kuliah melihat bilangan hadiah setiap tahun dan bertanya sama ada lebih banyak hadiah diberikan sekarang. Purata bergulir 5 tahun melicinkan hingar, dan paksi kedua menunjukkan sama ada hadiah dikongsi lebih ramai dari masa ke masa.

*Kuliah 586*

![chart-step-4-prizes-per-year.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-4-prizes-per-year.png)


## Apa yang kod lakukan

`prizes_per_year` mengira hadiah setiap tahun (kemuncak **15 pada 2001**). `rolling_average` melicinkannya dengan tetingkap 5 tahun, jadi empat nilai pertama ialah NaN. Carta melukis titik dengan `dodgerblue` dan purata dengan `crimson`, dengan tanda setiap 5 tahun dari 1900 hingga 2020 dibuat dengan NumPy. `average_share_per_year` dan purata bergulirnya menunjukkan sama ada bahagian setiap pemenang berubah, dilukis pada paksi-y kedua.

## Apa yang anda pelajari

- `.rolling(window=5).mean()` melicinkan siri masa yang bising supaya aliran kelihatan.
- Matplotlib boleh meletakkan garisan di atas plot serak dan menggunakan dua paksi-y (`twinx`).
- `np.arange` menjana tanda pada langkah tetap.
- Warna bernama seperti `dodgerblue` dan `crimson` menjadikan carta mudah dibaca.

Sebelumnya: [Step-3-Bar-and-Donut-Charts](Step-3-Bar-and-Donut-Charts-ms) · Seterusnya: [Step-5-Choropleth-Map](Step-5-Choropleth-Map-ms)
