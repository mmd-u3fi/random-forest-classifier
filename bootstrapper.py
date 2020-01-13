import random
class Bootstrap(object):
    def __init__(self, dataset):
        self.dataset = dataset
        self.sample_size = len(dataset[list(dataset.keys())[0]])
    def sample(self):
        size = random.randint(int(self.sample_size / 3), self.sample_size)
        indexes = [random.randint(0, self.sample_size - 1) for i in range(size)]
        new_set = {k: [self.dataset[k][v] for v in indexes] for k in self.dataset}
        return new_set