import json

with open("livros.json", "r", encoding="utf-8") as arquivo:
    livros = json.load(arquivo)

def mostrar(livro):
    print(
        "\nCódigo do Livro:", livro["codigo"],
        "\nTítulo da Obra:", livro["titulo"],
        "\nAutor da Obra:", livro["autor"],
        "\nAno da Obra:", livro["ano"],
        "\n"
    )

def carregarLivros():
    for livro in livros:
        mostrar(livro)

def salvarDados():
    with open("livros.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)

def incluirLivros():
    codigo = input("\nDigite o Código do Livro: ")
    titulo = input("Digite o Título da Obra: ")
    autor = input("Digite o Autor da Obra: ")
    ano = int(input("Digite o Ano de Publicação da Obra: "))
    
    livros.append({
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
    })

    salvarDados()

def excluirLivros():
    titulo = input("\nQual o nome da Obra que deseja excluir: ")

    for livro in livros:
        if livro["titulo"] == titulo:
            livros.remove(livro)
            salvarDados()
            print("\nLivro Excluído")
            return
    print("\nLivro não encontrado")

def alterarLivros():
    titulo = input("Qual o nome da Obra que deseja alterar: ")

    for livro in livros:

        if livro["titulo"] == titulo:
            print("\nCódigo da Obra: ", livro["codigo"])
            print("Título da Obra: ", livro["titulo"])
            print("Autor da Obra: ", livro["autor"])
            print("Ano de Publicação da Obra: ", livro["ano"])
            print("\nO que deseja alterar?: ")
            print("\n1 - Código")
            print("2 - Título")
            print("3 - Autor")
            print("4 - Ano")

            numeroDigitado = int(input("\nDigite a opção desejada: "))

            if numeroDigitado == 1:
                livro["codigo"] = input("Qual o novo Código da Obra: ")
            elif numeroDigitado == 2:
                livro["titulo"] = input("Qual o novo Título da Obra: ")
            elif numeroDigitado == 3:
                livro["autor"] = input("Qual o novo Autor da Obra: ")
            elif numeroDigitado == 4:
                livro["ano"] = int(input("Qual o novo Ano da Obra: "))
            else:
                print("Opção não encontrada.")
                return
            salvarDados()
            print("Livro alterado!!")
            return
        
    print("Livro não encontrado.")

def pesquisarLivros():
    texto = input("\nDigite o texto para pesquisar: ").lower()
    Pesquisa = False

    for livro in livros:
        if texto in livro["titulo"].lower() or texto in livro["autor"].lower():
            mostrar(livro)
            Pesquisa = True

    if Pesquisa == False:
        print("Nenhum livro encontrado.")


def listar_por_codigo():
    ordenados = sorted(livros, key=lambda livro: livro["codigo"])

    for livro in ordenados:
        mostrar(livro)

def listar_por_ano():
    ordenados = sorted(livros, key=lambda livro: livro["ano"])

    for livro in ordenados:
        mostrar(livro)

while True:
    print("\n--- Cadastro de Livros Biblioteca ---")
    print("\n1 - Incluir livro")
    print("2 - Listar livros")
    print("3 - Excluir livros")
    print("4 - Alterar informações dos livros")
    print("5 - Pesquisar por Informação")
    print("6 - Listar por Código")
    print("7 - Listar por Ano")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        incluirLivros()
    elif opcao == "2":
        carregarLivros()
    elif opcao == "3":
        excluirLivros()
    elif opcao == "4":
        alterarLivros()
    elif opcao == "5":
        pesquisarLivros()
    elif opcao == "6":
        listar_por_codigo()
    elif opcao == "7":
        listar_por_ano()
    elif opcao == "0":
        break
    else:
        print("Opção inválida")     