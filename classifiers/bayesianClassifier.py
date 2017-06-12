from classifiers.classifier import Classifier;
from sklearn.naive_bayes import MultinomialNB;
import numpy as np;

class BayesianClassifier(Classifier):
  def __init__(self, data, dataMap, strategyMap):
    Classifier.__init__(self, data, dataMap, strategyMap);

  def train(self):
    ''' Training the classifier to get better predictions - using naive bayes '''
    self.naive_bayes = MultinomialNB();
    self.options = {'fit': True};

    for column in self.X_train:
      strategy = self.strategyMap[column](self.X_train[column], self.options);
      matrix = strategy.compute();
      self.naive_bayes.fit(matrix.toarray(), list(self.y_train.values));

  def test(self):
    ''' Testing the classifier predictions - using naive bayes '''
    self.options['fit'] = False;
    self.predicts = [];

    for column in self.X_test:
      strategy = self.strategyMap[column](self.X_test[column], self.options);
      matrix = strategy.compute();
      self.predicts.append(self.naive_bayes.predict(matrix.toarray()));