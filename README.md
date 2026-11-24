
# Cadastro de Livros - Biblioteca

## 1. Introdução

O projeto consiste no desenvolvimento de um sistema de cadastro e gerenciamento de livros para uma biblioteca, utilizando a linguagem de programação Python.

O sistema permite realizar operações de inclusão, consulta, alteração e exclusão de livros, além de oferecer recursos de pesquisa e organização dos registros por código e ano de publicação.

Para armazenar as informações, foi utilizado um arquivo JSON, permitindo que os dados permaneçam salvos mesmo após o encerramento do programa.

## 2. Objetivo do Projeto

O objetivo é desenvolver uma aplicação simples para gerenciamento de livros, colocando em prática os conhecimentos adquiridos na disciplina de Estrutura de Dados e Organização de Arquivos.

O projeto busca trabalhar principalmente com listas, dicionários, funções, estruturas de repetição, condicionais e manipulação de arquivos externos.

## 3. Tecnologias e Recursos Utilizados

| Tecnologia / Recurso | Finalidade |
|---|---|
| Python | Linguagem utilizada no desenvolvimento. |
| JSON | Formato utilizado para armazenamento dos dados. |
| Módulo `json` | Leitura e gravação dos arquivos JSON. |
| `open()` | Abertura e manipulação do arquivo. |
| Listas | Armazenamento dos registros dos livros. |
| Dicionários | Organização das informações de cada livro. |
| Funções | Separação e organização das operações do sistema. |
| `sorted()` | Ordenação dos livros por código e ano. |

## 4. Estrutura dos Dados

O sistema utiliza uma lista chamada `livros`, que armazena os registros cadastrados.

Cada livro é representado por um dicionário, contendo quatro informações:

| Campo | Descrição | Tipo de dado |
|---|---|---|
| `codigo` | Código de identificação do livro. | String |
| `titulo` | Título da obra. | String |
| `autor` | Nome do autor. | String |
| `ano` | Ano de publicação da obra. | Inteiro |

### Exemplo de estrutura do arquivo JSON

```json
[
    {
        "codigo": "01",
        "titulo": "Peter Pan",
        "autor": "Vinicius",
        "ano": 2007
    },
    {
        "codigo": "02",
        "titulo": "Bíblia",
        "autor": "Jesus",
        "ano": 1
    }
]
```

## 5. Funcionalidades do Sistema

O sistema possui sete funcionalidades principais, acessadas por meio de um menu interativo no terminal.

### 5.1. Incluir Livro

Permite cadastrar um novo livro no sistema, solicitando as seguintes informações:

- Código do livro;
- Título da obra;
- Autor;
- Ano de publicação.

Após o preenchimento, os dados são adicionados à lista `livros` por meio do método `append()` e salvos no arquivo JSON.

### 5.2. Listar Livros

Exibe todos os livros cadastrados, apresentando individualmente o código, título, autor e ano de publicação.

A função percorre a lista utilizando uma estrutura de repetição `for` e chama a função `mostrar()` para exibir cada registro.

### 5.3. Excluir Livros

Permite excluir um livro cadastrado a partir do título da obra.

O sistema percorre os registros e verifica se existe um livro com o título informado. Quando encontra, utiliza o método `remove()` para removê-lo da lista e atualiza o arquivo JSON.

Caso não encontre o livro, apresenta uma mensagem informando que ele não foi localizado.

### 5.4. Alterar Informações dos Livros

Permite modificar as informações de um livro já cadastrado.

Primeiramente, o sistema solicita o título da obra que deseja alterar. Após localizar o registro, apresenta suas informações e disponibiliza quatro opções:

1. Alterar código;
2. Alterar título;
3. Alterar autor;
4. Alterar ano de publicação.

Após a escolha, o sistema solicita a nova informação, atualiza o dicionário correspondente e salva as alterações no arquivo JSON.

### 5.5. Pesquisar por Informação

Permite pesquisar livros utilizando parte do título ou do nome do autor.

O usuário informa um texto, e o sistema percorre a lista verificando se esse conteúdo está presente no título ou no autor.

A pesquisa utiliza o método `lower()` para transformar os textos em letras minúsculas, permitindo encontrar resultados independentemente de diferenças entre letras maiúsculas e minúsculas.

Caso nenhum resultado seja encontrado, o sistema apresenta uma mensagem informativa.

### 5.6. Listar por Código

Apresenta os livros organizados em ordem crescente de código.

