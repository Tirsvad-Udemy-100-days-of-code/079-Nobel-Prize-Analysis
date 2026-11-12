"""Render one chart image per lecture step into docs/images/.

Usage:
    python scripts/make_screenshots.py [output_dir]
Plotly figures need the `kaleido` package (a dev dependency) and Chrome.
"""

import sys
from pathlib import Path

from nobel_analysis.application import analysis, cleaning
from nobel_analysis.infrastructure.data import load_nobel
from nobel_analysis.presentation import charts

DEFAULT_OUT = Path(__file__).resolve().parents[1] / "docs" / "images"


def main(out: Path) -> None:
    """Write the chart images (one per lecture step that draws a chart)."""
    out.mkdir(parents=True, exist_ok=True)
    df = cleaning.clean(load_nobel())
    aged = analysis.add_winning_age(df)
    charts.category_bar_chart(df).write_image(out / "chart-step-3-categories.png", width=1000, height=520)
    charts.sex_donut_chart(df).write_image(out / "chart-step-3-donut.png", width=800, height=520)
    charts.prizes_per_year_chart(df).savefig(out / "chart-step-4-prizes-per-year.png", dpi=110)
    charts.country_choropleth(df).write_image(out / "chart-step-5-choropleth.png", width=1100, height=560)
    charts.sunburst_chart(df).write_image(out / "chart-step-6-sunburst.png", width=760, height=760)
    charts.winning_age_histogram(aged).savefig(out / "chart-step-7-age-histogram.png", dpi=110)
    print("wrote chart images to", out)


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT)
