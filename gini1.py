import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def calculate_gini(array):
    array = array[~np.isnan(array)]
    if len(array) == 0 or np.sum(array) == 0:
        return 0
    
    array = np.sort(array)
    n = len(array)
    index = np.arange(1, n + 1)
    return ((np.sum((2 * index - n - 1) * array)) / (n * np.sum(array)))

def process_excel_gini(input_file, column_name, output_file='wyniki_gini.xlsx'):
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)
    
    if column_name not in df.columns:
        print(f"Błąd: Brak kolumny '{column_name}' w pliku!")
        return

    data_vector = df[column_name].values
    gini_value = calculate_gini(data_vector)
    
    report_df = pd.DataFrame({
        'Metryka': ['Analizowana kolumna', 'Liczba rekordów', 'Współczynnik Giniego'],
        'Wartość': [column_name, len(data_vector), round(gini_value, 4)]
    })
    
    report_df.to_excel(output_file, index=False)
    print(f"Analiza zakończona. Wynik zapisano w: {output_file}")
    
    plt.figure(figsize=(6, 6))
    plt.boxplot(data_vector, patch_artist=True, labels=[column_name])
    plt.title(f'Rozkład: {column_name}\n(Gini: {gini_value:.3f})')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# TEST
process_excel_gini('dochody.xlsx', 'Dochod_Zroznicowany')
