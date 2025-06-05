# Projeto Platforms, Microservices, DevOps and APIs - 2025.1

Bem-vindo ao projeto da disciplina. Este repositório documenta o desenvolvimento de soluções com microserviços, práticas de DevOps e implantação em nuvem usando Kubernetes (Minikube e AWS EKS).

## Integrantes do Grupo
- Gabriel Mendes
- Henrique Turco

## Estrutura Geral

- **Projeto em Grupo**: Envolve como os microserviços foram integrados, quais tecnologias de infraestrutura foram utilizadas e como o sistema foi implantado em ambiente de produção com AWS EKS.
- **Projeto Individual**: Cada integrante desenvolveu microserviços isoladamente, seguindo especificações de APIs REST autenticadas e integradas ao gateway. Cada serviço incluiu endpoints funcionais, consumo de APIs externas, deploy com Minikube e EKS, além de práticas de DevOps como CI/CD, monitoramento e tratamento de erros. As entregas individuais envolveram também documentação completa com evidências e vídeo de demonstração.

## Repositórios dos Microserviços

- [Account](https://github.com/henriquetg1/account-apis-exercicio-individual.git)
- [Account Service](https://github.com/henriquetg1/account-service-apis-exercicio-individual.git)
- [Auth](https://github.com/henriquetg1/auth-apis-exercicio-individual.git)
- [Auth Service](https://github.com/henriquetg1/auth-service-apis-exercicio-individual.git)
- [Exchange Service](https://github.com/henriquetg1/exchange-service-apis-exercicio-individual.git)
- [Gateway Service](https://github.com/henriquetg1/gateway-service-apis-exercicio-individual.git)
- [Product](https://github.com/henriquetg1/product-apis-exercicio-individual.git)
- [Product Service](https://github.com/henriquetg1/product-service-apis-exercicio-individual.git)
- [Order](https://github.com/henriquetg1/order-apis-exercicio-individual.git)
- [Order Service](https://github.com/henriquetg1/order-service-apis-exercicio-individual.git)

---

## Setup

Para utilizar o código deste repositório, siga as instruções a seguir:

1. Crie um ambiente virtual do Python:
   ```shell
   python -m venv env
   ```

2. Ative o ambiente virtual (você deve fazer isso sempre que for executar algum script deste repositório):
   ```shell
   venv/Scripts/activate
   ```

3. Instale as dependências com:
   ```shell
   pip install -r requirements.txt
   ```

---

## Deployment

O material utiliza o [MkDocs](https://www.mkdocs.org/) para gerar a documentação. Para visualizar a documentação localmente, execute:
```shell
mkdocs serve
```

Para subir ao GitHub Pages, execute:
```shell
mkdocs gh-deploy
```

---

## Agradecimentos

Agradecemos à equipe docente da disciplina e ao suporte técnico fornecido para o desenvolvimento do projeto.

> Documentação desenvolvida para fins acadêmicos – Insper 2025.1.