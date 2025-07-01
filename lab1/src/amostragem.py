import pandas as pd

def amostragem_sem_reposicao(input_csv: str, output_csv: str, tamanho_amostra: int, random_state: int = None):
    try:
        df = pd.read_csv(input_csv)
        total_registros = len(df)

        if tamanho_amostra > total_registros:
            raise ValueError(f"Tamanho da amostra ({tamanho_amostra}) maior que o número de registros ({total_registros}) no arquivo.")

        amostra = df.sample(n=tamanho_amostra, replace=False, random_state=random_state)

        amostra.to_csv(output_csv, index=False)
        print(f"Amostra de {tamanho_amostra} registros salva com sucesso em '{output_csv}'.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{input_csv}' não encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{input_csv}' está vazio ou mal formatado.")
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
