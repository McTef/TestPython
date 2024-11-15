# Analyse et Classification des Créances

Ce script Python effectue une analyse simple des créances et les classe par tranche de risque en fonction de leur probabilité de défaut.

## Fonctionnalités
1. Calcul du flux de trésorerie total et de l'exposition au risque pour chaque créance.
2. Classification des créances en trois tranches de risque :
   - **Tranche A** : Probabilité de défaut < 2 %.
   - **Tranche B** : Probabilité de défaut entre 2 % et 5 %.
   - **Tranche C** : Probabilité de défaut ≥ 5 %.
3. Calcul des statistiques pour chaque tranche de risque :
   - Nombre de prêts.
   - Montant total emprunté.
   - Moyenne de l'exposition au risque.

### Prérequis
- Python 3.x doit être installé sur votre machine.
- Bibliothèques nécessaires :
  - `pandas`
  - `numpy`

#### Installation des dépendances
Pour installer les bibliothèques nécessaires, exécutez : pip install pandas numpy
