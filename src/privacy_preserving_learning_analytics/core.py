# Calculation reading guide: ../CALCULATIONS.md (repository root).
# g = Xᵀ(sigmoid(Xw)-y)/n; w_next = w - learning_rate×mean(client gradients).
# Clients receive equal weight, not sample-size weight. Clipping plus noise has no stated epsilon/delta accountant, secure aggregation, or attack evaluation. It is not a formal differential-privacy guarantee.

from __future__ import annotations
import numpy as np

def sigmoid(z): return 1/(1+np.exp(-np.clip(z,-30,30)))
def gradient(X,y,w):
    p=sigmoid(X@w); return X.T@(p-y)/len(y)
def clip_and_noise(g,clip=1.0,noise_std=0.0,rng=None):
    rng=rng or np.random.default_rng(0); norm=float(np.linalg.norm(g)); scaled=g if norm<=clip else g*(clip/(norm+1e-12)); return scaled+rng.normal(0,noise_std,size=g.shape)
def federated_train(shards,rounds=40,lr=.35,clip=1.0,noise_std=0.0,seed=0):
    dim=shards[0][0].shape[1]; w=np.zeros(dim); rng=np.random.default_rng(seed)
    for _ in range(rounds):
        grads=[clip_and_noise(gradient(X,y,w),clip,noise_std,rng) for X,y in shards]; w-=lr*np.mean(grads,axis=0)
    return w
def accuracy(X,y,w): return float(((sigmoid(X@w)>=.5)==y).mean())
