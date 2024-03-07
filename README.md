# desafio-sre

Aplicação que expõe uma api web que recebe por parametros um JWT (string) e verifica se é valida.

## Instalação

1. Clone o repositório:
git clone https://github.com/nathaliapaulon/desafio-sre.git

2. Navegue até o diretório do projeto:
cd desafio-sre/app/

## Uso

Passo 1 - Criar um Ambiente Virtual: 
python3 -m venv venv
	
Passo 2 - Ativar o Ambiente Virtual: 
source venv/bin/activate

Passo 3 - Instalar as Dependências: 
pip install Flask PyJWT

Executando a Aplicação:	python app.py

A aplicação estará rodando no endereço `http://localhost:5000`.

Para validar um JWT, faça uma requisição POST para `/validate` com o JWT no corpo da requisição:
bash curl -X POST -H "Content-Type: application/json" -d '{"token":"seu_jwt_aqui"}' http://localhost:5000/validate

## Testes

curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05sIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg"}' http://localhost:5000/validate

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Containerização
docker pull nathaliapaulon7491/app-desafio

## Contato

Nathalia F Paulon - nathaliapaulon@hotmail.com

Link para o projeto: [https://github.com/nathaliapaulon/desafio-sre](https://github.com/nathaliapaulon/desafio-sre)
