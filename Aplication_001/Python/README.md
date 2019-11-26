# Aplicação 001

A seguinte aplicação é bem simples, ela exectua apenas uma requisição HTTP GET. O núcleo da aplicação é a função:

```py
@app.route('/',methods=['GET','POST'])
def hello():
    if request.method == 'GET':
            return "Hello World"
    else:
        return "Erro"
```
Essa função trata as requisições GET e POST HTTP. A requisição é passado com um método da app.route (rota de aplicação Flask). O servidor HTTP feito em Flask envia de volta ao cliente uma mensagem: string (Hello World).

A aplicação está completa para começar um teste simples com o Docker e assim avançar para o Kubernets.

## Dockerfile

O Dockerfile desta aplicação (está no mesmo diretório atual)

```dockerfile
FROM python:3.6-alpine AS base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt  /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt


FROM base

COPY --from=builder /install /usr/local
WORKDIR /app
COPY src/main.py /app
CMD ["python3.6", "main.py"]


```

O primeiro passo começa com uma imagem Python oficial, com o ambiente Python 3.6 instalado. O comando COPY irá passar um arquivo requirements.txt para que sejam baixadas as bibliotecas necessárias. O resultado é uma imagem contendo todas as dependencias necessárias.

* Salvar imagem no dockerhub: Para enviar uma imagem para o DockerHub é preciso fazer o login:

```bash
docker login
```

E enviar a imagem: (é preciso nomeá-la)

```bash
docker image tag pyhello samico/pyhello

docker image push  samico/pyhello
```

## Kurbenetes

Para inicializar o kubernetes na máquina local abra o Docker Desktop Preferences e selecione Kurbenetes e marqui Enable. Para executar a imagem que construímos abra o terminal e execute:

```bash
kubectl run demo --image=samico/pyhello --port=9999 app=demo

kubectl port-forward deploy/demo 9999:9999
```

Verificar status:

```bash
kubectl get pods --selector app=demo
```