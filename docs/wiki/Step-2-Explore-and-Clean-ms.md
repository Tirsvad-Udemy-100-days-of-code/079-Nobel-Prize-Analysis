[English](Step-2-Explore-and-Clean) · [Dansk](Step-2-Explore-and-Clean-da) · **Bahasa Malaysia**

# Langkah 2: Teroka dan bersihkan set data

**Soalan:** Apakah bentuk data, adakah ada pendua atau nilai NaN, dan bagaimana menjadikan lajur boleh digunakan?

![Langkah 2: Teroka dan bersihkan set data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/step-2-explore-and-clean.jpg)

*Kuliah 584*


## Apa yang kod lakukan

`data_shape` memberi **962 baris dan 16 lajur**. `first_year` ialah **1901** dan `last_year` ialah **2020**. `count_duplicates` menemui **0** pendua. `nan_per_column` menunjukkan di mana nilai hilang: `organization_name` dan `organization_city` (255), `organization_country` (254), `motivation` (88), `birth_city` (31) dan 28 bagi setiap satu `birth_date`, `sex`, `birth_country`, `birth_country_current` dan `ISO`. `convert_birth_date` menukar `birth_date` kepada datetime dan `add_share_pct` menukar bahagian seperti `1/2` kepada `50.0`.

## Apa yang anda pelajari

- `.shape`, `.head()` dan `.tail()` memberi gambaran pertama tentang jadual.
- `.duplicated()` dan `.isna().sum()` mencari pendua dan nilai hilang.
- Nilai NaN selalunya ada sebab: organisasi tiada data kelahiran, dan penerima Kesusasteraan dan Keamanan sering tiada organisasi penyelidikan.
- `pd.to_datetime` menukar teks kepada tarikh; `.map()` membina lajur baharu daripada yang lama.
- Dalam Google Colab anda perlu menaik taraf plotly dahulu; di sini kebergantungan itu dinyatakan dalam `pyproject.toml`.

Sebelumnya: [Step-1-Goals](Step-1-Goals-ms) · Seterusnya: [Step-3-Bar-and-Donut-Charts](Step-3-Bar-and-Donut-Charts-ms)
