# import required dependencies
# make sure these are present in the main application as well
import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer

def Get_Sentiment():
    # load Bag Of Words Vocabulary
    BoW_Vocab_path = "./requirements/BoW_Vocab.txt"                         # change path if required

    if os.path.getsize(BoW_Vocab_path) > 0:
        with open(BoW_Vocab_path, 'rb') as vocab_file:
            unpickler = pickle.Unpickler(vocab_file)
            vocab = unpickler.load()
    else:
        print("Empty")
        return 11

    # load the sentiment prediction model
    Prediction_Model_path = "./requirements/Sentiment_Prediction_Model.txt"  # change path if required
    
    if os.path.getsize(Prediction_Model_path) > 0:
        with open(Prediction_Model_path, 'rb') as model_binaryfie:
            unpickler = pickle.Unpickler(model_binaryfie)
            model = unpickler.load()
    else:
        print("Empty")
        return 22

    vocab_size = len(vocab)
    #print(vocab_size)

    # create a CountVectorizer Object
    vect= CountVectorizer(max_features=vocab_size)
    vect.vocabulary_ = vocab

    # get user input
    text_input = input("Enter a text about how u feel: ")

    # create BoW for the input text
    BoW = vect.transform([text_input])
    BoW_array = BoW.toarray()

    # predict sentiment
    senti = model.predict(BoW_array)[0]

    return senti