[English](Step-3-Bar-and-Donut-Charts) · [Dansk](Step-3-Bar-and-Donut-Charts-da) · **Bahasa Malaysia**

# Langkah 3: Carta bar dan donat dengan plotly

**Soalan:** Kategori mana memberi paling banyak hadiah, dan berapa peratus penerima adalah wanita?

![Langkah 3: Carta bar dan donat dengan plotly](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/step-3-bar-and-donut-charts.jpg)

*Kuliah 585*

![chart-step-3-donut.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/chart-step-3-donut.png)

![chart-step-3-categories.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/chart-step-3-categories.png)


## Apa yang kod lakukan

`sex_counts` memberi 876 lelaki dan 58 wanita, maka `women_percentage` ialah **6.21 %** (dipaparkan sebagai carta donat). `first_female_laureates` menemui Marie Curie (Fizik, 1903), Bertha von Suttner (Keamanan, 1905) dan Selma Lagerlöf (Kesusasteraan, 1909). `repeat_winners` menyenaraikan yang menang lebih sekali: Marie Curie, Linus Pauling, John Bardeen, Frederick Sanger, Palang Merah (tiga kali) dan UNHCR. `number_of_categories` ialah **6**; `prizes_per_category` menyusun Perubatan (222), Fizik (216), Kimia (186), Keamanan (135), Kesusasteraan (117) dan Ekonomi (86). `first_prize_in_category` menunjukkan hadiah Ekonomi pertama pada **1969**. `prizes_by_category_and_sex` menyuap carta bar bertindan.

## Apa yang anda pelajari

- Carta donat ialah carta pai dengan `hole` ditetapkan.
- Carta bar boleh diwarnakan dengan skala warna bernama (`Aggrnyl`) tanpa menunjukkan paksi warna.
- `.groupby()` dengan `.agg()` mengira baris bagi setiap kumpulan; `.value_counts()` ialah jalan pintas.
- Bertanya soalan yang baik kepada data ialah kemahiran tersendiri, dan data tidak dapat menjawab semua soalan.

Sebelumnya: [Step-2-Explore-and-Clean](Step-2-Explore-and-Clean-ms) · Seterusnya: [Step-4-Trends-over-Time](Step-4-Trends-over-Time-ms)