Para realizar essa operação, é utilizada a função `sorted()`, juntamente com `lambda`, que define o campo `codigo` como critério de ordenação.

### 5.7. Listar por Ano

Apresenta os livros organizados em ordem crescente de ano de publicação, começando pelas obras mais antigas.

Assim como na ordenação por código, utiliza a função `sorted()` e `lambda`, tendo o campo `ano` como critério de organização.

## 6. Organização das Funções

O código foi dividido em funções para facilitar a organização, manutenção e compreensão do sistema.

| Função | Responsabilidade |
|---|---|
| `mostrar(livro)` | Exibir as informações de um livro. |
| `carregarLivros()` | Percorrer e listar os livros cadastrados. |
| `salvarDados()` | Salvar os registros no arquivo JSON. |
| `incluirLivros()` | Cadastrar novos livros. |
| `excluirLivros()` | Remover livros pelo título. |
| `alterarLivros()` | Modificar informações de livros existentes. |
| `pesquisarLivros()` | Pesquisar pelo título ou autor. |
| `listar_por_codigo()` | Ordenar os livros pelo código. |
| `listar_por_ano()` | Ordenar os livros pelo ano de publicação. |

## 7. Armazenamento e Manipulação de Arquivos

O armazenamento dos dados é realizado por meio do arquivo `livros.json`, utilizando o módulo `json` do Python.

O sistema utiliza duas operações principais:

### Leitura dos dados

```python
with open("livros.json", "r", encoding="utf-8") as arquivo:
    livros = json.load(arquivo)
```

Essa operação realiza a leitura do arquivo JSON e transforma seu conteúdo em uma estrutura de dados Python.

### Gravação dos dados

```python
with open("livros.json", "w", encoding="utf-8") as arquivo:
    json.dump(livros, arquivo, ensure_ascii=False, indent=4)
```

Essa operação grava os dados atualizados no arquivo JSON.

O parâmetro `ensure_ascii=False` permite manter caracteres especiais e acentos legíveis, enquanto `indent=4` organiza a formatação do arquivo.

Dessa maneira, as informações cadastradas não são perdidas quando o programa é encerrado.

## 8. Funcionamento do Menu Principal

O menu principal é executado por meio de uma estrutura de repetição `while True`, que mantém o sistema funcionando até que o usuário escolha a opção de saída.

A escolha é recebida por meio da função `input()` e analisada utilizando estruturas condicionais `if`, `elif` e `else`.

Cada opção direciona o usuário para a função correspondente.

O programa é encerrado quando a opção `0 - Sair` é selecionada, utilizando o comando `break`.

## 9. Estruturas de Programação Utilizadas

Durante o desenvolvimento, foram utilizadas diferentes estruturas e recursos da linguagem Python:

- **Listas:** utilizadas para armazenar todos os livros cadastrados.
- **Dicionários:** utilizados para organizar as informações individuais de cada livro.
- **Funções (`def`):** utilizadas para dividir o programa em operações independentes.
- **Estrutura `for`:** utilizada para percorrer os registros cadastrados.
- **Estrutura `while`:** utilizada para manter o menu principal em execução.
- **Estruturas condicionais (`if`, `elif`, `else`):** utilizadas para verificar condições e direcionar as operações.
- **Método `append()`:** utilizado para adicionar novos livros à lista.
- **Método `remove()`:** utilizado para excluir livros.
- **Função `sorted()`:** utilizada para ordenar os registros.
- **Expressões `lambda`:** utilizadas para definir os critérios de ordenação.
- **Manipulação de arquivos:** utilizada para realizar a leitura e gravação dos dados em JSON.

## 10. Considerações Finais

O desenvolvimento deste projeto permitiu aplicar na prática os conhecimentos adquiridos na disciplina de Estrutura de Dados e Organização de Arquivos.

Durante a construção do sistema, foi possível trabalhar com listas, dicionários, funções, estruturas condicionais, estruturas de repetição e manipulação de arquivos JSON.

O resultado foi um sistema funcional de cadastro e gerenciamento de livros, que permite organizar e consultar informações de maneira simples, mantendo os dados armazenados mesmo após o encerramento da aplicação.

## 11. Estrutura dos Arquivos do Projeto

O projeto está organizado da seguinte maneira:

```text
Cadastro de Livros/
│
├── app.py
│
└── livros.json
```

- **app.py:** contém o código-fonte do sistema e todas as suas funcionalidades.
- **livros.json:** armazena os registros dos livros cadastrados.
