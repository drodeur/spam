from sklearn.feature_extraction.text import CountVectorizer;

class BagOfWords(object):
  def __init__(self, data, options):
    self.data = data;
    self.options = options;

    try:
      self.options['vector'];
    except KeyError:
      self.options['vector'] = count_vector = CountVectorizer(token_pattern='(?u)\\b\\w\\w+\\b');

  def compute(self):
    if self.options['fit'] == True:
      return self.options['vector'].fit_transform(self.data);

    return self.options['vector'].transform(self.data);