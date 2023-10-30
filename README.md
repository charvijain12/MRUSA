# MRUSA - Sentiment Driven Music Recommender

This deep learning project consists of two main parts: Sentiment Analysis and Recommendation System. The Sentiment Analysis part involves creating a sentiment analysis model using Kaggle datasets, and the Recommendation System is built using the Spotify Web API.

## 1. Sentiment Analysis

### Data Sources
- Two Kaggle datasets are used for sentiment analysis:
  - [Emotion Dataset 1](https://www.kaggle.com/datasets/parulpandey/emotion-dataset?select=test.csv)
  - [Emotion Dataset 2](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text/data)

### Steps to Run the Sentiment Analysis Model
1. You will need three files in the same location:
   - BoW Vocab.txt
   - Sentiment Prediction Model.txt
   - Model Application.py

2. Run the `Model Application.py` file and provide user input.

### Output
The output of the sentiment analysis model will be numeric digits that map to the emotion experienced. Here is the emotion mapping:
- Sadness(0): Sadness, Boredom, Surprise
- Joy(1): Joy, Enthusiasm, Happiness, Fun, Neutral
- Love(2): Love
- Anger(3): Hate, Anger, Empty, Relief
- Fear(4): Fear, Worry

*Note: The preprocessing tasks can be further improved.*

## 2. Recommendation System

The recommendation system is built using the Spotify Web API with OAuth 2.0 client credentials flow.

### Steps to Run the CLI App
1. Install the required dependencies:
   ```bash
   pip install python-dotenv
   pip install requests
   ```

2. Create a `.env` file in the './Music Recommendation System' directory. In this file, add the following code:
   ```plaintext
   CLIENT_ID = "<your_client_id>"
   CLIENT_SECRET = "<your_client_secret>"
   ```

3. Open `CLI Application.py` and run the application.

This project combines sentiment analysis to understand the user's emotional state and a recommendation system to suggest music based on those emotions. It can be further enhanced and customized to provide a personalized music experience for users.

## License
This project is licensed under the `MIT License` - see the LICENSE file for details.









