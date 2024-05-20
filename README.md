# Tratando Planilhas de Emails com Python :snake: 

Este repositório contém um conjunto de scripts para tratar planilhas de emails. O objetivo é facilitar a manipulação e processamento de emails que esstejam em algum tipo de banco com dados além desses emails e retorna-los de forma organizada, separando com vírgula e quebra de linha. 

- O script [`extract-email.py`](extract-email.py) vai filtrar todos os emails detectados no arquivo/texto e retorna-los os separando por vírgula e quebrando uma linha.
  
- O script [`delete-repeated-emails.py`](delete-repeated-emails.py) vai remover todos os emails repetidos da sua lista de e-mails.

- O script [`convert-csv.py`](convert-csv.py) vai converter o arquivo `.txt` gerado pelo script anterior em um arquivo `.csv`

- O script [`split-into-x-emails.py`](split-into-x-emails.py) vai ler o arquivo txt com a lista de emails já organizada e dividir em vários arquivos de acordo com a sua necessidade de números de e-mails.
  - Por exemplo: a lista tem 1000 e-mails e você precisa de arquivos que contenham apenas 100 e-mails. Então você consegue criar 10 arquivos com 100 e-mails.

## Funcionalidades

- Extração de endereços de email a partir de planilhas
- Remoção de emails duplicados
- Limpeza e normalização de endereços de email
- Divisão de uma grande lista em listas menores

## Como usar

1. Clone este repositório para o seu ambiente local.
2. Cole o texto que precisa ser tratado em `emails.txt` ou adicione seu próprio arquivo e modifique o caminho no script `extract-email.py`.
3. Execute os scripts fornecidos para realizar as operações desejadas.
4. Todos os arquivos com os e-mails separados por vírgula irão para a pasta `datalake`

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

| <a  href="https://www.linkedin.com/in/victor-breia/"> <img  style="border-radius: 50%;"  src="https://raw.githubusercontent.com/vbreia/vbreia/main/Sem%20T%C3%ADtulo-2.png" width="100px;"  alt=""/> |<h1> [Victor Breia](https://www.linkedin.com/in/victor-breia/)</a>                                                                      </h1>                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Contate-me:                                                                                                                                                                                                                   | [![LinkedIn Badge](https://img.shields.io/badge/linkedin-blue?logo=linkedin&style=for-the-badge&logoColor=white)](https://www.linkedin.com/in/victor-breia/) [![Outlook badge](https://img.shields.io/badge/outlook-blue?logo=microsoftoutlook&style=for-the-badge&logoColor=white)](mailto:victordaschagas@outlook.com) |