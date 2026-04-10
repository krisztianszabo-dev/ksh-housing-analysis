import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


class HousingDataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data(file_path)

    def load_data(self, path):

        df = pd.read_csv(path, sep=";", decimal=',', encoding='latin2', skiprows=1, na_values='..')
        df.columns = df.columns.str.strip()
        df.iloc[:, 0] = df.iloc[:, 0].ffill()
        for col in df.columns[2:]:
            df[col] = df[col].astype(str).str.replace(r'\s+', '', regex=True).astype(float)
        return df

    def tablazat_es_grafikon(self,oszlop):

        # Konzol táblázat
        print(f"\n--- {oszlop} ---")
        print(self.df[['Év', 'Negyedév', oszlop]].to_string(index=False))

        # Grafikon
        plt.figure(figsize=(12, 6))
        x_tengely = self.df['Év'].astype(str) + " " + self.df['Negyedév']

        plt.plot(x_tengely, self.df[oszlop], marker='o', color='#1f77b4', linewidth=2)
        plt.title(f'{oszlop} alakulása', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    def lin_regression(self):
        oszlop = "Új és használt lakások összevont lakáspiaci árindexe, 2015 = 100%"


        x_adatok = range(len(self.df)) #self.df['Év'].astype(str) + " " + self.df['Negyedév']
        y_adatok = self.df[oszlop].values

        slope, intercept, r, p, std_err = stats.linregress(x_adatok, y_adatok)

        mymodel = [slope * x + intercept for x in x_adatok]

        plt.figure(figsize=(12, 6))

        x_feliratok = self.df['Év'].astype(str) + " " + self.df['Negyedév']

        plt.scatter(x_feliratok, y_adatok, color='#1f77b4', label='Eredeti adatok')

        plt.plot(x_feliratok, mymodel, color='red', linewidth=2, label='Regressziós egyenes')

        plt.title(f'{oszlop} alakulása', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()


    def kiadott_es_epitett(self,oszlop1,oszlop2):
        # Konzol táblázat
        print(f"\n--- {oszlop1} | {oszlop2} ---")
        print(self.df[['Év', 'Negyedév', oszlop1, oszlop2]].to_string(index=False))

        # Grafikon
        plt.figure(figsize=(12, 6))
        x_tengely = self.df['Év'].astype(str) + " " + self.df['Negyedév']

        plt.plot(x_tengely, self.df[oszlop1], marker='o', color='#1f77b4', linewidth=2, label = oszlop1)
        plt.plot(x_tengely, self.df[oszlop2], marker='o', color='red', linewidth=2, label = oszlop2)
        plt.title(f'{oszlop1} és {oszlop2} összevetve', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.legend()
        plt.show()
