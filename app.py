import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import openpyxl as py




data = pd.DataFrame({
    'Aluno': ['Ana', 'Pedro', 'Maria'],
    'Matemática': [85, 79, 92],
    'Física': [90, 82, 89],
    'Química': [78, 88, 94],
    'Biologia': [92, 85, 91]
})
# df = pd.DataFrame(data)
caminho_arquivo_excel = 'dados2.xlsx'
data.to_excel(caminho_arquivo_excel, index=False)














# df = pd.read_excel('BASE.xlsx')

# data = ({'colunas':['a','b','c','d'],
#          'x':[1,3,4,6],
#          'y':[81,89,76,45]})


# caminho_arquio = 'dados2.xlsx'





# df = pd.DataFrame(data)

# df.to_excel('BASE.xlsx', index=False)

# sns.barplot(data=df, x='vendedor', y='vendas')
# plt.show()