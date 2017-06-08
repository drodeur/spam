import re;
from collections import Counter;

documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?'];

for document in documents:
  tokens = [];
  for word in re.split(r'\s+', re.sub(r'[^a-z|\s]', '', document.lower())):
    tokens.append(word);
  print(Counter(tokens));