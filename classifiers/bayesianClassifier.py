from classifiers.classifier import Classifier;

class BayesianClassifier(Classifier):
  def __init__(self, data, dataMap, strategyMap):
    Classifier.__init__(self, data, dataMap, strategyMap);