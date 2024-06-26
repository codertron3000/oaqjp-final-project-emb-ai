'''Defines the routes for the EmotionDetection Server'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route('/')
def render_index_page():
    '''Renders the index.html template page'''
    return render_template('index.html')


@app.route('/emotionDetector')
def emot_detector():
    '''Renders the emotionDetector page, recieves input and displays response from the server'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"""for the given statement, the system response is 'anger': {response['anger']},
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']},
    'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
