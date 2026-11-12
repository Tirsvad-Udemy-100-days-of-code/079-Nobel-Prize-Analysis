[English](Step-7-Laureate-Age) · **Dansk** · [Bahasa Malaysia](Step-7-Laureate-Age-ms)

# Trin 7: Modtagernes alder

**Spørgsmål:** Hvor gamle er modtagerne, når de vinder prisen, varierer det efter kategori, og hvordan har det ændret sig over tid?

![Trin 7: Modtagernes alder](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/step-7-laureate-age.jpg)

*Lektion 589*

![chart-step-7-age-histogram.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-7-age-histogram.png)


## Hvad koden gør

`add_winning_age` tilføjer `winning_age`, ceremoniåret minus fødselsåret. `oldest_and_youngest` finder den ældste vinder, John Goodenough (kemi, **97**), og den yngste, Malala Yousafzai (fred, **17**). `age_statistics` giver et gennemsnit på **59,95** år og en 75. percentil på **69**: tre fjerdedele af modtagerne er yngre end 69. Diagrammerne er et Seaborn-histogram, et `.regplot()` af alder mod år, et boksplot pr. kategori og `.lmplot()` med `row` pr. kategori og `lowess=True`.

## Hvad du lærte

- Datoregning: `.dt.year` på en datetime-kolonne.
- `.describe()` giver antal, gennemsnit, kvartiler og ekstremer i ét kald; `.idxmax()` og `.idxmin()` finder rækkerne for ekstremerne.
- Et histogram viser en fordeling; antallet af intervaller ændrer billedet.
- En regressionslinje med `lowess` følger en tendens uden at antage en ret linje; `row` og `hue` opdeler den efter kategori.
- Boksplot og tidsserier viser forskellige billeder af de samme data.

Forrige: [Step-6-Sunburst-Charts](Step-6-Sunburst-Charts-da) · Næste: [Summary](Summary-da)
