import pickle
import torch
# 加载模型文件
file='/home/sys123456/Q22301179/data/unetr_pp_Data/DATASET/nnFormer_trained_models/unetr_pp/3d_fullres/Task006_Lung/unetr_pp_trainer_lung__unetr_pp_Plansv2.1/fold_1/model_final_checkpoint.model'
f = open(file,'rb')
model = torch.load(f,map_location='cpu')#可使用cpu或gpu

# 将模型保存为.pkl文件
with open('/home/sys123456/Q22301179/data/unetr_pp_Data/DATASET/nnFormer_trained_models/unetr_pp/3d_fullres/Task006_Lung/unetr_pp_trainer_lung__unetr_pp_Plansv2.1/fold_1/model_final_checkpoint.model.pkl', 'wb') as f:
    pickle.dump(model, f)
