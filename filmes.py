# filmes organizados por gênero
filmes_por_genero = {
    'ação': ['Duro de Matar', 'Velozes e Furiosos', 'John Wick'],
    'comédia': ['Se Beber, Não Case', 'Superbad', 'Minha Mãe é uma Peça'],
    'drama': ['O Pianista', 'A Lista de Schindler', 'Clube da Luta'],
    'ficção científica': ['Interestelar', 'Blade Runner', 'Matrix'],
    'terror': ['Invocação do Mal', 'Pânico', 'Hereditário'],
    'romance': ['Diário de uma Paixão', 'Titanic', 'Orgulho e Preconceito']
}


def mostrar_recomendacoes(preferencias):

    filmes_recomendados = []

    for genero in preferencias:
        if genero.lower() in filmes_por_genero:
            filmes_recomendados.extend(filmes_por_genero[genero.lower()])

    # Removendo duplicatas (caso o usuário tenha escolhido gêneros com filmes em comum)
    filmes_recomendados = list(set(filmes_recomendados))

    return filmes_recomendados


def main():
    print("=== Bem-vindo ao Sistema de Recomendação de Filmes ===\n")

    # Mostrando a lista de gêneros disponíveis
    generos = list(filmes_por_genero.keys())
    print("Que gênero você quer assistir?")
    for i, genero in enumerate(generos, start=1):
        print(f"({i}) {genero.capitalize()}")

    # Solicitando as preferências do usuário
    print("\nDigite os números dos gêneros separados por espaço (ex.: 1 3):")
    entrada_usuario = input("> ")

    # Processando a entrada do usuário
    try:
        indices_selecionados = [int(idx.strip()) - 1 for idx in entrada_usuario.split()]
        preferencias = [generos[i] for i in indices_selecionados if 0 <= i < len(generos)]
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números correspondentes aos gêneros.")
        return

    # Gerando recomendações
    recomendacoes = mostrar_recomendacoes(preferencias)

    # Mostrando os resultados
    if recomendacoes:
        print("\nCom base em suas preferências, recomendamos os seguintes filmes:")
        for filme in recomendacoes:
            print(f"- {filme}")
    else:
        print("\nDesculpe, não encontramos recomendações para seus gêneros favoritos.")


if __name__ == "__main__":
    main()
