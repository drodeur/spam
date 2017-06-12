from sklearn.model_selection import train_test_split

class Classifier(object):

  def __init__(self, data, dataMap, strategyMap):
    self.data = data;
    self.labelIndex = self.data.columns.get_loc('label');
    self.map = dataMap;
    self.strategyMap = strategyMap;

    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
      data.select(lambda name: name != 'label', 1), data['label'], random_state=1);

    self.convertAll();

  def convertAll(self):
    ''' Process to convert initialData, train and test subsets '''

    self.convertInitialData();
    self.convertSubset(self.y_train);
    self.convertSubset(self.y_test);

  def convertInitialData(self, stopIndex=-1):
    ''' Convert the labels to numerical representation '''

    for index, row in self.data.iterrows():
      row[self.labelIndex] = self.map[row[self.labelIndex]];

      if self.must_stop(stopIndex, index):
        break;

  def convertSubset(self, labels, stopIndex=-1):
    ''' Convert the labels to numerical representation '''

    counter = 0;
    for index, label in labels.iteritems():
      labels[index] = self.map[label];

      if self.must_stop(stopIndex, counter):
        break;
      counter += 1;

  def must_stop(self, stopIndex, index):
    ''' Is it time to break the loop? '''
    return stopIndex > -1 and index >= stopIndex;

  def stats(self, label):
    ''' Print accuracy, precision, recall and F1 scores '''
    accuracy = precision = recall = falseNegative = falsePositive = 0;
    labels = list(self.y_test);
    total = len(labels);
    hypothesis = self.map[label];

    for predictRow in self.predicts:
      for index, predict in enumerate(predictRow):
        if predict == labels[index]:
          accuracy += 1;

          if labels[index] == hypothesis:
            precision += 1;
            recall += 1;
        elif labels[index] == hypothesis:
          falseNegative += 1;
        else:
          falsePositive += 1;

    accuracy /= total;
    precision /= precision + falsePositive;
    recall /= recall + falseNegative;

    print("Accuracy :\t{}".format(accuracy));
    print("Precision :\t{}".format(precision));
    print("Recall :\t{}".format(recall));
    print("F1 :\t\t{}".format((precision + recall) / 2.0));

  def test(self):
    ''' Testing the classifier predictions '''

    for column in self.X_test:
      strategy = self.strategyMap[column](self.X_test[column]);
      strategy.compute();


  def train(self):
    ''' Training the classifier to get better predictions '''

    for column in self.X_train:
      strategy = self.strategyMap[column](self.X_train[column]);
      strategy.compute();


  def unconvertInitialData(self, stopIndex=-1):
    ''' Reversed engineering of convert method for pretty print'''

    for index, row in self.data.iterrows():
      for key, value in self.map.items():
        if value == row[self.labelIndex]:
          row[self.labelIndex] = key;
          break;

      if self.must_stop(stopIndex, index):
        break;

  def unconvertSubset(self, labels, stopIndex=-1):
    ''' Reversed engineering of convert method for pretty print'''

    counter = 0;
    for index, label in labels.iteritems():
      for key, value in self.map.items():
        if value == label:
          label[index] = key;
          break;

      if self.must_stop(stopIndex, counter):
        break;
      counter += 1;

  def __str__(self):
    ''' Usefull representation for print the dataset '''

    self.unconvertInitialData(5);
    output = self.data.head(5).to_string() + '\n';
    self.convertInitialData(5);


    output += '----------------------------------------------------------\n';
    output += 'Number of rows in the total set: {}\n'.format(self.data.shape[0]);
    output += 'Number of rows in the training set: {}\n'.format(self.X_train.shape[0]);
    output += 'Number of rows in the test set: {}\n'.format(self.X_test.shape[0]);
    output += '-----------------------------------------------------------\n';

    return output;
