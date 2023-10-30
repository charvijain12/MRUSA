# import required dependencies
import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# load Bag Of Words Vocabulary
if os.path.getsize("BoW_Vocab.txt") > 0:
    with open("BoW_Vocab.txt", 'rb') as vocab_file:
        unpickler = pickle.Unpickler(vocab_file)
        vocab = unpickler.load()
else:
    print("Empty")

# load the sentiment prediction model
if os.path.getsize("Sentiment_Prediction_Model.txt") > 0:
    with open("Sentiment_Prediction_Model.txt", 'rb') as model_binaryfie:
        unpickler = pickle.Unpickler(model_binaryfie)
        model = unpickler.load()
else:
    print("Empty")

vocab_size = len(vocab)
#print(vocab_size)

# create a CountVectorizer Object
vect= CountVectorizer(max_features=vocab_size)
vect.vocabulary_ = vocab

#print(vect.vocabulary_)
#print(len(vect.vocabulary_))
#input()

# get user input
text_input = input("Enter a text about how u feel: ")

# create BoW for the input text
BoW = vect.transform([text_input])
BoW_array = BoW.toarray()

# predict sentiment
print(model.predict(BoW_array))

