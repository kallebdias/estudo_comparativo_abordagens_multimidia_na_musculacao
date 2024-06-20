# Create a DataFrame with the provided data
new_data = {
    'Mídia': ['Animação', 'Animação', 'Animação', 'Animação', 'Animação',
              'Imagem', 'Imagem', 'Imagem', 'Imagem', 'Imagem',
              'Texto', 'Texto', 'Texto', 'Texto', 'Texto'],
    '[1 - Supino Reto]': [3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 2, 3, 1, 3, 2],
    '[2 - Crucifixo]': [3, 3, 3, 3, 2, 1, 2, 3, 1, 2, 2, 2, 1, 3, 2],
    '[3 - Rosca Direta Alternada]': [3, 2, 3, 3, 3, 3, 2, 2, 3, 3, 2, 1, 1, 2, 1],
    '[4 - Afundo]': [3, 2, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 1, 3, 2],
    '[5 - Agachamento Livre com Barra]': [2, 3, 3, 3, 2, 2, 2, 2, 3, 2, 2, 3, 3, 3, 3],
    '[6 - Levantamento Terra]': [3, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(new_data)

# Group by 'Mídia' and calculate the mean score for each exercise
grouped_new_data = df.groupby('Mídia').mean()

import ace_tools as tools; tools.display_dataframe_to_user(name="Grouped Exercise Performance by Media Type (Updated Data)", dataframe=grouped_new_data)

grouped_new_data

from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Perform ANOVA for each exercise
anova_results = {}
posthoc_results = {}

exercises = df.columns[1:]

for exercise in exercises:
    groups = [df[df['Mídia'] == media][exercise] for media in df['Mídia'].unique()]
    anova_results[exercise] = f_oneway(*groups)

    # Perform Tukey's HSD test if ANOVA is significant
    if anova_results[exercise].pvalue < 0.05:
        tukey = pairwise_tukeyhsd(endog=df[exercise], groups=df['Mídia'], alpha=0.05)
        posthoc_results[exercise] = tukey.summary()

import ace_tools as tools; tools.display_dataframe_to_user(name="ANOVA Results for Each Exercise", dataframe=pd.DataFrame(anova_results).T)

anova_results, posthoc_results