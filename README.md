#  Gerador de Senhas em Python

Um gerador de senhas simples e funcional feito com Python, que permite personalizar o tamanho da senha e os tipos de caracteres utilizados. A senha gerada é automaticamente copiada para a área de transferência.

## Funcionalidades

- Definição do tamanho da senha
- Escolha dos tipos de caracteres:
  - Letras minúsculas
  - Letras maiúsculas
  - Números
  - Caracteres especiais
- Geração aleatória e segura da senha
- Cópia automática da senha para a área de transferência

##  Tecnologias utilizadas

- Python 3.x
- Bibliotecas:
  - `random`
  - `string`
  - `sys`
  - `pyperclip`

##  Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/gerador-senhas-python.git
cd gerador-senhas-python
```
2. Instale a biblioteca pyperclip(se ainda não tiver):

```bash
pip install pyperclip
```
3. Execute o script:

```bash
python gerador_senha.py
```
## Estrutura do projeto
gerador-senhas-python/
├── gerador_senha.py
├── README.md
└── .gitignore

## Arquivos ignorados (via .gitignore)
gitignore
Copiar
Editar
.idea/
__pycache__/
*.pyc

Feito com foco em aprendizado e prática de Python por João Felipe.
