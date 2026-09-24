from pathlib import Path
import json,csv,numpy as np
from privacy_preserving_learning_analytics.synthetic import make_shards
from privacy_preserving_learning_analytics.core import federated_train,accuracy
root=Path(__file__).resolve().parents[1]; (root/'results').mkdir(exist_ok=True)
shards,test=make_shards(); Xtest,ytest=test; rows=[]
for noise in [0,.02,.05,.1,.2]:
    w=federated_train(shards,noise_std=noise,seed=3); rows.append({'noise_std':noise,'accuracy':accuracy(Xtest,ytest,w)})
with open(root/'results'/'privacy_utility.csv','w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=rows[0].keys()); wr.writeheader(); wr.writerows(rows)
metrics={'federated_accuracy':round(rows[0]['accuracy'],3),'noisy_federated_accuracy_noise_0_10':round(rows[3]['accuracy'],3),'utility_delta':round(rows[0]['accuracy']-rows[3]['accuracy'],3)}
(root/'results'/'demo_metrics.json').write_text(json.dumps(metrics,indent=2)); print(json.dumps(metrics,indent=2))
