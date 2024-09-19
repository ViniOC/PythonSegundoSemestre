import oracledb

url = "oracle.fiap.com.br/orcl"
connection = oracledb.connect(user='RM556182', dsn=url, password='101003')

def create_film(cursor, titulo, diretor, ano_lancamento):
    cursor.execute("INSERT INTO t_py_filmes (titulo, diretor, ano_lancamento) VALUES (:1, :2, :3)",
                   (titulo, diretor, ano_lancamento))
    connection.commit()
    print("Filme adicionado com sucesso!")

def add_mock_films(cursor):
    filmes = [
        ('O Poderoso Chefão', 'Francis Ford Coppola', 1972),
        ('Cidadão Kane', 'Orson Welles', 1941),
        ('Pulp Fiction', 'Quentin Tarantino', 1994),
        ('A Lista de Schindler', 'Steven Spielberg', 1993),
        ('Forrest Gump', 'Robert Zemeckis', 1994),
        ('O Senhor dos Anéis: A Sociedade do Anel', 'Peter Jackson', 2001),
        ('Matrix', 'Lana Wachowski, Lilly Wachowski', 1999),
        ('Star Wars: Episódio IV - Uma Nova Esperança', 'George Lucas', 1977),
        ('Os Intocáveis', 'Brian De Palma', 1987),
        ('Titanic', 'James Cameron', 1997)
    ]
    
    for titulo, diretor, ano in filmes:
        create_film(cursor, titulo, diretor, ano)

def read_films(cursor):
    cursor.execute("SELECT * FROM t_py_filmes")
    for row in cursor.fetchall():
        print(row)

def update_film(cursor, film_id, titulo, diretor, ano_lancamento):
    cursor.execute("UPDATE t_py_filmes SET titulo = :1, diretor = :2, ano_lancamento = :3 WHERE id = :4",
                   (titulo, diretor, ano_lancamento, film_id))
    connection.commit()
    print("Filme atualizado com sucesso!")

def delete_film(cursor, film_id):
    cursor.execute("DELETE FROM t_py_filmes WHERE id = :1", (film_id,))
    connection.commit()
    print("Filme deletado com sucesso!")

def main():
    cursor = connection.cursor()

    # Adiciona filmes mock
    add_mock_films(cursor)

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Filme")
        print("2. Listar Filmes")
        print("3. Atualizar Filme")
        print("4. Deletar Filme")
        print("5. Sair")

        choice = input("Opção: ")

        if choice == '1':
            titulo = input("Título: ")
            diretor = input("Diretor: ")
            ano_lancamento = int(input("Ano de Lançamento: "))
            create_film(cursor, titulo, diretor, ano_lancamento)

        elif choice == '2':
            print("\nLista de Filmes:")
            read_films(cursor)

        elif choice == '3':
            film_id = int(input("ID do filme a ser atualizado: "))
            titulo = input("Novo Título: ")
            diretor = input("Novo Diretor: ")
            ano_lancamento = int(input("Novo Ano de Lançamento: "))
            update_film(cursor, film_id, titulo, diretor, ano_lancamento)

        elif choice == '4':
            film_id = int(input("ID do filme a ser deletado: "))
            delete_film(cursor, film_id)

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()
