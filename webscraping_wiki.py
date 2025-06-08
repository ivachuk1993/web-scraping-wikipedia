import pandas as pd

url_wikipedia = "https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_esperan%C3%A7a_m%C3%A9dia_de_vida_%C3%A0_nascen%C3%A7a"

print(f"Verificando tabelas em: {url_wikipedia}")

try:
    tabelas = pd.read_html(url_wikipedia)

    print(f"Número total de tabelas encontradas na página: {len(tabelas)}")

    # --- Iterando e inspecionando todas as tabelas ---
    print("\n--- Inspecionando todas as tabelas encontradas: ---")
    for i, tabela_atual in enumerate(tabelas): # 'tabelas' é a lista de DataFrames
        print(f"\n--- Tabela {i} ---")
        print("Primeiras 5 linhas:")
        print(tabela_atual.head()) # Comando que verifica as 5 primeiras linhas
        print("Colunas:")
        print(tabela_atual.columns)
        print("-" * 40) # Linha de separação
    print("--- Fim da Inspeção ---")
    # --- Final ---


    # --- Escolhendo a tabela desejada (a contagem em inicia em 0, como quero a segunda tabela, será a 1) ---
    if len(tabelas) > 1:
        tabela_desejada = tabelas[1] # Acessa a segunda tabela (índice 1)

        print("\n--- Conteúdo das primeiras 5 linhas da segunda tabela ---")
        print(tabela_desejada.head())

        print("\nColunas da segunda tabela:")
        print(tabela_desejada.columns)

        #nome_arquivo_csv = "expectativa_de_vida_segunda_tabela.csv"
        #tabela_desejada.to_csv(nome_arquivo_csv, index=False, encoding='utf-8')
        # print(f"\nSegunda tabela salva com sucesso como '{nome_arquivo_csv}'.")

    else:
        print("A página não possui uma segunda tabela para ser acessada (foram encontradas menos de duas tabelas).")

except Exception as e:
    print(f"Ocorreu um erro ao raspar a página: {e}")
    print("Por favor, verifique a URL, sua conexão com a internet ou se a biblioteca 'lxml' está instalada.")