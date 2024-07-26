# [UNIVESP] Projeto Integrador 1 - Grupo 13: Pet Happy
Esse repositório contém o back-end do Projeto Integrador 1 do Grupo 13 da Universidade Virtual do Estado de São Paulo (UNIVESP). Além desse repositório, veja o [repositório do front-end](https://github.com/suelenfrancis/PetHappy-Projeto-Integrador-01) para ter acesso ao projeto completo.

## Principais tecnologias utilizadas no Back-end
| Tecnologia | Versão |
| ---------- | ------ |
| Django     | 5.0.1  |
| Django Rest Framework | 3.15.1 |
| MySQL Server Community Edition | 8.0.36 |

## Rodando o projeto
Para rodar o backend do projeto, será necessário instalar o gerenciador de dependências do python, o `Pipenv`:
```bash
pip install pipenv
```
Tendo o `Pipenv` instalado ficará mais fácil instalar todas as dependências necessárias para o projeto num ambiente virtual do Python. Para instalar as dependências, vá até o diretório raiz do projeto e rode o comando:
```bash
pipenv install
```
Ao terminar de instalar todas as dependências do projeto, ainda dentro do diretório raiz rode o comando:
```bash
python manage.py runserver
```
Caso o comando seja executado sem erro, mas apareça uma alerta informando que existem migrações a serem feitas, rode o seguinte comando:
```bash
python manage.py migrate
```
Se tudo deu certo, a API ficará disponível no endereço:`http://127.0.0.1/8000/`

## Comando úteis durante o desenvolvimento

### Criando migrações
Sempre que alterar ou criar um modelo, será necessário criar migrações para alterar o esquema de tabelas do banco de dados. Para isso, rode o comando:
```bash
python manage.py makemigrations
```

### Migrando para o banco de dados
Após criar as migrações (ver comando acima), você pode subir as alterações para o banco de dados com o seguinte comando:
```bash
python manage.py migrate
```

### Rodando o servidor
Para rodar o servidor localmente utilize o comando:
```bash
python manage.py runserver
```
Caso queira rodar localmente, mas acessar a API através da rede, para os casos de desenvolvimento em outro dispositivo (mobile), utilize:
```bash
python manage.py runserver 0.0.0.0/8000
```

### Criando super usuário
Para teste, quando for necessário criar um super usuário, utilize o comando:
```bash
python manage.py createsuperuser
```
Informe o `username` e o `password`, não é necessário informar o e-mail.