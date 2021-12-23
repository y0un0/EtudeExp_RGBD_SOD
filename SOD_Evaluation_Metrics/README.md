# SOD_Evaluation_Metrics

Les métriques sont basées sur ces articles:

      @inproceedings{Fmeasure,
          title={Frequency-tuned salient region detection},
          author={Achanta, Radhakrishna and Hemami, Sheila and Estrada, Francisco and S{\"u}sstrunk, Sabine},
          booktitle=CVPR,
          number={CONF},
          pages={1597--1604},
          year={2009}
      }
      
      @inproceedings{MAE,
          title={Saliency filters: Contrast based filtering for salient region detection},
          author={Perazzi, Federico and Kr{\"a}henb{\"u}hl, Philipp and Pritch, Yael and Hornung, Alexander},
          booktitle=CVPR,
          pages={733--740},
          year={2012}
      }
      
      @inproceedings{Smeasure,
          title={Structure-measure: A new way to eval foreground maps},
          author={Fan, Deng-Ping and Cheng, Ming-Ming and Liu, Yun and Li, Tao and Borji, Ali},
          booktitle=ICCV,
          pages={4548--4557},
          year={2017}
      }
      
      @inproceedings{Emeasure,
          title="Enhanced-alignment Measure for Binary Foreground Map Evaluation",
          author="Deng-Ping {Fan} and Cheng {Gong} and Yang {Cao} and Bo {Ren} and Ming-Ming {Cheng} and Ali {Borji}",
          booktitle=IJCAI,
          pages="698--704",
          year={2018}
      }
      
      @inproceedings{wFmeasure,
        title={How to eval foreground maps?},
        author={Margolin, Ran and Zelnik-Manor, Lihi and Tal, Ayellet},
        booktitle=CVPR,
        pages={248--255},
        year={2014}
      }

Code: https://github.com/zyjwuyan/SOD_Evaluation_Metrics.git

## Contributions

main.py:

- Ajout de lignes de code pour régler un bug: lignes 31-40

## Dépendances

- Pytorch
- torchvision
- numpy
- scipy
- tqdm

## Utilisation

- Il est nécessaire que les fichiers soient ordonnés de la façon suivante:

      --gt/
            --Objectscale/
                --img1.png
                --img2.png
                    ...
            --Multiobjects/
                ...
      --pred_maps/
            --JL-DCF/
                --Objectscale/
                    --img1.png
                    --img1.png
                        ...
                --Multiobject/
                    ...
            --DFM-Net/
                ...

- Le calcul des métriques se fais en lançant la commande suivante: 
  
  `!python main.py --pred_root_dir /content/pred_maps/ --gt_root_dir /content/gt/ --save_dir /content/score/`


- La création des courbes de précision-rappel et de F-measure est réalisée en lançant la commande suivante:
  
    `!python draw_curve.py`
  
  Ensuite les fichiers seront sauvegardé dans le dossier '/content/score/'.

