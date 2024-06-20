import pandas as pd
from scipy.stats import chi2_contingency

# Dados fornecidos
data = {
    'Mídia': [
        'Animação', 'Animação', 'Animação', 'Animação', 'Animação',
        'Imagem', 'Imagem', 'Imagem', 'Imagem', 'Imagem',
        'Texto', 'Texto', 'Texto', 'Texto', 'Texto'
    ],
    'Facilidade de Entendimento': [
        'Achei fácil', 'Achei fácil', 'Achei fácil', 'Achei fácil', 'Achei fácil',
        'Achei fácil', 'Senti dificuldade', 'Achei fácil', 'Achei fácil', 'Achei fácil',
        'Senti dificuldade', 'Achei fácil', 'Achei fácil', 'Senti dificuldade', 'Achei fácil'
    ],
    'Preferência para Aprender Novos Exercícios': [
        'Sim', 'Sim', 'Sim', 'Sim', 'Sim',
        'Sim', 'Não', 'Sim', 'Sim', 'Sim',
        'Não', 'Não', 'Sim', 'Sim', 'Não'
    ],
    'Preferência por Meio de Instrução': [
        'Ambos, dependendo da situação', 'Instrutores presenciais', 'Ambos, dependendo da situação',
        'Ambos, dependendo da situação', 'Instrutores presenciais', 'Ambos, dependendo da situação',
        'Instrutores presenciais', 'Ambos, dependendo da situação', 'Instrutores presenciais',
        'Instrutores presenciais', 'Instrutores presenciais', 'Instrutores presenciais', 'Instrutores presenciais',
        'Ambos, dependendo da situação', 'Instrutores presenciais'
    ]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Tabelas de contingência e testes qui-quadrado

# Facilidade de Entendimento
contingency_table1 = pd.crosstab(df['Mídia'], df['Facilidade de Entendimento'])
chi2_1, p_1, dof_1, expected_1 = chi2_contingency(contingency_table1)

# Preferência para Aprender Novos Exercícios
contingency_table2 = pd.crosstab(df['Mídia'], df['Preferência para Aprender Novos Exercícios'])
chi2_2, p_2, dof_2, expected_2 = chi2_contingency(contingency_table2)

# Preferência por Meio de Instrução
contingency_table3 = pd.crosstab(df['Mídia'], df['Preferência por Meio de Instrução'])
chi2_3, p_3, dof_3, expected_3 = chi2_contingency(contingency_table3)

import ace_tools as tools; tools.display_dataframe_to_user(name="Contingency Table for Ease of Understanding", dataframe=contingency_table1)
import ace_tools as tools; tools.display_dataframe_to_user(name="Contingency Table for Preference for Learning New Exercises", dataframe=contingency_table2)
import ace_tools as tools; tools.display_dataframe_to_user(name="Contingency Table for Preference for Instruction Mode", dataframe=contingency_table3)

chi2_1, p_1, chi2_2, p_2, chi2_3, p_3
