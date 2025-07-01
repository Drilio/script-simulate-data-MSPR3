# Simulation de Données Départementales (2023 & 2024)

Ce projet génère des données simulées pour les années **2023** et **2024** à partir des données réelles **2017** et **2022** grâce à une interpolation linéaire. Les valeurs sont arrondies pour garantir l'absence de décimales.

---

## 📁 Fichiers nécessaires

Place les fichiers suivants dans le même dossier que ce projet :

- `ALL_DATA_BY_DEP_2017.csv`
- `ALL_DATA_BY_DEP_FINAL_2022.csv`
- `simulate_data.py`
- `Dockerfile`

---

## 🚀 Exécution en local

### 1. Installer les dépendances

```bash
pip install pandas
```