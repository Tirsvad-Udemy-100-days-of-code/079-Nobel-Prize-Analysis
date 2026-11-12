"""Generate the flat three-language wiki in docs/wiki/."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "wiki"
OUT.mkdir(parents=True, exist_ok=True)
IMG = "https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/"
LANGS = [("en", "English", ""), ("da", "Dansk", "-da"), ("ms", "Bahasa Malaysia", "-ms")]
LBL = {
    "en": dict(q="Question", code="What the code does", gain="What you gained", prev="Previous", next="Next", lec="Lecture"),
    "da": dict(q="Spørgsmål", code="Hvad koden gør", gain="Hvad du lærte", prev="Forrige", next="Næste", lec="Lektion"),
    "ms": dict(q="Soalan", code="Apa yang kod lakukan", gain="Apa yang anda pelajari", prev="Sebelumnya", next="Seterusnya", lec="Kuliah"),
}

STEPS = [
    dict(
        slug="Step-1-Goals", img="step-1-goals.jpg", lec="583",
        title=dict(en="Step 1: The goals of the day", da="Trin 1: Dagens mål", ms="Langkah 1: Matlamat hari ini"),
        short=dict(en="Step 1 Goals", da="Trin 1 Mål", ms="Langkah 1 Matlamat"),
        gain_line=dict(en="What will we build, and which tools do we need?", da="Hvad skal vi bygge, og hvilke værktøjer skal vi bruge?", ms="Apa yang akan kita bina, dan alat apa yang diperlukan?"),
        q=dict(en="What do we analyse today, and what will we learn?", da="Hvad analyserer vi i dag, og hvad lærer vi?", ms="Apa yang kita analisis hari ini, dan apa yang akan kita pelajari?"),
        code=dict(
            en="The repository already holds the data set (`data/nobel_prize_data.csv`: 962 prizes from 1901 to 2020) and the notebook (`notebooks/Nobel_Prize_Analysis.ipynb`). `load_nobel()` reads the file; no Google Colab is needed.",
            da="Repositoriet indeholder allerede datasættet (`data/nobel_prize_data.csv`: 962 priser fra 1901 til 2020) og notebooken (`notebooks/Nobel_Prize_Analysis.ipynb`). `load_nobel()` læser filen; Google Colab er ikke nødvendig.",
            ms="Repositori ini sudah mengandungi set data (`data/nobel_prize_data.csv`: 962 hadiah dari 1901 hingga 2020) dan buku nota (`notebooks/Nobel_Prize_Analysis.ipynb`). `load_nobel()` membaca fail itu; Google Colab tidak diperlukan.",
        ),
        gain=dict(
            en=["The aim: find patterns in the past winners of the Nobel Prize.", "The tools of the day: a choropleth map, plotly bar and sunburst charts, Seaborn `.lmplot()` with `row`, `hue` and `lowess`, and a Seaborn histogram.", "The same data tells different stories depending on how you look at it (box plot against time series)."],
            da=["Målet: finde mønstre hos tidligere Nobelprismodtagere.", "Dagens værktøjer: et choropleth-kort, plotly-søjle- og sunburst-diagrammer, Seaborn `.lmplot()` med `row`, `hue` og `lowess` samt et Seaborn-histogram.", "De samme data fortæller forskellige historier, afhængigt af hvordan man ser på dem (boksplot mod tidsserie)."],
            ms=["Matlamat: mencari corak pada pemenang Hadiah Nobel yang lalu.", "Alat hari ini: peta choropleth, carta bar dan sunburst plotly, Seaborn `.lmplot()` dengan `row`, `hue` dan `lowess`, dan histogram Seaborn.", "Data yang sama menceritakan kisah berbeza bergantung pada cara kita melihatnya (plot kotak berbanding siri masa)."],
        ),
    ),
    dict(
        slug="Step-2-Explore-and-Clean", img="step-2-explore-and-clean.jpg", lec="584",
        title=dict(en="Step 2: Explore and clean the data set", da="Trin 2: Udforsk og rens datasættet", ms="Langkah 2: Teroka dan bersihkan set data"),
        short=dict(en="Step 2 Explore and Clean", da="Trin 2 Udforsk og Rens", ms="Langkah 2 Teroka dan Bersih"),
        gain_line=dict(en="What does the data look like, and what is missing?", da="Hvordan ser data ud, og hvad mangler?", ms="Bagaimana rupa data, dan apa yang tiada?"),
        q=dict(en="What is the shape of the data, are there duplicates or NaN values, and how do we make the columns usable?", da="Hvilken form har data, er der dubletter eller NaN-værdier, og hvordan gør vi kolonnerne brugbare?", ms="Apakah bentuk data, adakah ada pendua atau nilai NaN, dan bagaimana menjadikan lajur boleh digunakan?"),
        code=dict(
            en="`data_shape` gives **962 rows and 16 columns**. `first_year` is **1901** and `last_year` is **2020**. `count_duplicates` finds **0** duplicates. `nan_per_column` shows where values are missing: `organization_name` and `organization_city` (255), `organization_country` (254), `motivation` (88), `birth_city` (31) and 28 each for `birth_date`, `sex`, `birth_country`, `birth_country_current` and `ISO`. `convert_birth_date` makes `birth_date` a datetime and `add_share_pct` turns a share such as `1/2` into `50.0`.",
            da="`data_shape` giver **962 rækker og 16 kolonner**. `first_year` er **1901** og `last_year` er **2020**. `count_duplicates` finder **0** dubletter. `nan_per_column` viser hvor der mangler værdier: `organization_name` og `organization_city` (255), `organization_country` (254), `motivation` (88), `birth_city` (31) og 28 hver for `birth_date`, `sex`, `birth_country`, `birth_country_current` og `ISO`. `convert_birth_date` gør `birth_date` til en datetime, og `add_share_pct` omdanner en andel som `1/2` til `50.0`.",
            ms="`data_shape` memberi **962 baris dan 16 lajur**. `first_year` ialah **1901** dan `last_year` ialah **2020**. `count_duplicates` menemui **0** pendua. `nan_per_column` menunjukkan di mana nilai hilang: `organization_name` dan `organization_city` (255), `organization_country` (254), `motivation` (88), `birth_city` (31) dan 28 bagi setiap satu `birth_date`, `sex`, `birth_country`, `birth_country_current` dan `ISO`. `convert_birth_date` menukar `birth_date` kepada datetime dan `add_share_pct` menukar bahagian seperti `1/2` kepada `50.0`.",
        ),
        gain=dict(
            en=["`.shape`, `.head()` and `.tail()` give a first impression of a table.", "`.duplicated()` and `.isna().sum()` find duplicates and missing values.", "NaN values often have a reason: organisations have no birth data, and Literature and Peace laureates often have no research organisation.", "`pd.to_datetime` converts text to dates; `.map()` builds a new column from an old one.", "In Google Colab you would upgrade plotly first; here the dependency is declared in `pyproject.toml`."],
            da=["`.shape`, `.head()` og `.tail()` giver et første indtryk af en tabel.", "`.duplicated()` og `.isna().sum()` finder dubletter og manglende værdier.", "NaN-værdier har ofte en årsag: organisationer har ingen fødselsdata, og litteratur- og fredsprismodtagere har ofte ingen forskningsorganisation.", "`pd.to_datetime` omdanner tekst til datoer; `.map()` bygger en ny kolonne ud fra en gammel.", "I Google Colab skulle man opgradere plotly først; her er afhængigheden angivet i `pyproject.toml`."],
            ms=["`.shape`, `.head()` dan `.tail()` memberi gambaran pertama tentang jadual.", "`.duplicated()` dan `.isna().sum()` mencari pendua dan nilai hilang.", "Nilai NaN selalunya ada sebab: organisasi tiada data kelahiran, dan penerima Kesusasteraan dan Keamanan sering tiada organisasi penyelidikan.", "`pd.to_datetime` menukar teks kepada tarikh; `.map()` membina lajur baharu daripada yang lama.", "Dalam Google Colab anda perlu menaik taraf plotly dahulu; di sini kebergantungan itu dinyatakan dalam `pyproject.toml`."],
        ),
    ),
    dict(
        slug="Step-3-Bar-and-Donut-Charts", img="step-3-bar-and-donut-charts.jpg", lec="585",
        title=dict(en="Step 3: Bar and donut charts with plotly", da="Trin 3: Søjle- og donutdiagrammer med plotly", ms="Langkah 3: Carta bar dan donat dengan plotly"),
        short=dict(en="Step 3 Bar and Donut Charts", da="Trin 3 Søjle- og Donutdiagrammer", ms="Langkah 3 Carta Bar dan Donat"),
        gain_line=dict(en="Which categories award most prizes, and how many prizes went to women?", da="Hvilke kategorier uddeler flest priser, og hvor mange gik til kvinder?", ms="Kategori mana memberi paling banyak hadiah, dan berapa banyak kepada wanita?"),
        q=dict(en="Which categories award the most prizes, and what share of the laureates are women?", da="Hvilke kategorier uddeler flest priser, og hvor stor en andel af modtagerne er kvinder?", ms="Kategori mana memberi paling banyak hadiah, dan berapa peratus penerima adalah wanita?"),
        code=dict(
            en="`sex_counts` gives 876 men and 58 women, so `women_percentage` is **6.21 %** (shown as a donut chart). `first_female_laureates` finds Marie Curie (Physics, 1903), Bertha von Suttner (Peace, 1905) and Selma Lagerlöf (Literature, 1909). `repeat_winners` lists those who won more than once: Marie Curie, Linus Pauling, John Bardeen, Frederick Sanger, the Red Cross (three times) and the UNHCR. `number_of_categories` is **6**; `prizes_per_category` ranks Medicine (222), Physics (216), Chemistry (186), Peace (135), Literature (117) and Economics (86). `first_prize_in_category` shows the first Economics prize in **1969**. `prizes_by_category_and_sex` feeds the stacked bar chart.",
            da="`sex_counts` giver 876 mænd og 58 kvinder, så `women_percentage` er **6,21 %** (vist som donutdiagram). `first_female_laureates` finder Marie Curie (fysik, 1903), Bertha von Suttner (fred, 1905) og Selma Lagerlöf (litteratur, 1909). `repeat_winners` viser dem, der vandt mere end én gang: Marie Curie, Linus Pauling, John Bardeen, Frederick Sanger, Røde Kors (tre gange) og UNHCR. `number_of_categories` er **6**; `prizes_per_category` rangerer medicin (222), fysik (216), kemi (186), fred (135), litteratur (117) og økonomi (86). `first_prize_in_category` viser den første økonomipris i **1969**. `prizes_by_category_and_sex` bruges til det stablede søjlediagram.",
            ms="`sex_counts` memberi 876 lelaki dan 58 wanita, maka `women_percentage` ialah **6.21 %** (dipaparkan sebagai carta donat). `first_female_laureates` menemui Marie Curie (Fizik, 1903), Bertha von Suttner (Keamanan, 1905) dan Selma Lagerlöf (Kesusasteraan, 1909). `repeat_winners` menyenaraikan yang menang lebih sekali: Marie Curie, Linus Pauling, John Bardeen, Frederick Sanger, Palang Merah (tiga kali) dan UNHCR. `number_of_categories` ialah **6**; `prizes_per_category` menyusun Perubatan (222), Fizik (216), Kimia (186), Keamanan (135), Kesusasteraan (117) dan Ekonomi (86). `first_prize_in_category` menunjukkan hadiah Ekonomi pertama pada **1969**. `prizes_by_category_and_sex` menyuap carta bar bertindan.",
        ),
        gain=dict(
            en=["A donut chart is a pie chart with `hole` set.", "A bar chart can be coloured with a named colour scale (`Aggrnyl`) without showing the colour axis.", "`.groupby()` with `.agg()` counts rows per group; `.value_counts()` is the shortcut.", "Asking good questions of the data is a skill of its own, and the data cannot answer every question."],
            da=["Et donutdiagram er et cirkeldiagram med `hole` sat.", "Et søjlediagram kan farves med en navngiven farveskala (`Aggrnyl`) uden at vise farveaksen.", "`.groupby()` med `.agg()` tæller rækker pr. gruppe; `.value_counts()` er genvejen.", "At stille gode spørgsmål til data er en færdighed i sig selv, og data kan ikke besvare alle spørgsmål."],
            ms=["Carta donat ialah carta pai dengan `hole` ditetapkan.", "Carta bar boleh diwarnakan dengan skala warna bernama (`Aggrnyl`) tanpa menunjukkan paksi warna.", "`.groupby()` dengan `.agg()` mengira baris bagi setiap kumpulan; `.value_counts()` ialah jalan pintas.", "Bertanya soalan yang baik kepada data ialah kemahiran tersendiri, dan data tidak dapat menjawab semua soalan."],
        ),
    ),
    dict(
        slug="Step-4-Trends-over-Time", img="step-4-trends-over-time.jpg", lec="586",
        title=dict(en="Step 4: Trends over time with Matplotlib", da="Trin 4: Tendenser over tid med Matplotlib", ms="Langkah 4: Aliran dari masa ke masa dengan Matplotlib"),
        short=dict(en="Step 4 Trends over Time", da="Trin 4 Tendenser over Tid", ms="Langkah 4 Aliran Masa"),
        gain_line=dict(en="Are more prizes awarded now than in the beginning?", da="Uddeles der flere priser nu end i begyndelsen?", ms="Adakah lebih banyak hadiah diberikan sekarang berbanding permulaan?"),
        q=dict(en="Are more prizes awarded recently than when the prize was created, and are prizes shared more than before?", da="Uddeles der flere priser nu end da prisen blev oprettet, og deles priserne mere end før?", ms="Adakah lebih banyak hadiah diberikan kebelakangan ini berbanding semasa hadiah diwujudkan, dan adakah hadiah dikongsi lebih ramai?"),
        code=dict(
            en="`prizes_per_year` counts the prizes of each year (the peak is **15 in 2001**). `rolling_average` smooths them with a 5 year window, so the first four values are NaN. The chart draws the points in `dodgerblue` and the average in `crimson`, with a tick every 5 years from 1900 to 2020 made with NumPy. `average_share_per_year` and its rolling average show whether the share per winner changes, drawn on a second y-axis.",
            da="`prizes_per_year` tæller priserne i hvert år (toppen er **15 i 2001**). `rolling_average` udjævner dem med et 5-årigt vindue, så de første fire værdier er NaN. Diagrammet tegner punkterne i `dodgerblue` og gennemsnittet i `crimson` med et mærke hvert 5. år fra 1900 til 2020 lavet med NumPy. `average_share_per_year` og dets glidende gennemsnit viser om andelen pr. modtager ændrer sig, tegnet på en anden y-akse.",
            ms="`prizes_per_year` mengira hadiah setiap tahun (kemuncak **15 pada 2001**). `rolling_average` melicinkannya dengan tetingkap 5 tahun, jadi empat nilai pertama ialah NaN. Carta melukis titik dengan `dodgerblue` dan purata dengan `crimson`, dengan tanda setiap 5 tahun dari 1900 hingga 2020 dibuat dengan NumPy. `average_share_per_year` dan purata bergulirnya menunjukkan sama ada bahagian setiap pemenang berubah, dilukis pada paksi-y kedua.",
        ),
        gain=dict(
            en=["`.rolling(window=5).mean()` smooths a noisy time series so the trend shows.", "Matplotlib can superimpose a line on a scatter plot and use two y-axes (`twinx`).", "`np.arange` generates tick marks at regular steps.", "Named colours such as `dodgerblue` and `crimson` make charts readable."],
            da=["`.rolling(window=5).mean()` udjævner en støjende tidsserie, så tendensen træder frem.", "Matplotlib kan lægge en linje oven på et punktdiagram og bruge to y-akser (`twinx`).", "`np.arange` laver mærker med faste mellemrum.", "Navngivne farver som `dodgerblue` og `crimson` gør diagrammer læsbare."],
            ms=["`.rolling(window=5).mean()` melicinkan siri masa yang bising supaya aliran kelihatan.", "Matplotlib boleh meletakkan garisan di atas plot serak dan menggunakan dua paksi-y (`twinx`).", "`np.arange` menjana tanda pada langkah tetap.", "Warna bernama seperti `dodgerblue` dan `crimson` menjadikan carta mudah dibaca."],
        ),
    ),
    dict(
        slug="Step-5-Choropleth-Map", img="step-5-choropleth-map.jpg", lec="587",
        title=dict(en="Step 5: A choropleth map and the top countries", da="Trin 5: Et choropleth-kort og de bedste lande", ms="Langkah 5: Peta choropleth dan negara teratas"),
        short=dict(en="Step 5 Choropleth Map", da="Trin 5 Choropleth-kort", ms="Langkah 5 Peta Choropleth"),
        gain_line=dict(en="Which countries win the most prizes?", da="Hvilke lande vinder flest priser?", ms="Negara mana memenangi paling banyak hadiah?"),
        q=dict(en="Which countries win the most prizes, and in which categories?", da="Hvilke lande vinder flest priser, og i hvilke kategorier?", ms="Negara mana memenangi paling banyak hadiah, dan dalam kategori apa?"),
        code=dict(
            en="`top20_countries` counts prizes per `birth_country_current`: the United States of America leads with **281**, followed by the United Kingdom (105), Germany (84), France (57) and Sweden (29). The column `birth_country_current` is the least problematic: `birth_country` contains countries that no longer exist and `organization_country` has many NaN values. `prizes_per_country_iso` feeds the choropleth map through the `ISO` column, `prizes_by_country_and_category` splits the bars by category and `cumulative_prizes_by_country` uses `.cumsum()` to show how the lead changed over time.",
            da="`top20_countries` tæller priser pr. `birth_country_current`: USA fører med **281**, efterfulgt af Storbritannien (105), Tyskland (84), Frankrig (57) og Sverige (29). Kolonnen `birth_country_current` er den mindst problematiske: `birth_country` indeholder lande, der ikke længere findes, og `organization_country` har mange NaN-værdier. `prizes_per_country_iso` fodrer choropleth-kortet via kolonnen `ISO`, `prizes_by_country_and_category` deler søjlerne op efter kategori, og `cumulative_prizes_by_country` bruger `.cumsum()` til at vise hvordan føringen skiftede over tid.",
            ms="`top20_countries` mengira hadiah bagi setiap `birth_country_current`: Amerika Syarikat mendahului dengan **281**, diikuti United Kingdom (105), Jerman (84), Perancis (57) dan Sweden (29). Lajur `birth_country_current` paling kurang bermasalah: `birth_country` mengandungi negara yang sudah tiada dan `organization_country` banyak nilai NaN. `prizes_per_country_iso` menyuap peta choropleth melalui lajur `ISO`, `prizes_by_country_and_category` membahagikan bar mengikut kategori dan `cumulative_prizes_by_country` menggunakan `.cumsum()` untuk menunjukkan bagaimana pendahulu berubah dari masa ke masa.",
        ),
        gain=dict(
            en=["Choosing the right column matters: every candidate has its own problems.", "A horizontal bar chart ranks countries clearly.", "`px.choropleth` colours a map from ISO country codes.", "Stacking a bar chart by category shows what makes up each total.", "`.cumsum()` after `.groupby()` gives a running total per group."],
            da=["Det betyder noget at vælge den rigtige kolonne: hver kandidat har sine problemer.", "Et vandret søjlediagram rangerer lande tydeligt.", "`px.choropleth` farver et kort ud fra ISO-landekoder.", "At stable et søjlediagram efter kategori viser hvad hver total består af.", "`.cumsum()` efter `.groupby()` giver en løbende sum pr. gruppe."],
            ms=["Memilih lajur yang betul penting: setiap calon ada masalahnya sendiri.", "Carta bar mendatar menyusun negara dengan jelas.", "`px.choropleth` mewarnakan peta daripada kod negara ISO.", "Menindan carta bar mengikut kategori menunjukkan apa yang membentuk setiap jumlah.", "`.cumsum()` selepas `.groupby()` memberi jumlah berjalan bagi setiap kumpulan."],
        ),
    ),
    dict(
        slug="Step-6-Sunburst-Charts", img="step-6-sunburst-charts.jpg", lec="588",
        title=dict(en="Step 6: Sunburst charts of research locations", da="Trin 6: Sunburst-diagrammer over forskningssteder", ms="Langkah 6: Carta sunburst lokasi penyelidikan"),
        short=dict(en="Step 6 Sunburst Charts", da="Trin 6 Sunburst-diagrammer", ms="Langkah 6 Carta Sunburst"),
        gain_line=dict(en="Which institutions and cities are hot spots for discoveries?", da="Hvilke institutioner og byer er hotspots for opdagelser?", ms="Institusi dan bandar mana menjadi tumpuan penemuan?"),
        q=dict(en="Which research organisations and cities had the most laureates at the time of the discovery?", da="Hvilke forskningsorganisationer og byer havde flest modtagere da opdagelsen blev gjort?", ms="Organisasi penyelidikan dan bandar mana mempunyai paling ramai penerima semasa penemuan dibuat?"),
        code=dict(
            en="`top_organisations` ranks the University of California (**40**), Harvard University (**29**), Stanford University (23), MIT (21) and the University of Chicago (**20**). `top_organisation_cities` puts Cambridge, MA first (50) before New York (45) and Cambridge in the United Kingdom (31). `top_birth_cities` finds New York (53), Paris (26) and London (19). `sunburst_data` groups prizes by organisation country, city and organisation, and the sunburst chart shows that hierarchy with `px.sunburst`.",
            da="`top_organisations` rangerer University of California (**40**), Harvard University (**29**), Stanford University (23), MIT (21) og University of Chicago (**20**). `top_organisation_cities` sætter Cambridge, MA først (50) før New York (45) og Cambridge i Storbritannien (31). `top_birth_cities` finder New York (53), Paris (26) og London (19). `sunburst_data` grupperer priser efter organisationens land, by og organisation, og sunburst-diagrammet viser hierarkiet med `px.sunburst`.",
            ms="`top_organisations` menyusun University of California (**40**), Harvard University (**29**), Stanford University (23), MIT (21) dan University of Chicago (**20**). `top_organisation_cities` meletakkan Cambridge, MA dahulu (50) sebelum New York (45) dan Cambridge di United Kingdom (31). `top_birth_cities` menemui New York (53), Paris (26) dan London (19). `sunburst_data` mengumpulkan hadiah mengikut negara organisasi, bandar dan organisasi, dan carta sunburst menunjukkan hierarki itu dengan `px.sunburst`.",
        ),
        gain=dict(
            en=["Reusing one pattern (`.groupby().agg()` then `.sort_values()`) for organisations, cities and birth cities.", "`.dropna()` before grouping a hierarchy.", "A sunburst chart shows part-to-whole relationships across several levels and invites exploration by clicking.", "Different questions point to different places: where people were born is not where they worked."],
            da=["Samme mønster (`.groupby().agg()` og derefter `.sort_values()`) bruges til organisationer, byer og fødebyer.", "`.dropna()` før et hierarki grupperes.", "Et sunburst-diagram viser del-helhed på flere niveauer og indbyder til at udforske ved at klikke.", "Forskellige spørgsmål peger på forskellige steder: hvor man er født er ikke hvor man arbejdede."],
            ms=["Menggunakan semula satu corak (`.groupby().agg()` kemudian `.sort_values()`) untuk organisasi, bandar dan bandar kelahiran.", "`.dropna()` sebelum mengumpulkan hierarki.", "Carta sunburst menunjukkan hubungan bahagian-kepada-keseluruhan merentas beberapa peringkat dan menggalakkan penerokaan dengan klik.", "Soalan berbeza menunjuk ke tempat berbeza: tempat lahir bukan tempat bekerja."],
        ),
    ),
    dict(
        slug="Step-7-Laureate-Age", img="step-7-laureate-age.jpg", lec="589",
        title=dict(en="Step 7: The age of the laureates", da="Trin 7: Modtagernes alder", ms="Langkah 7: Umur para penerima"),
        short=dict(en="Step 7 Laureate Age", da="Trin 7 Modtagernes Alder", ms="Langkah 7 Umur Penerima"),
        gain_line=dict(en="How old are laureates when they win, and has that changed?", da="Hvor gamle er modtagere, når de vinder, og har det ændret sig?", ms="Berapa umur penerima semasa menang, dan adakah ia berubah?"),
        q=dict(en="How old are the laureates when they win the prize, does it vary by category, and how has it changed over time?", da="Hvor gamle er modtagerne, når de vinder prisen, varierer det efter kategori, og hvordan har det ændret sig over tid?", ms="Berapa umur penerima semasa memenangi hadiah, adakah ia berbeza mengikut kategori, dan bagaimana ia berubah dari masa ke masa?"),
        code=dict(
            en="`add_winning_age` adds `winning_age`, the year of the ceremony minus the birth year. `oldest_and_youngest` finds the oldest winner, John Goodenough (Chemistry, **97**), and the youngest, Malala Yousafzai (Peace, **17**). `age_statistics` gives a mean of **59.95** years and a 75th percentile of **69**: three quarters of the laureates are younger than 69. The charts are a Seaborn histogram, a `.regplot()` of age against year, a box plot per category and `.lmplot()` with `row` per category and `lowess=True`.",
            da="`add_winning_age` tilføjer `winning_age`, ceremoniåret minus fødselsåret. `oldest_and_youngest` finder den ældste vinder, John Goodenough (kemi, **97**), og den yngste, Malala Yousafzai (fred, **17**). `age_statistics` giver et gennemsnit på **59,95** år og en 75. percentil på **69**: tre fjerdedele af modtagerne er yngre end 69. Diagrammerne er et Seaborn-histogram, et `.regplot()` af alder mod år, et boksplot pr. kategori og `.lmplot()` med `row` pr. kategori og `lowess=True`.",
            ms="`add_winning_age` menambah `winning_age`, tahun upacara tolak tahun lahir. `oldest_and_youngest` menemui pemenang tertua, John Goodenough (Kimia, **97**), dan termuda, Malala Yousafzai (Keamanan, **17**). `age_statistics` memberi purata **59.95** tahun dan persentil ke-75 **69**: tiga suku penerima berumur kurang daripada 69. Carta ialah histogram Seaborn, `.regplot()` umur berbanding tahun, plot kotak bagi setiap kategori dan `.lmplot()` dengan `row` bagi setiap kategori dan `lowess=True`.",
        ),
        gain=dict(
            en=["Date arithmetic: `.dt.year` on a datetime column.", "`.describe()` gives count, mean, quartiles and extremes in one call; `.idxmax()` and `.idxmin()` find the rows of the extremes.", "A histogram shows a distribution; the number of bins changes the picture.", "A regression line with `lowess` follows a trend without assuming a straight line; `row` and `hue` split it by category.", "Box plots and time series show different pictures of the same data."],
            da=["Datoregning: `.dt.year` på en datetime-kolonne.", "`.describe()` giver antal, gennemsnit, kvartiler og ekstremer i ét kald; `.idxmax()` og `.idxmin()` finder rækkerne for ekstremerne.", "Et histogram viser en fordeling; antallet af intervaller ændrer billedet.", "En regressionslinje med `lowess` følger en tendens uden at antage en ret linje; `row` og `hue` opdeler den efter kategori.", "Boksplot og tidsserier viser forskellige billeder af de samme data."],
            ms=["Aritmetik tarikh: `.dt.year` pada lajur datetime.", "`.describe()` memberi kiraan, purata, kuartil dan nilai ekstrem dalam satu panggilan; `.idxmax()` dan `.idxmin()` mencari baris nilai ekstrem.", "Histogram menunjukkan taburan; bilangan bin mengubah gambaran.", "Garis regresi dengan `lowess` mengikut aliran tanpa mengandaikan garis lurus; `row` dan `hue` memecahkannya mengikut kategori.", "Plot kotak dan siri masa menunjukkan gambaran berbeza bagi data yang sama."],
        ),
    ),
    dict(
        slug="Summary", img="step-8-summary.jpg", lec="590",
        title=dict(en="Step 8: Learning points and summary", da="Trin 8: Læringspunkter og opsummering", ms="Langkah 8: Pengajaran dan ringkasan"),
        short=dict(en="Summary", da="Opsummering", ms="Ringkasan"),
        gain_line=dict(en="Everything the lecture taught, in one list", da="Alt hvad lektionen lærte, på én liste", ms="Semua yang diajar kuliah, dalam satu senarai"),
        q=dict(en="What did we review, and what did we learn that is new?", da="Hvad repeterede vi, og hvad lærte vi, der er nyt?", ms="Apa yang kita ulang kaji, dan apa yang baharu kita pelajari?"),
        code=dict(
            en="Run `python -m nobel_analysis` to print every answer of the assignment in one report, or open the notebook to see the charts. `python -m pytest` proves each value.",
            da="Kør `python -m nobel_analysis` for at udskrive alle opgavens svar i én rapport, eller åbn notebooken for at se diagrammerne. `python -m pytest` beviser hver værdi.",
            ms="Jalankan `python -m nobel_analysis` untuk mencetak semua jawapan tugasan dalam satu laporan, atau buka buku nota untuk melihat carta. `python -m pytest` membuktikan setiap nilai.",
        ),
        gain=dict(
            en=["Review: finding and explaining NaN values; converting objects and strings to numbers; donut and bar charts with plotly; a rolling average for a time series; `.value_counts()`, `.groupby()`, `.merge()`, `.sort_values()` and `.agg()`.", "New: a choropleth map; bar charts of different segments of the data; sunburst charts; Seaborn `.lmplot()` with `row`, `hue` and `lowess`; a different picture emerges when you look at the same data in different ways; the distribution of the data in a Seaborn histogram."],
            da=["Repetition: at finde og forklare NaN-værdier; at omdanne objekter og strenge til tal; donut- og søjlediagrammer med plotly; glidende gennemsnit for en tidsserie; `.value_counts()`, `.groupby()`, `.merge()`, `.sort_values()` og `.agg()`.", "Nyt: et choropleth-kort; søjlediagrammer af forskellige udsnit af data; sunburst-diagrammer; Seaborn `.lmplot()` med `row`, `hue` og `lowess`; et andet billede træder frem, når man ser på de samme data på forskellige måder; fordelingen af data i et Seaborn-histogram."],
            ms=["Ulang kaji: mencari dan menerangkan nilai NaN; menukar objek dan rentetan kepada nombor; carta donat dan bar dengan plotly; purata bergulir untuk siri masa; `.value_counts()`, `.groupby()`, `.merge()`, `.sort_values()` dan `.agg()`.", "Baharu: peta choropleth; carta bar bagi segmen data berbeza; carta sunburst; Seaborn `.lmplot()` dengan `row`, `hue` dan `lowess`; gambaran berbeza muncul apabila melihat data yang sama dengan cara berbeza; taburan data dalam histogram Seaborn."],
        ),
    ),
]

HOME = dict(
    title=dict(en="Nobel Prize Analysis", da="Nobelprisanalyse", ms="Analisis Hadiah Nobel"),
    intro=dict(
        en="Day 79 of Udemy's *100 Days of Code*: analyse the past winners of the Nobel Prize with Pandas, Plotly, Matplotlib and Seaborn. This wiki explains what each lecture step teaches. Every step has a screenshot of its lecture.",
        da="Dag 79 af Udemys *100 Days of Code*: analysér tidligere vindere af Nobelprisen med Pandas, Plotly, Matplotlib og Seaborn. Denne wiki forklarer hvad hvert trin i lektionen lærer. Hvert trin har et skærmbillede af sin lektion.",
        ms="Hari 79 *100 Days of Code* Udemy: menganalisis pemenang Hadiah Nobel yang lalu dengan Pandas, Plotly, Matplotlib dan Seaborn. Wiki ini menerangkan apa yang diajar oleh setiap langkah kuliah. Setiap langkah mempunyai tangkapan skrin kuliahnya.",
    ),
    page=dict(en="Page", da="Side", ms="Halaman"),
    gain=dict(en="What you gain", da="Hvad du får", ms="Apa yang anda peroleh"),
    gs=dict(en="Getting started", da="Kom i gang", ms="Bermula"),
    gs_line=dict(en="A `.venv`, the install, and how to run and test the project on Windows and Linux", da="En `.venv`, installationen, og hvordan projektet køres og testes på Windows og Linux", ms="`.venv`, pemasangan, dan cara menjalankan serta menguji projek pada Windows dan Linux"),
    tail=dict(
        en="The questions of the assignment: the shape and quality of the data, categories and women laureates, prizes over time, the top countries, organisations and cities, and the age of the laureates.",
        da="Opgavens spørgsmål: datas form og kvalitet, kategorier og kvindelige modtagere, priser over tid, de bedste lande, organisationer og byer samt modtagernes alder.",
        ms="Soalan tugasan: bentuk dan kualiti data, kategori dan penerima wanita, hadiah dari masa ke masa, negara, organisasi dan bandar teratas, serta umur penerima.",
    ),
)

GS = dict(
    title=dict(en="Getting started", da="Kom i gang", ms="Bermula"),
    req=dict(
        en="Requirements: Python 3.13 or newer. Runtime dependencies: `pandas`, `numpy`, `plotly`, `matplotlib` and `seaborn`.",
        da="Krav: Python 3.13 eller nyere. Kørselsafhængigheder: `pandas`, `numpy`, `plotly`, `matplotlib` og `seaborn`.",
        ms="Keperluan: Python 3.13 atau lebih baharu. Kebergantungan masa jalan: `pandas`, `numpy`, `plotly`, `matplotlib` dan `seaborn`.",
    ),
    win=dict(en="Windows (PowerShell)", da="Windows (PowerShell)", ms="Windows (PowerShell)"),
    win_i=dict(en="Create and use a local `.venv`:", da="Opret og brug en lokal `.venv`:", ms="Cipta dan gunakan `.venv` setempat:"),
    lin=dict(en="Linux and macOS", da="Linux og macOS", ms="Linux dan macOS"),
    lin_i=dict(en="Create and use a local `.venv`:", da="Opret og brug en lokal `.venv`:", ms="Cipta dan gunakan `.venv` setempat:"),
    run=dict(en="Run the analysis, the tests, the type check and the notebook (the same on both systems):", da="Kør analysen, testene, typetjekket og notebooken (ens på begge systemer):", ms="Jalankan analisis, ujian, semakan jenis dan buku nota (sama pada kedua-dua sistem):"),
    scan=dict(en="Scan the code with opengrep before you push (Windows default path `~/.opengrep/cli/latest/opengrep.exe`):", da="Scan koden med opengrep, før du pusher (Windows-standardsti `~/.opengrep/cli/latest/opengrep.exe`):", ms="Imbas kod dengan opengrep sebelum anda push (laluan lalai Windows `~/.opengrep/cli/latest/opengrep.exe`):"),
    gain=dict(
        en="**What you gain:** a repeatable set-up (a virtual environment per project), a package you install in editable mode, and tests that prove each answer.",
        da="**Hvad du får:** en gentagelig opsætning (et virtuelt miljø pr. projekt), en pakke du installerer i redigerbar tilstand, og tests der beviser hvert svar.",
        ms="**Apa yang anda peroleh:** persediaan yang boleh diulang (persekitaran maya bagi setiap projek), pakej yang dipasang dalam mod boleh sunting, dan ujian yang membuktikan setiap jawapan.",
    ),
)

CHARTS = {'step-3-bar-and-donut-charts.jpg': ['chart-step-3-donut.png', 'chart-step-3-categories.png'], 'step-4-trends-over-time.jpg': ['chart-step-4-prizes-per-year.png'], 'step-5-choropleth-map.jpg': ['chart-step-5-choropleth.png'], 'step-6-sunburst-charts.jpg': ['chart-step-6-sunburst.png'], 'step-7-laureate-age.jpg': ['chart-step-7-age-histogram.png']}

ORDER = ["Home", "Getting-Started"] + [s["slug"] for s in STEPS]


def langline(slug, cur):
    parts = []
    for code, name, suf in LANGS:
        parts.append(f"**{name}**" if code == cur else f"[{name}]({slug}{suf})")
    return " · ".join(parts)


def nav(slug, lang):
    i = ORDER.index(slug)
    suf = dict((c, s) for c, _, s in LANGS)[lang]
    l = LBL[lang]
    bits = []
    if i > 0:
        bits.append(f"{l['prev']}: [{ORDER[i-1]}]({ORDER[i-1]}{suf})")
    if i < len(ORDER) - 1:
        bits.append(f"{l['next']}: [{ORDER[i+1]}]({ORDER[i+1]}{suf})")
    return " · ".join(bits)


def extra(s):
    return "".join(f"\n![{c}]({IMG}{c})\n" for c in CHARTS.get(s["img"], []))


def write(name, text):
    (OUT / name).write_text(text.rstrip("\n") + "\n", encoding="utf-8", newline="\n")


for code, lname, suf in LANGS:
    l = LBL[code]
    # Home
    rows = [f"| {HOME['page'][code]} | {HOME['gain'][code]} |", "| --- | --- |", f"| [{HOME['gs'][code]}](Getting-Started{suf}) | {HOME['gs_line'][code]} |"]
    for s in STEPS:
        rows.append(f"| [{s['title'][code]}]({s['slug']}{suf}) | {s['gain_line'][code]} |")
    write(f"Home{suf}.md", f"{langline('Home', code)}\n\n# {HOME['title'][code]}\n\n{HOME['intro'][code]}\n\n" + "\n".join(rows) + f"\n\n{HOME['tail'][code]}\n")
    # Getting started
    g = GS
    write(f"Getting-Started{suf}.md", f"""{langline('Getting-Started', code)}

