import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": { "text": text_to_analyze }}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) 
    
    formatted_resp = json.loads(response.text)

    emotion_scores = {}
    if response.status_code == 400:
        emotion_scores =  {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
        return emotion_scores

    emotion_scores = formatted_resp['emotionPredictions'][0]['emotion']
    dom_emotion = max(emotion_scores, key= emotion_scores.get)
    emotion_scores['dominant_emotion'] = dom_emotion

    return emotion_scores