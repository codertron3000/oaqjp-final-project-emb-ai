import requests
import json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    result = {
        'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness'],
        'dominant_emotion': '',
    }
    def find_dominant_emotion(options):
        dominant = {'emotion': '', 'score': 0}
        for key, value in options:
            if value > dominant ['score']:
                dominant ['emotion'] = key
                dominant ['score'] = value
        result['dominant_emotion'] = dominant['emotion']
        return
    find_dominant_emotion(result)
    return result
