# JL-DCF

```
@inproceedings{Fu2020JLDCF,
title={JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection},
author={Fu, Keren and Fan, Deng-Ping and Ji, Ge-Peng and Zhao, Qijun},
booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
pages={3052--3062},
year={2020}
}
```

Code: https://github.com/jiangyao-scu/JL-DCF-pytorch.git

## Contributions

main.py:

- Ajout des nom des datasets pour leur prise en charge lors du test: lignes 9-50, lignes 118-120

solver.py:

- mesure de la vitesse d'inférence en FPS: lignes 62-63, lignes 74-75, lignes 77-78, lignes 86-87, ligne 107
- Visualisation des cartes de caractéristiques: lignes 91-105

JL_DCF.py:

- Ajout des cartes de caractéristiques de chaque branche en sortie du forward: ligne 230

## Dépendances

- Pytorch
- torchvision
- numpy
- matplotlib
- OpenCV

## Entrainement

- Télécharge les poids resnet101-5d3b4d8f grâce au lien gdrive présent dans le README de la page principale puis placer les poids dans le dossier "pretrained"
- Télécharger le dataset d'entrainement grâce au lien gdrive présent dans le README de la page principale.
- Lancer l'entrainement grâce à la commande suivante:

```bash 
!python main.py --mode=train --arch=resnet --network=resnet101 --train_root=/content/RGBDcollection --train_list=/content/RGBDcollection/train_ori.lst
```

## Test

- Télécharge les poids JL-DCF_resn101 grâce au lien gdrive présent dans le README de la page principale puis placer les poids dans le dossier "models"
- Télécharger les datasets de test ("10_sous_datasets", "4_datasets_globaux") grâce au lien gdrive présent dans le README de la page principale.
- Lancer les tests grâce à la commande suivante:

```bash 
!python main.py --mode=test --arch=resnet --network=resnet101 --model=/content/JL-DCF-pytorch/models/JL-DCF_resn101.pth --test_folder=/content/pred_maps/JL-DCF/Objectscale/ --sal_mode=Objectscale
```
