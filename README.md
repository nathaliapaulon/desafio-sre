# desafio-sre

Aplicação que expõe uma api web que recebe por parametros um JWT (string) e verifica se é valida.

## Instalação

1. Clone o repositório:
git clone https://github.com/nathaliapaulon/desafio-sre.git

2. Navegue até o diretório do projeto:
cd desafio-sre

3. Crie um ambiente virtual e ative-o:
python3 -m venv venv source venv/bin/activate

4. Instale as dependências:
cd app
pip install -r requirements.txt

## Uso

Para iniciar a aplicação, execute o seguinte comando no diretório do projeto:
python app.py

A aplicação estará rodando no endereço `http://localhost:5000`.

Para validar um JWT, faça uma requisição POST para `/validate` com o JWT no corpo da requisição:
bash curl -X POST -H "Content-Type: application/json" -d '{"token":"seu_jwt_aqui"}' http://localhost:5000/validate

## Testes

Para executar os testes, use o seguinte comando:
pytest

## Contato

Nathalia F Paulon - nathaliapaulon@hotmail.com

Link para o projeto: [https://github.com/nathaliapaulon/desafio-sre](https://github.com/nathaliapaulon/desafio-sre)
