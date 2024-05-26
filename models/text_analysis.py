from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from textblob import TextBlob
from flask_smorest import Blueprint
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

text_bp = Blueprint('text_bp', __name__ , description='Text analysis operations')

# Text analysis route
@text_bp.route('/analyze', methods=['POST'])
@jwt_required()
def analyze_text():
    data = request.json
    if 'text' not in data:
        return jsonify({"error": "Text is required"}), 400
    
    text = data['text']
    
   
    # Using TextBlob for analysis
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Counting the number of sentences
    sentences = blob.sentences
    num_sentences = len(sentences)
    
    # Calculating positive and negative scores
    positive_score = 0
    negative_score = 0
    for sentence in sentences:
        sentiment = TextBlob(str(sentence)).sentiment.polarity
        if sentiment > 0:
            positive_score += sentiment
        elif sentiment < 0:
            negative_score += sentiment
    
    # Using VADER for sentiment analysis
    vader_sentiment = sia.polarity_scores(text)
    
    response = {
        'text': text,
        'textblob': {
            'polarity': polarity,
            'subjectivity': subjectivity
        },
        'vader': vader_sentiment,
        'positive_score': positive_score,
        'negative_score': negative_score,
        'num_sentences': num_sentences
    }
    
    return jsonify(response), 200
    
  