import re;
from sklearn.feature_extraction.text import CountVectorizer;
from collections import Counter;
import pandas as pd;

documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?'];

for document in documents:
  tokens = [];
  for word in re.split(r'\s+', re.sub(r'[^a-z|\s]', '', document.lower())):
    tokens.append(word);
  print(Counter(tokens));

count_vector = CountVectorizer(token_pattern='(?u)\\b\\w\\w+\\b');
count_vector.fit(documents);
print(count_vector.get_feature_names());

doc_array = count_vector.transform(documents).toarray();
print(doc_array);

frequency_matrix = pd.DataFrame(data=doc_array, columns=count_vector.get_feature_names());
print(frequency_matrix);