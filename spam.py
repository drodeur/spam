from classifiers.strategies.strategies import Strategies;
from classifiers.bayesianClassifier import BayesianClassifier;
import pandas as pd;

labelsMap = {'ham':0, 'spam':1};
fieldsMap = {'sms_message': Strategies.BAG_OF_WORDS};


classifier = BayesianClassifier(pd.read_table('SMSSpamCollection', names=['label', 'sms_message']), labelsMap, fieldsMap);
classifier.train();
classifier.test();