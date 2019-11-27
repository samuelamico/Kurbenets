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

Destruir o Pod original não vai para a execução, pois o Kubernetes partirá do pressuposto de que você deve ter cometido um erro e, de modo prestativo, iniciará um novo Pad. Para desativar basta terminar o Deployment:

```bash
kubectl delete all --selector app=demo
```

### Manifestos YAML

Pode-se criar e editar o manifesto do recurso (a especificação do estado desejado para o recurso) diretamente, através do arquivo de manifesto.

* Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo
  labels:
    app: demo
spec:
  replicas: 3
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
        - name: demo
          image: pyhello
          ports:
          - containerPort: 9999
```

Dentro do diretorio que contém o arquivo .yaml digite:

```bash
kubectl apply -f deploymente.yaml
```

```bash
kubectl get pods --selector app=demo

NAME                    READY   STATUS    RESTARTS   AGE
demo-5f84b97797-75sdg   1/1     Running   0          17s
demo-5f84b97797-btf59   1/1     Running   0          17s
demo-5f84b97797-xptpn   1/1     Running   0          17s
```

* Service

Para realizar a comunicação entre a API Flask é preciso conectar-se diretamente com o endereço do Pod.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo
  labels:
    app: demo
spec:
  ports:
  - port: 9999
    protocol: TCP
    targetPort: 9999
  selector:
    app: demo
  type: ClusterIP

```

Dentro do diretorio que contém o arquivo .yaml digite:

```bash
kubectl apply -f service.yaml
```

```bash
kubectl port-forward service/demo 9999:9999
```