# DFM-Net

```
@inproceedings{zhang2021depth,
title={Depth quality-inspired feature manipulation for efficient RGB-D salient object detection},
author={Zhang, Wenbo and Ji, Ge-Peng and Wang, Zhuo and Fu, Keren and Zhao, Qijun},
booktitle={Proceedings of the 29th ACM International Conference on Multimedia},
pages={731--740},
year={2021}
}
```

Code: https://github.com/zwbx/DFM-Net.git

## Contributions

net.py:

- Ajout des cartes d'attention du module DHA à la sortie du modèle: ligne 29, lignes 35-39, ligne 286

data.py:

- Prise en compte des images en .bmp pour les données de test: ligne 200

test.py:

- Ajout de la vitesse d'inférence en FPS: lignes 61-62, lignes 69-70, lignes 72-75, ligne 78
- Sauvegarde des cartes d'attentions: lignes 81-106

Les auteurs de cette méthodes n'ont pas fourni le code d'entrainement mais ils nous ont suggéré d'utiliser le code d'entrainement d'un autre de leurs modèle. Malheureusement la tentative d'implémentation n'a pas totalement marché car nous avons bien réussi à lancer un entrainement et à récupérer la courbe d'entrainement mais les poids n'était pas exploitable par le modèle pour la phase de test. Le code n'a donc pas était inclu dans ce répo.

## Dépendances

- Pytorch
- torchvision
- numpy
- matplotlib
- OpenCV

## Test

Préparer les données de cette façon et télécharger le poids "DFMNet_300_epoch.pth" grâce au lien de la page principal:

```
-dataset\ 
   -Objectscale\  
   -Multipleobjects\
   ...
 -pretrain
   -DFMNet_300_epoch.pth
   ...
```

puis lancer test.py.
