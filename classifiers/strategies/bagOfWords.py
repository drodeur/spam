from sklearn.feature_extraction.text import CountVectorizer;
import pandas as pd;

class BagOfWords(object):
  def __init__(self, data):
    count_vector = CountVectorizer(token_pattern='(?u)\\b\\w\\w+\\b');
    matrix = count_vector.fit_transform(data);#.toarray();
    #frequency_matrix = pd.DataFrame(data=doc_array, columns=count_vector.get_feature_names());
    #print(matrix);