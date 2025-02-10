# Dicionário com filmes pré-definidos organizados por gênero
movies_by_genre = {
    'ação': ['Duro de Matar', 'Velozes e Furiosos', 'John Wick'],
    'comédia': ['Se Beber, Não Case', 'Superbad', 'Minha Mãe é uma Peça'],
    'drama': ['O Pianista', 'A Lista de Schindler', 'Clube da Luta'],
    'ficção científica': ['Interestelar', 'Blade Runner', 'Matrix'],
    'terror': ['Invocação do Mal', 'Pânico', 'Hereditário'],
    'romance': ['Diário de uma Paixão', 'Titanic', 'Orgulho e Preconceito']
}


def show_recommendations(preferences):
    """
    Função para recomendar filmes com base nas preferências do usuário.
    """
    recommended_movies = []

    # Iterando sobre os gêneros favoritos do usuário
    for genre in preferences:
        if genre.lower() in movies_by_genre:
            recommended_movies.extend(movies_by_genre[genre.lower()])

    # Removendo duplicatas (caso o usuário tenha escolhido gêneros com filmes em comum)
    recommended_movies = list(set(recommended_movies))

    return recommended_movies


def main():
    print("=== Bem-vindo ao Sistema de Recomendação de Filmes ===\n")

    # Mostrando a lista de gêneros disponíveis
    genres = list(movies_by_genre.keys())
    print("Que gênero você quer assistir?")
    for i, genre in enumerate(genres, start=1):
        print(f"({i}) {genre.capitalize()}")

    # Solicitando as preferências do usuário
    print("\nDigite os números dos gêneros separados por espaço (ex.: 1 3):")
    user_input = input("> ")

    # Processando a entrada do usuário
    try:
        selected_indices = [int(idx.strip()) - 1 for idx in user_input.split()]
        preferences = [genres[i] for i in selected_indices if 0 <= i < len(genres)]
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números correspondentes aos gêneros.")
        return

    # Gerando recomendações
    recommendations = show_recommendations(preferences)

    # Mostrando os resultados
    if recommendations:
        print("\nCom base em suas preferências, recomendamos os seguintes filmes:")
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print("\nDesculpe, não encontramos recomendações para seus gêneros favoritos.")


if __name__ == "__main__":
    main()