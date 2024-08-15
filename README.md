# [UNIVESP] Projeto Integrador 1 - Grupo 13: Pet Happy
Esse repositório contém o back-end do Projeto Integrador 1 do Grupo 13 da Universidade Virtual do Estado de São Paulo (UNIVESP). Além desse repositório, veja o [repositório do front-end](https://github.com/suelenfrancis/PetHappy-Projeto-Integrador-01) para ter acesso ao projeto completo.

# Principais tecnologias utilizadas no Back-end
| Tecnologia | Versão |
| ---------- | ------ |
| Django     | 5.0.1  |
| Django Rest Framework | 3.15.1 |
| MySQL Server Community Edition | 8.0.36 |

# Rodando o projeto

## Instalando o docker (recomendado)
Para rodar o ambiente de desenvolvimento mais fácil, com apenas um script, será necessário instalar o docker:
- [Instalando no Linux (Ubuntu)](https://docs.docker.com/engine/install/ubuntu/)
- [Complementando instalação no Linux (Ubuntu)](https://docs.docker.com/engine/install/linux-postinstall/)
- [Instalando no Windows](https://docs.docker.com/desktop/install/windows-install/)

## Rodando com o docker instalado (recomendado)
Em um **ambiente Linux ou utilizando WSL no Windows, com o docker instalado**, basta rodar o script `run-dev-local.sh` presente no diretório `/scripts/`:
```bash
./scripts/run-dev-local.sh
```
Caso esteja num **ambiente Windows com o docker desktop instalado**, basta rodar o docker compose diretamente dentro do diretório `/infra/`:
```powershell
docker-compose -f /infra/backend-dev.yml up
```

## Rodando sem o docker instalado (boa sorte)
Para rodar o backend do projeto, será necessário instalar algumas ferramentas:
- Python (versão 3.11.x)
- Pipenv (versão 2013.11.17)
- MySQL server

### Instalando dependências
Para rodar o projeto, será necessário instalar as bibliotecas python necessárias. Recomendo instalar essas bibliotecas num ambiente virtual, para evitar problemas de compatibilidade. Existem duas abordagens para isso:

#### Via Pipenv (recomendado)
Para instalar o gerenciador de dependências do python, o `Pipenv`:
```bash
pip install pipenv
```
Tendo o `Pipenv` instalado ficará mais fácil instalar todas as dependências necessárias para o projeto num ambiente virtual do Python. Para instalar as dependências, vá até o diretório raiz do projeto e rode o comando:
```bash
pipenv install
```

#### Via ambiente virtual nativo
Caso você não queira baixar o `pipenv`, você pode criar um ambiente virtual utilizando as ferramentas nativas do python e instalando as dependências via `requirements.txt`. Para isso, basta criar um ambiente virtual dentro do diretório `/api/`:
```bash
cd /api/ # Acessa o diretório /api/
python -m venv venv # criar um ambiente virtual
```
Com o ambiente virtual criado, vamos ativar o ambiente virtual. Para ativar o **Linux**:
```bash
source venv/bin/activate
```
Para ativar o ambiente virtual no **Windows**:
```powershell
./venv/Scripts/activate.bat
```
Após ativar o ambiente virtual, basta **instalar as dependências via `requirements.txt`**:
```bash
pip install -r requirements.txt
```

### Configurando variáveis de ambiente
Para executar todas as variáveis de ambiente necessárias, execute a `.env`:
```bash
source ./infra/.env.dev
```
### Rodando servidor em desenvolvimento
Ao terminar de instalar todas as dependências do projeto, ainda dentro do diretório raiz rode o comando:
```bash
python manage.py runserver
```
Caso o comando seja executado sem erro, mas apareça uma alerta informando que existem migrações a serem feitas, rode o seguinte comando:
```bash
python manage.py migrate
```
Se tudo deu certo, a API ficará disponível no endereço:`http://127.0.0.1/8000/`

# Comando Django úteis durante o desenvolvimento

## Criando migrações
Sempre que alterar ou criar um modelo, será necessário criar migrações para alterar o esquema de tabelas do banco de dados. Para isso, rode o comando:
```bash
python manage.py makemigrations
```

## Migrando para o banco de dados
Após criar as migrações (ver comando acima), você pode subir as alterações para o banco de dados com o seguinte comando:
```bash
python manage.py migrate
```

## Rodando o servidor
Para rodar o servidor localmente utilize o comando:
```bash
python manage.py runserver
```
Caso queira rodar localmente, mas acessar a API através da rede, para os casos de desenvolvimento em outro dispositivo (mobile), utilize:
```bash
python manage.py runserver 0.0.0.0/8000
```

## Criando super usuário
Para teste, quando for necessário criar um super usuário, utilize o comando:
```bash
python manage.py createsuperuser
```
Informe o `username` e o `password`, não é necessário informar o e-mail.