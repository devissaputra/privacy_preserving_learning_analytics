import numpy as np

def make_shards(n_clients=8,n_each=180,dim=6,seed=37):
    rng=np.random.default_rng(seed); true=rng.normal(0,1,dim); shards=[]
    for c in range(n_clients):
        X=rng.normal(loc=(c-n_clients/2)*.08,size=(n_each,dim)); p=1/(1+np.exp(-(X@true+rng.normal(0,.35,n_each)))); y=(rng.random(n_each)<p).astype(int); shards.append((X,y))
    Xtest=rng.normal(size=(800,dim)); p=1/(1+np.exp(-(Xtest@true+rng.normal(0,.35,800)))); ytest=(rng.random(800)<p).astype(int); return shards,(Xtest,ytest)
