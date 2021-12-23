# SYS843_EtudeExp_RGBD_SOD
Younès Driouache

Voici les des dossiers des méthodes DANet, DFM-Net, JL-DCF et UCNet.

Les codes utilisé proviennent des répos suivant:

- DANet = https://github.com/Xiaoqi-Zhao-DLUT/DANet-RGBD-Saliency.git
- DFM-Net = https://github.com/zwbx/DFM-Net.git
- JL-DCF = https://github.com/jiangyao-scu/JL-DCF-pytorch.git
- UCNet = https://github.com/JingZhang617/UCNet.git

```
@inproceedings{DANet,
  title={A Single Stream Network for Robust and Real-time RGB-D Salient Object Detection},
  author={Zhao, Xiaoqi and Zhang, Lihe and Pang, Youwei and Lu, Huchuan and Zhang, Lei},
  booktitle=ECCV,
  year={2020}
}
```

```
@inproceedings{zhang2021depth,
title={Depth quality-inspired feature manipulation for efficient RGB-D salient object detection},
author={Zhang, Wenbo and Ji, Ge-Peng and Wang, Zhuo and Fu, Keren and Zhao, Qijun},
booktitle={Proceedings of the 29th ACM International Conference on Multimedia},
pages={731--740},
year={2021}
}
```
```
@inproceedings{Fu2020JLDCF,
title={JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection},
author={Fu, Keren and Fan, Deng-Ping and Ji, Ge-Peng and Zhao, Qijun},
booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
pages={3052--3062},
year={2020}
}
```

```
@inproceedings{Zhang2020UCNet,
  title={UC-Net: Uncertainty Inspired RGB-D Saliency Detection via Conditional Variational Autoencoders},
  author={Zhang, Jing and Fan, Deng-Ping and Dai, Yuchao and Anwar, Saeed and Sadat Saleh, Fatemeh and Zhang, Tong and Barnes, Nick},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  year={2020}
}
```

## Datasets et poids des modèles

Poids des modèles: https://drive.google.com/file/d/1WxrzNBMnmFfRay9s4LAaRli2Q5THQGUp/view?usp=sharing

Dataset d'entrainement: 

- RGBDCollection pour les méthodes JL-DCF, DANet et DFM-Net: https://drive.google.com/file/d/1KZtFdJbA1hrkgh2On2OGF_tEPxQqDFx_/view?usp=sharing
- data pour la méthode UCNet: https://drive.google.com/file/d/1v99Af35qfXA76yjazpAVtV7PwyePSwZf/view?usp=sharing

A noter que les datasets d'entrainement RGBDcollection et data comportent les même données. La seule différence est que "data" possède un dossier en plus nommé "gray".

Datasets de test:

- Test sur les datasets globaux: https://drive.google.com/file/d/1bcAQ3OaMoV6ZWaa1CRfpriKjBzlKL_is/view?usp=sharing
- Test sur les sous datasets: https://drive.google.com/file/d/1Y1EDO35tXCLN4zFS5Xrm7QkIRpsGLMwQ/view?usp=sharing


