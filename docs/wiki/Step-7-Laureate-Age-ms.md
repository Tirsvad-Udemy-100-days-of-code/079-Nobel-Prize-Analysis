[English](Step-7-Laureate-Age) · [Dansk](Step-7-Laureate-Age-da) · **Bahasa Malaysia**

# Langkah 7: Umur para penerima

**Soalan:** Berapa umur penerima semasa memenangi hadiah, adakah ia berbeza mengikut kategori, dan bagaimana ia berubah dari masa ke masa?

![Langkah 7: Umur para penerima](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/step-7-laureate-age.jpg)

*Kuliah 589*

![chart-step-7-age-histogram.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-7-age-histogram.png)


## Apa yang kod lakukan

`add_winning_age` menambah `winning_age`, tahun upacara tolak tahun lahir. `oldest_and_youngest` menemui pemenang tertua, John Goodenough (Kimia, **97**), dan termuda, Malala Yousafzai (Keamanan, **17**). `age_statistics` memberi purata **59.95** tahun dan persentil ke-75 **69**: tiga suku penerima berumur kurang daripada 69. Carta ialah histogram Seaborn, `.regplot()` umur berbanding tahun, plot kotak bagi setiap kategori dan `.lmplot()` dengan `row` bagi setiap kategori dan `lowess=True`.

## Apa yang anda pelajari

- Aritmetik tarikh: `.dt.year` pada lajur datetime.
- `.describe()` memberi kiraan, purata, kuartil dan nilai ekstrem dalam satu panggilan; `.idxmax()` dan `.idxmin()` mencari baris nilai ekstrem.
- Histogram menunjukkan taburan; bilangan bin mengubah gambaran.
- Garis regresi dengan `lowess` mengikut aliran tanpa mengandaikan garis lurus; `row` dan `hue` memecahkannya mengikut kategori.
- Plot kotak dan siri masa menunjukkan gambaran berbeza bagi data yang sama.

Sebelumnya: [Step-6-Sunburst-Charts](Step-6-Sunburst-Charts-ms) · Seterusnya: [Summary](Summary-ms)
