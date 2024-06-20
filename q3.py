import pandas as pd

# Dados fornecidos
data = {
    'Mídia': [
        'Animação', 'Animação', 'Animação', 'Animação', 'Animação',
        'Imagem', 'Imagem', 'Imagem', 'Imagem', 'Imagem',
        'Texto', 'Texto', 'Texto', 'Texto', 'Texto'
    ],
    'Supino Reto': [9, 9, 8, 22, 24, 28, 11, 19, 43, 30, 13, 49, 43, 24, 33],
    'Crucifixo': [11, 29, 26, 26, 56, 40, 20, 13, 52, 26, 26, 33, 31, 37, 29],
    'Rosca Direta Alternada': [14, 15, 31, 20, 11, 23, 24, 25, 27, 20, 22, 18, 14, 15, 16],
    'Afundo': [13, 34, 23, 17, 7, 18, 12, 14, 33, 13, 18, 15, 20, 12, 22],
    'Agachamento Livre': [18, 45, 57, 28, 34, 37, 35, 18, 30, 18, 12, 26, 21, 20, 19],
    'Levantamento Terra': [26, 8, 24, 9, 13, 30, 27, 16, 17, 16, 18, 32, 22, 18, 17]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Cálculo das médias
mean_times = df.groupby('Mídia').mean()

import ace_tools as tools; tools.display_dataframe_to_user(name="Comparative Time Analysis by Media Type", dataframe=mean_times)

mean_times
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Perform ANOVA for each exercise
anova_results = {}
posthoc_results = {}

exercises = ['Supino Reto', 'Crucifixo', 'Rosca Direta Alternada', 'Afundo', 'Agachamento Livre', 'Levantamento Terra']

for exercise in exercises:
    groups = [df[df['Mídia'] == media][exercise] for media in df['Mídia'].unique()]
    anova_results[exercise] = f_oneway(*groups)

    # Perform Tukey's HSD test if ANOVA is significant
    if anova_results[exercise].pvalue < 0.05:
        tukey = pairwise_tukeyhsd(endog=df[exercise], groups=df['Mídia'], alpha=0.05)
        posthoc_results[exercise] = tukey.summary()

import ace_tools as tools; tools.display_dataframe_to_user(name="ANOVA Results for Each Exercise Time", dataframe=pd.DataFrame(anova_results).T)

anova_results, posthoc_results