# {g['title'][code]}

{g['req'][code]}

## {g['win'][code]}

{g['win_i'][code]}

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## {g['lin'][code]}

{g['lin_i'][code]}

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## {g['run'][code]}

```bash
python -m nobel_analysis
python -m pytest
python -m mypy
jupyter lab notebooks/Nobel_Prize_Analysis.ipynb
```

{g['scan'][code]}

```bash
bash scripts/scan.sh
```

{g['gain'][code]}

{nav('Getting-Started', code)}
""")
    for s in STEPS:
        bullets = "\n".join(f"- {b}" for b in s["gain"][code])
        write(f"{s['slug']}{suf}.md", f"""{langline(s['slug'], code)}

# {s['title'][code]}

**{l['q']}:** {s['q'][code]}

![{s['title'][code]}]({IMG}{s['img']})

*{l['lec']} {s['lec']}*
{extra(s)}

## {l['code']}

{s['code'][code]}

## {l['gain']}

{bullets}

{nav(s['slug'], code)}
""")

side = """<!-- Generated by scripts/make_wiki.py; change the generator, not this page. -->
**Nobel Prize Analysis**

- [Home](Home)
- [Getting Started](Getting-Started)
""" + "\n".join(f"- [{s['short']['en']}](" + s["slug"] + ")" for s in STEPS) + """

**Languages**

- English: [Home](Home)
- Dansk: [Hjem](Home-da)
- Bahasa Melayu: [Utama](Home-ms)
"""
write("_Sidebar.md", side)
print(len(list(OUT.glob("*.md"))), "files")
