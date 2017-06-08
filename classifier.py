

class Classifier(object):

  def __init__(self, data, dataMap):
    self.data = data;
    self.labelIndex = self.data.columns.get_loc('label');
    self.map = dataMap;

    self.convert();

  def convert(self, stopIndex=-1):
    ''' Convert the labels to numerical representation '''

    for index, row in self.data.iterrows():
      row[self.labelIndex] = self.map[row[self.labelIndex]];

      if self.must_stop(stopIndex, index):
        break;

  def must_stop(self, stopIndex, index):
    ''' Is it time to break the loop? '''
    return stopIndex > -1 and index >= stopIndex;

  def unconvert(self, stopIndex=-1):
    ''' Reversed engineering of convert method for pretty print'''

    for index, row in self.data.iterrows():
      for key, value in self.map.items():
        if value == row[self.labelIndex]:
          row[self.labelIndex] = key;
          break;

      if self.must_stop(stopIndex, index):
        break;

  def __str__(self):
    ''' Usefull representation for print the dataset '''

    self.unconvert(5);
    output = self.data.head(5).to_string();
    self.convert(5);
    
    return output;
