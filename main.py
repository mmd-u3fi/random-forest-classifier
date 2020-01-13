from dataset_parser import parse_dataset
from test_train_split import dataset_split
from random_forest import RandomForest

dataset = parse_dataset()
train, test = dataset_split(dataset, 0.15)
r = RandomForest(5, train, 'class')
print(r.accuracy(test))