[English](Step-3-Bar-and-Donut-Charts) · **Dansk** · [Bahasa Malaysia](Step-3-Bar-and-Donut-Charts-ms)

# Trin 3: Søjle- og donutdiagrammer med plotly

**Spørgsmål:** Hvilke kategorier uddeler flest priser, og hvor stor en andel af modtagerne er kvinder?

![Trin 3: Søjle- og donutdiagrammer med plotly](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/step-3-bar-and-donut-charts.jpg)

*Lektion 585*

![chart-step-3-donut.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/chart-step-3-donut.png)

![chart-step-3-categories.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/chart-step-3-categories.png)


## Hvad koden gør

`sex_counts` giver 876 mænd og 58 kvinder, så `women_percentage` er **6,21 %** (vist som donutdiagram). `first_female_laureates` finder Marie Curie (fysik, 1903), Bertha von Suttner (fred, 1905) og Selma Lagerlöf (litteratur, 1909). `repeat_winners` viser dem, der vandt mere end én gang: Marie Curie, Linus Pauling, John Bardeen, Frederick Sanger, Røde Kors (tre gange) og UNHCR. `number_of_categories` er **6**; `prizes_per_category` rangerer medicin (222), fysik (216), kemi (186), fred (135), litteratur (117) og økonomi (86). `first_prize_in_category` viser den første økonomipris i **1969**. `prizes_by_category_and_sex` bruges til det stablede søjlediagram.

## Hvad du lærte

- Et donutdiagram er et cirkeldiagram med `hole` sat.
- Et søjlediagram kan farves med en navngiven farveskala (`Aggrnyl`) uden at vise farveaksen.
- `.groupby()` med `.agg()` tæller rækker pr. gruppe; `.value_counts()` er genvejen.
- At stille gode spørgsmål til data er en færdighed i sig selv, og data kan ikke besvare alle spørgsmål.

Forrige: [Step-2-Explore-and-Clean](Step-2-Explore-and-Clean-da) · Næste: [Step-4-Trends-over-Time](Step-4-Trends-over-Time-da)
