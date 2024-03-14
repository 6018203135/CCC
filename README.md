# An Efficient and Lightweight Adaptive Network for 3D Medical Image Segmentation
---
## Installation
The code is tested with PyTorch 1.11.0 and CUDA 11.3. After cloning the repository, follow the below steps for installation,

1. Create and activate conda environment
```shell
conda create --name ConvNet python=3.8
conda activate ConvNet
```
2. Install PyTorch and torchvision
```shell
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
```
3. Install other dependencies
```shell
pip install -r requirements.txt
```
<hr />

####  Functions of scripts and folders
- **For evaluation:**
  - ``evaluation_scripts/run_evaluation_synapse.sh``
  
  - ``evaluation_scripts/run_evaluation_lung.sh``
  
  - ``evaluation_scripts/run_evaluation_tumor.sh``

- **For inference:**
  - ``unetr_pp/inference/predict_simple.py``
  
- **Network architecture:**
  - ``unetr_pp/network_architecture/tumor/unetr_pp_tumor.py``
  
  - ``unetr_pp/network_architecture/lung/unetr_pp_lung.py``
  
  - ``unetr_pp/network_architecture/synapse/unetr_pp_synapse.py``
  
- **For training:**
  - ``unetr_pp/run/run_training.py``
  
- **Trainer for dataset:**
  - ``unetr_pp/training/network_training/unetr_pp_trainer_tumor.py``
  
  - ``unetr_pp/training/network_training/unetr_pp_trainer_lung.py``
  
  - ``unetr_pp/training/network_training/unetr_pp_trainer_synapse.py``
---

## Training
#### 1. Dataset download
We follow the same dataset preprocessing as in [UNETR++](https://github.com/Amshaker/unetr_plus_plus). We conducted extensive experiments on four benchmarks: Synapse, BTCV, BRaTs, and Decathlon-Lung. 

The dataset folders for Synapse should be organized as follows: 
```
./DATASET_Synapse/
  ├── unetr_pp_raw/
      ├── unetr_pp_raw_data/
           ├── Task02_Synapse/
              ├── imagesTr/
              ├── imagesTs/
              ├── labelsTr/
              ├── labelsTs/
              ├── dataset.json
           ├── Task002_Synapse
       ├── unetr_pp_cropped_data/
           ├── Task002_Synapse
 ```
 
  The dataset folders for Decathlon-Lung should be organized as follows: 

```
./DATASET_Lungs/
  ├── unetr_pp_raw/
      ├── unetr_pp_raw_data/
           ├── Task06_Lung/
              ├── imagesTr/
              ├── imagesTs/
              ├── labelsTr/
              ├── labelsTs/
              ├── dataset.json
           ├── Task006_Lung
       ├── unetr_pp_cropped_data/
           ├── Task006_Lung
 ```
   The dataset folders for BRaTs should be organized as follows: 

```
./DATASET_Tumor/
  ├── unetr_pp_raw/
      ├── unetr_pp_raw_data/
           ├── Task03_tumor/
              ├── imagesTr/
              ├── imagesTs/
              ├── labelsTr/
              ├── labelsTs/
              ├── dataset.json
           ├── Task003_tumor
       ├── unetr_pp_cropped_data/
           ├── Task003_tumor
 ```
 
Please refer to [Setting up the datasets](https://github.com/282857341/nnFormer) on nnFormer repository for more details.
Alternatively, you can download the preprocessed dataset for [Synapse](https://mbzuaiac-my.sharepoint.com/:u:/g/personal/abdelrahman_youssief_mbzuai_ac_ae/EbHDhSjkQW5Ak9SMPnGCyb8BOID98wdg3uUvQ0eNvTZ8RA?e=YVhfdg), [Decathlon-Lung](https://mbzuaiac-my.sharepoint.com/:u:/g/personal/abdelrahman_youssief_mbzuai_ac_ae/EWhU1T7c-mNKgkS2PQjFwP0B810LCiX3D2CvCES2pHDVSg?e=OqcIW3), [BRaTs](https://mbzuaiac-my.sharepoint.com/:u:/g/personal/abdelrahman_youssief_mbzuai_ac_ae/EaQOxpD2yE5Btl-UEBAbQa0BYFBCL4J2Ph-VF_sqZlBPSQ?e=DFY41h), and extract it under the project directory.

#### 2.Data splitting and Preprocessing
You can refer to [nnFormer](https://github.com/282857341/nnFormer) for data splitting and preprocessing

#### 3. Training and Testing
The following scripts can be used for training our 3D ConvNet++ model on the datasets:
```shell
bash training_scripts/run_training_synapse.sh
bash training_scripts/run_training_acdc.sh
bash training_scripts/run_training_lung.sh
bash training_scripts/run_training_tumor.sh
```
To reproduce the results of 3D ConvNet++:

1- Download [Synapse weights](https://drive.google.com/file/d/13JuLMeDQRR_a3c3tr2V2oav6I29) and paste ```model_final_checkpoint.model``` in the following path:

```shell
unetr_pp/evaluation/unetr_pp_synapse_checkpoint/unetr_pp/3d_fullres/Task002_Synapse/unetr_pp_trainer_synapse__unetr_pp_Plansv2.1/fold_0/
```
Then, run 
```shell
bash evaluation_scripts/run_evaluation_synapse.sh
```

2- Download [Decathlon-Lung weights](https://mbzuaiac-my.sharepoint.com/:u:/g/personal/abdelrahman_youssief_mbzuai_ac_ae/ETAlc8WTjV1BhZx7zwFpA8UBS4og6upb1qX2UKkypMoTjw) and paste ```model_final_checkpoint.model``` it in the following path:
```shell
unetr_pp/evaluation/unetr_pp_lung_checkpoint/unetr_pp/3d_fullres/Task006_Lung/unetr_pp_trainer_lung__unetr_pp_Plansv2.1/fold_0/
```
Then, run 
```shell
bash evaluation_scripts/run_evaluation_lung.sh
```

3- Download [BRaTs weights](https://drive.google.com/file/d/1LiqnVKKv3DrDKvo6J0oClhIFirhaz5PG) and paste ```model_final_checkpoint.model``` it in the following path:
```shell
unetr_pp/evaluation/unetr_pp_lung_checkpoint/unetr_pp/3d_fullres/Task003_tumor/unetr_pp_trainer_tumor__unetr_pp_Plansv2.1/fold_0/
```
Then, run 
```shell
bash evaluation_scripts/run_evaluation_tumor.sh
```

#### 4. Visualization Results

You can see the results of our 3D ConvNet++ model visualization in the directory ``CCC/result_figure``.
#### 5. One Frequently Asked Problem
```
input feature has wrong size
```
If you encounter this problem during your implementation, please check the code in ``unetr_pp/run/default_configuration.py``. I have set independent crop size (i.e., patch size) for each dataset. You may need to modify the crop size based on your own need.
