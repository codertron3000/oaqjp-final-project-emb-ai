import requests
import json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 400:
        result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        return result
    formatted_response = json.loads(response.text)
    result = {
        'anger': float(formatted_response['emotionPredictions'][0]['emotion']['anger']),
        'disgust': float(formatted_response['emotionPredictions'][0]['emotion']['disgust']),
        'fear': float(formatted_response['emotionPredictions'][0]['emotion']['fear']),
        'joy': float(formatted_response['emotionPredictions'][0]['emotion']['joy']),
        'sadness': float(formatted_response['emotionPredictions'][0]['emotion']['sadness']),
    }
    def find_dominant_emotion(options):
        dominant = {'emotion': '', 'score': 0.0}
        print(dominant['score'])
        for key, value in options.items():
            if value > dominant['score']:
                dominant ['emotion'] = key
                dominant ['score'] = value
        result['dominant_emotion'] = dominant['emotion']
        return
    find_dominant_emotion(result)
    return result
