[English](Step-6-Sunburst-Charts) · [Dansk](Step-6-Sunburst-Charts-da) · **Bahasa Malaysia**

# Langkah 6: Carta sunburst lokasi penyelidikan

**Soalan:** Organisasi penyelidikan dan bandar mana mempunyai paling ramai penerima semasa penemuan dibuat?

![Langkah 6: Carta sunburst lokasi penyelidikan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/step-6-sunburst-charts.jpg)

*Kuliah 588*

![chart-step-6-sunburst.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-6-sunburst.png)


## Apa yang kod lakukan

`top_organisations` menyusun University of California (**40**), Harvard University (**29**), Stanford University (23), MIT (21) dan University of Chicago (**20**). `top_organisation_cities` meletakkan Cambridge, MA dahulu (50) sebelum New York (45) dan Cambridge di United Kingdom (31). `top_birth_cities` menemui New York (53), Paris (26) dan London (19). `sunburst_data` mengumpulkan hadiah mengikut negara organisasi, bandar dan organisasi, dan carta sunburst menunjukkan hierarki itu dengan `px.sunburst`.

## Apa yang anda pelajari

- Menggunakan semula satu corak (`.groupby().agg()` kemudian `.sort_values()`) untuk organisasi, bandar dan bandar kelahiran.
- `.dropna()` sebelum mengumpulkan hierarki.
- Carta sunburst menunjukkan hubungan bahagian-kepada-keseluruhan merentas beberapa peringkat dan menggalakkan penerokaan dengan klik.
- Soalan berbeza menunjuk ke tempat berbeza: tempat lahir bukan tempat bekerja.

Sebelumnya: [Step-5-Choropleth-Map](Step-5-Choropleth-Map-ms) · Seterusnya: [Step-7-Laureate-Age](Step-7-Laureate-Age-ms)
