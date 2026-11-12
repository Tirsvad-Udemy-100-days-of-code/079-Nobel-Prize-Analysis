[English](Step-5-Choropleth-Map) · [Dansk](Step-5-Choropleth-Map-da) · **Bahasa Malaysia**

# Langkah 5: Peta choropleth dan negara teratas

**Soalan:** Negara mana memenangi paling banyak hadiah, dan dalam kategori apa?

![Langkah 5: Peta choropleth dan negara teratas](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/step-5-choropleth-map.jpg)

*Kuliah 587*

![chart-step-5-choropleth.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-5-choropleth.png)


## Apa yang kod lakukan

`top20_countries` mengira hadiah bagi setiap `birth_country_current`: Amerika Syarikat mendahului dengan **281**, diikuti United Kingdom (105), Jerman (84), Perancis (57) dan Sweden (29). Lajur `birth_country_current` paling kurang bermasalah: `birth_country` mengandungi negara yang sudah tiada dan `organization_country` banyak nilai NaN. `prizes_per_country_iso` menyuap peta choropleth melalui lajur `ISO`, `prizes_by_country_and_category` membahagikan bar mengikut kategori dan `cumulative_prizes_by_country` menggunakan `.cumsum()` untuk menunjukkan bagaimana pendahulu berubah dari masa ke masa.

## Apa yang anda pelajari

- Memilih lajur yang betul penting: setiap calon ada masalahnya sendiri.
- Carta bar mendatar menyusun negara dengan jelas.
- `px.choropleth` mewarnakan peta daripada kod negara ISO.
- Menindan carta bar mengikut kategori menunjukkan apa yang membentuk setiap jumlah.
- `.cumsum()` selepas `.groupby()` memberi jumlah berjalan bagi setiap kumpulan.

Sebelumnya: [Step-4-Trends-over-Time](Step-4-Trends-over-Time-ms) · Seterusnya: [Step-6-Sunburst-Charts](Step-6-Sunburst-Charts-ms)
