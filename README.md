# Simulation de Données Départementales (2023 & 2024)

Ce projet génère des données simulées pour les années **2023** et **2024** à partir des données réelles **2017** et **2022** grâce à une interpolation linéaire. Les valeurs sont arrondies pour garantir l'absence de décimales.

---
## 🧮 Méthodologie : Interpolation Linéaire
Ce projet utilise une interpolation linéaire pour simuler les valeurs des années 2023 et 2024, à partir des données connues de 2017 (passé) et 2022 (présent).

### 📌 Principe
L’interpolation linéaire consiste à estimer des valeurs intermédiaires entre deux points, en supposant que l’évolution est régulière (linéaire) entre ces deux années.



## 📁 Fichiers nécessaires

Place les fichiers suivants dans le même dossier que ce projet :

- `ALL_DATA_BY_DEP_2017.csv`
- `ALL_DATA_BY_DEP_FINAL_2022.csv`
- `simulate_data.py`
- `Dockerfile`

---

## 🐳 Exécution avec Docker

1. Construire l'image Docker
Dans le dossier contenant le Dockerfile et les fichiers .csv :

```bash
docker build -t simulate-data .
```
2. Lancer le conteneur
```bash
docker run --rm -v "$PWD:/app" simulate-data
```
Les fichiers simulés seront générés dans ton répertoire local (.csv).

## 🚀 Exécution en local

### 1. Installer les dépendances

```bash
pip install pandas
```