import pandas

data = pandas.read_csv('squirrel_data.csv')
print(data['Primary Fur Color'].value_counts())

gray = data['Primary Fur Color'].value_counts().Gray
cinnamon = data['Primary Fur Color'].value_counts().Cinnamon
black = data['Primary Fur Color'].value_counts().Black

data_dict = {
    'Fur Color': ['gray', 'cinnamon', 'black'],
    'Count': [gray, cinnamon, black],
}

data = pandas.DataFrame(data_dict)
data.to_csv('squirrel_fur_count.csv')
