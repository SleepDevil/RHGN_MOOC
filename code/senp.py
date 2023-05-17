import numpy as np
import pickle as p
import torch
 
f = torch.load("../taobao_data/cid3_feature.npy")
print(f.size())