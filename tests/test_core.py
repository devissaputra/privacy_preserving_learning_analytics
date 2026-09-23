import numpy as np
from privacy_preserving_learning_analytics.core import gradient,clip_and_noise,federated_train,accuracy
from privacy_preserving_learning_analytics.synthetic import make_shards

def test_clip():
    g=np.array([3.,4.]); c=clip_and_noise(g,clip=1,noise_std=0); assert np.linalg.norm(c)<=1.000001

def test_train():
    shards,test=make_shards(4,60,4,2); w=federated_train(shards,rounds=10,noise_std=0); assert len(w)==4; assert 0<=accuracy(*test,w)<=1
