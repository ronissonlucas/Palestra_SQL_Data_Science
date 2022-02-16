import pandas as pd
import numpy as np

# quantidade de linhas
def gerar_dados(tamanho_amostra = 100, SEED = 10):
    """Gera dados aleatórios para simular uma base de dados de clientes."""
    np.random.seed(SEED)
    
    # cidade
    lista_cidades = ['Salvador', 'Ilhéus', 'Itabuna', 'Porto Seguro', 
                     'Feira de Santana', 'Lauro de Freitas'
                    ]
    cidade = np.random.choice(lista_cidades, size = tamanho_amostra)
    
    #sexo
    sexo = np.random.choice(['Masculino', 'Feminino', 'Não Informado'], size = tamanho_amostra)
    
    # renda
    renda = np.random.randint(low = 1_000, high = 10_000, size = tamanho_amostra)
    
    # idade
    idade = np.random.randint(18, 65, size = tamanho_amostra)
    
    # profissão
    lista_profissoes = ['Professor', 'Cientista de Dados', 'Engenheiro de Dados', 'Economista',
                        'Advogado', 'Físico', 'Contador', 'Bancário'
                       ]
    profissao = np.random.choice(lista_profissoes, size = tamanho_amostra)
    
    # escolaridade
    escolaridade = ['Ensino Fundamental', 'Ensino Médio','Ensino Superior']
    grau_escolaridade = np.random.choice(escolaridade, size = tamanho_amostra)
    
    # score
    score = np.random.uniform(0, 10, size = tamanho_amostra).round(2)
    
    # tempo empregado
    tempo_empregado = np.random.randint(1, 30, size = tamanho_amostra)

    data = {
        'id': np.arange(1, tamanho_amostra+1),
        'cidade': cidade,
        'sexo': sexo,
        'idade': idade,
        'renda': renda,
        'escolaridade': grau_escolaridade,
        'score': score,
        'profissao': profissao,
        'tempo_empregado': tempo_empregado
    }

    df = pd.DataFrame(data)
    
    return df
