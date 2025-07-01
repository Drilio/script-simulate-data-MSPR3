import pandas as pd

df_2017 = pd.read_csv("ALL_DATA_BY_DEP_2017.csv")
df_2022 = pd.read_csv("ALL_DATA_BY_DEP_FINAL_2022.csv")

df_2017 = df_2017.rename(columns=lambda col: col.replace("_2017", "") if "_2017" in col else col)

df_2017 = df_2017.sort_values("code_departement").reset_index(drop=True)
df_2022 = df_2022.sort_values("code_departement").reset_index(drop=True)

common_cols = df_2017.columns.intersection(df_2022.columns)
numeric_cols = df_2017[common_cols].select_dtypes(include="number").columns

df_2023 = df_2017.copy()
df_2024 = df_2017.copy()

df_2023[numeric_cols] = (
    df_2017[numeric_cols] + (6/10) * (df_2022[numeric_cols] - df_2017[numeric_cols])
).round(0).astype(int)

df_2024[numeric_cols] = (
    df_2017[numeric_cols] + (7/10) * (df_2022[numeric_cols] - df_2017[numeric_cols])
).round(0).astype(int)

df_2023["annee"] = 2023
df_2024["annee"] = 2024

df_2023.to_csv("ALL_DATA_BY_DEP_SIMULATED_2023.csv", index=False)
df_2024.to_csv("ALL_DATA_BY_DEP_SIMULATED_2024.csv", index=False)

print("✅ Données simulées (entiers) sauvegardées :")
print("   → ALL_DATA_BY_DEP_SIMULATED_2023.csv")
print("   → ALL_DATA_BY_DEP_SIMULATED_2024.csv")
