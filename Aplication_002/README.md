## Aplication_002
Nesta aplicação será visto os conceitos de Pods, Deployments e Services e como usar a aplicação Helm para gerenciar aplicações Kubernetes.

----------------------------------------

## Kubernetes

Checando os deployments ativos da aplicação 001:

```bash
kubectl get deployments
```

* Consultando Deployments

```bash
Name:                   demo
Namespace:              default
CreationTimestamp:      Wed, 27 Nov 2019 09:27:39 -0300
Labels:                 app=demo
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=demo
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=demo
  Containers:
   demo:
    Image:        samico/pyhello
    Port:         9999/TCP
    Host Port:    0/TCP
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   demo-f95c5c9dc (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  111s  deployment-controller  Scaled up replica set demo-f95c5c9dc to 1
```