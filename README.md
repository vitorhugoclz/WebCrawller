# WebCrawller

# Requisitos
1. Ter Python 3.8 ou superior instalado em sua máquina caso não tenha, acessar (https://www.python.org/downloads/) para baixar a versão mais recente

2. Ter instalado a ferramenta pip para download de pacotes Python, caso não tenha acessar (https://pypi.org/project/pip/)

3. Ter intalado a ferramenta de ambiente virtual do Python ("venv"), pode ser acessada (https://pypi.org/project/virtualenv/)

4. Faça um clone do repositório no ambiente local 
````
git clone https://github.com/vitorhugoclz/WebCrawller.git
````
5. na pasta onde projeto foi clonado crie um ambiente virtual como descrito em https://docs.python.org/pt-br/3/tutorial/venv.html

6. Ative o ambiente virtual segundo seu sistema operacional, também descrito em https://docs.python.org/pt-br/3/tutorial/venv.html
  
7. instale a ferramenta selenium segundo tutorial presente em https://selenium-python.readthedocs.io/installation.html

8. É necessário ter apenas o driver do Firefox na mesma pasta que o código main.py, não precisando instalar o Selenium server

9.  com ambiente virtual ativo e com driver no mesma pasta que o código main.py basta executar o código python.

### obs:
para trocar a url é necessário editar o arquivo e trocar o valor da variável url. O código foi feito para baixar o html de sub-páginas do dominio https://artofproblemsolving.com/community/, outros sites não funcionaram. 

Alguns link de exemplo foram deixados no código.