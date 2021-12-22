# UCNet

```
@inproceedings{Zhang2020UCNet,
  title={UC-Net: Uncertainty Inspired RGB-D Saliency Detection via Conditional Variational Autoencoders},
  author={Zhang, Jing and Fan, Deng-Ping and Dai, Yuchao and Anwar, Saeed and Sadat Saleh, Fatemeh and Zhang, Tong and Barnes, Nick},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  year={2020}
}
```

Code: https://github.com/JingZhang617/UCNet.git

## Contributions

test.py:

- Mesure de la vitesse d'inférence en FPS: lignes 40-41, lignes 47-48, lignes 50-51, lignes 56-58
- Passer du code en commentaire: ligne 7

train.py:

- Passer du code en commentaire: lignes 170-172
- Mesure du temps d'entrainement: ligne 130, lignes 191-193
- Sauvegarde de la loss dans un fichier csv: lignes 76-78, ligne 129, ligne 133, ligne 166, ligne 185, ligne 193

## Dépendances

- Pytorch
- pandas
- numpy
- torchvision

## Entrainement

- Télécharger la base de donnée d'entrainement "data" grâce au lien gdrive présent sur la page principale. Cette base de données est exactement la même que RGBDcollection, c'est juste qu'elle dispose d'un dossier en plus nommé "gray" qui est spécifique à cette méthode.
- Lancer train.py

## Test

- Télécharger les datasets de test ("10_sous_datasets", "4_datasets_globaux") grâce au lien présent sur la page principale
- Télécharger les poids "Model_100_gen_trained" grâce au lien présent sur la page principale puis placer ces poids dans le dossier "models"
- Lancer test.py
