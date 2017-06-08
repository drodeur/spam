from classifier import Classifier;
import pandas as pd;

c = Classifier(pd.read_table('SMSSpamCollection', names=['label', 'sms_message']), {'ham':0, 'spam':1});
print(c);