[English](Step-4-Trends-over-Time) · **Dansk** · [Bahasa Malaysia](Step-4-Trends-over-Time-ms)

# Trin 4: Tendenser over tid med Matplotlib

**Spørgsmål:** Uddeles der flere priser nu end da prisen blev oprettet, og deles priserne mere end før?

![Trin 4: Tendenser over tid med Matplotlib](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/step-4-trends-over-time.jpg)

*Lektion 586*

![chart-step-4-prizes-per-year.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/chart-step-4-prizes-per-year.png)


## Hvad koden gør

`prizes_per_year` tæller priserne i hvert år (toppen er **15 i 2001**). `rolling_average` udjævner dem med et 5-årigt vindue, så de første fire værdier er NaN. Diagrammet tegner punkterne i `dodgerblue` og gennemsnittet i `crimson` med et mærke hvert 5. år fra 1900 til 2020 lavet med NumPy. `average_share_per_year` og dets glidende gennemsnit viser om andelen pr. modtager ændrer sig, tegnet på en anden y-akse.

## Hvad du lærte

- `.rolling(window=5).mean()` udjævner en støjende tidsserie, så tendensen træder frem.
- Matplotlib kan lægge en linje oven på et punktdiagram og bruge to y-akser (`twinx`).
- `np.arange` laver mærker med faste mellemrum.
- Navngivne farver som `dodgerblue` og `crimson` gør diagrammer læsbare.

Forrige: [Step-3-Bar-and-Donut-Charts](Step-3-Bar-and-Donut-Charts-da) · Næste: [Step-5-Choropleth-Map](Step-5-Choropleth-Map-da)
