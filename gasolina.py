import pandas as pd
import seaborn as sns

df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=df, x='dia', y='venda', marker='o')
  grafico.set(title='EVOLUÇÃO PREÇO DA GASOLINA POR DIA', xlabel='Dia', ylabel='Preço')

grafico.figure.savefig('gasolina.png')