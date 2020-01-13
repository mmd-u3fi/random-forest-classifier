from c45.classifier import C45
from bootstrapper import Bootstrap
from collections import Counter

class RandomForest(object):
    def __init__ (self, number_of_trees, dataset, target_column):
        bootstrap = Bootstrap(dataset)
        self.target_column = target_column
        self.trees = [C45(bootstrap.sample(), target_column) for i in range(number_of_trees)]
        for tree in self.trees:
            tree.create_tree()
    def predict(self, dataset):
        predictions = [tree.predict(dataset) for tree in self.trees]
        return self.most_common_prediction(self.transpose(predictions))
    def transpose(self, predictions):
        trans = []
        column_size = len(predictions[0])
        row_size = len(predictions)
        for j in range(column_size):
            temp = [predictions[i][j] for i in range(row_size)]
            trans.append(temp)
        return trans
    def most_common_prediction(self, predictions):
        counts = [Counter(predictions[i]).most_common(1) for i in range(len(predictions))]
        final = [i[0][0] for i in counts]
        return final
    def accuracy(self, dataset):
        preds = self.predict(dataset)
        correct_guesses = 0
        for x, y in zip(preds, dataset[self.target_column]):
            if x == y:
                correct_guesses += 1
        return correct_guesses / len(dataset[self.target_column])