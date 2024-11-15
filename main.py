import pandas as pd
import numpy as np

def main():
    # Création d'une table de données contenant les créances
    donnees = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'montant': [10000, 15000, 5000, 20000, 12000],
        'taux_interet': [0.05, 0.04, 0.06, 0.03, 0.045],
        'duree': [5, 3, 2, 7, 4],
        'probabilite_defaut': [1.5, 4, 6, 2.5, 3]
    })

    # Calculs des indicateurs (flux de trésorie total et exposition au risque)
    donnees['flux_tresorerie_total'] = donnees['montant'] * (1 + donnees['taux_interet']) ** donnees['duree']
    donnees['exposition_risque'] = donnees['montant'] * (donnees['probabilite_defaut'] / 100)

    # Classification des créances par tranche de risque
    conditions = [
        donnees['probabilite_defaut'] < 2,  # Probabilité de défaut inférieure à 2 % -> tranche A
        donnees['probabilite_defaut'] < 5,  # Probabilité de défaut inférieure à 5 % mais ≥ 2 % -> tranche B
    ]
    choix = ['A', 'B']  # Les tranches A et B sont définies pour les conditions plus haut
    donnees['tranche_risque'] = np.select(conditions, choix, default='C')  # Sinon, tranche C

    # Calculs statistiques pour chaque tranches
    # je regroupe la table " donnees " par tranche de risque (A, B, C) et je calcule les statistiques demandées
    stats_tranches = donnees.groupby('tranche_risque', as_index=False).agg(
        nombre_prets=('id', 'count'),
        montant_total=('montant', 'sum'),
        moyenne_exposition_risque=('exposition_risque', 'mean')
    )

    # Affichage des statistiques des tranches, avec avant celui des créances et des indicateurs calculés
    print("Créances, flux de trésorie totale et expositionx au risque :\n\n", donnees.to_string(index=False), "\n")
    print("Statistiques par tranche de risque :\n\n", stats_tranches.to_string(index=False))


if __name__ == "__main__":
    main()