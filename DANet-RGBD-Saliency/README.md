# DANet

```
@inproceedings{DANet,
  title={A Single Stream Network for Robust and Real-time RGB-D Salient Object Detection},
  author={Zhao, Xiaoqi and Zhang, Lihe and Pang, Youwei and Lu, Huchuan and Zhang, Lei},
  booktitle=ECCV,
  year={2020}
}
```
Code: https://github.com/Xiaoqi-Zhao-DLUT/DANet-RGBD-Saliency.git

## Contributions

DANet.py:

- ajout d'outputs: ligne 108

datasets.py:

- Modifications dans la fonction make_dataset: lignes 11-36

train.py:

- sauvegarde de la courbe de loss: lignes 78-83
- ajout d'une liste pour conserver les valeurs de loss: ligne 87, ligne 139, ligne 148
- ajout de la mesure du temps: ligne 88, lignes 146-148

generate_salmap.py:

- mesure de la vitesse d'inférence en FPS: lignes 49-50, lignes 65-66, lignes 68-69, lignes 72-73, ligne 89

generate_visfeamaps.py:

- Récupération des cartes d'attention: lignes 63-67, lignes 74-76, lignes 82-85, lignes 106-113
- Récupération des cartes de caractéristique de l'encodeur: lignes 94-103

## Dépendances

- Pytorch 1.5.0
- torchvision
- numpy
- scipy
- Pillow
- Cython
- pydensecrf-1.0rc2

## Entrainement

Mettre le chemin des données d'entrainement dans config.py:

``datasets_root_train ='/content/RGBDcollection'``

Lancer train.py

Note: Les hyperparamètres sont à changer dans train.py

## Test

Mettre le chemin des données d'entrainement dans config.py:

``datasets_root_test ='/content/Complexbackground'``

Lancer generate_salmap.py pour visualiser les cartes de saillance prédites

Lancer generate_visfeamaps.py pour visualiser les cartes de caractéristiques
