from approaches import NER_using_RNN
from data import data_parser
from sklearn.model_selection import train_test_split

data_path = r"data/ner.csv"
test_size = 0.2
random_state = 42
print("Data parsing...")
df = data_parser.data_preparing(data_path)
df_train, df_test = train_test_split(df, test_size=test_size, random_state=random_state)
print("Train RNN model...")
modelRNN = NER_using_RNN.NER_RNN(df_train, df_test, train_epochs=5)



