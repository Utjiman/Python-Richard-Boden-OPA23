import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
from inspect import currentframe

DATA_PATH = (
    Path(__file__).parents[2] / "Data" / "Data_Processing")  ## Hoppa runt i mappar (__file__) = där man befinner sig från början

STYLES_PATH = Path(__file__).parent / "styles"

## .parents[2] 2 mappar över den aktuella. / "Data" / "Data_Processing" går in i andra mappar
class StoryCharts:
    def __init__(self) -> None:
        plt.style.use(STYLES_PATH / "base.mplstyle")

    def _set_labels(self, title, xlabel, ylabel):
        self.ax.set_xlabel(xlabel, loc="left")
        self.ax.set_ylabel(ylabel, loc="top")
        self.ax.set_title(title, loc="left", pad=15)

    def _plot(self, x, y, colors="#0c4e6e", **label_kwargs):
        self.fig, self.ax = plt.subplots()

        calling_method_name = currentframe().f_back.f_code.co_name
        if calling_method_name == "Line":
            self.ax.plot(x, y, color=colors)
        elif calling_method_name == "Bar":
            self.ax.bar(x, y, color=colors)

        self._set_labels(**label_kwargs)
        self.fig.tight_layout()
        plt.show()

    def Line(self, x, y, colors="#0c4e6e", **label_kwargs):
        self._plot(x, y, colors, **label_kwargs)

    def Bar(self, x, y, colors="#0c4a6e", **label_kwargs):
        self._plot(x,y, colors, **label_kwargs)


if (
    __name__ == "__main__"
):  ## för att köra som ett ensamt script. koden körs inte när den är importerad från ett annat script.
    print("\n\n")
    # print(data_path)
    # print(__name__)

df = pd.read_csv(DATA_PATH / "co2_annmean_mlo.csv", skiprows=43)

print(df.head())

sc = StoryCharts()
sc.Line(
    df["year"],
    df["mean"],
    xlabel="Year from 1959",
    ylabel="co2 mole fraction in ppm",
    title="The annual mean of co2 osv"
)
sc.Bar(
    df["year"],
    df["mean"],
    xlabel="Year from 1959",
    ylabel="co2 mole fraction in ppm",
    title="The annual mean of co2 osv"
)