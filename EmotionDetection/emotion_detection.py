import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    if formatted_response["code"] == 3:
        response_dict = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        return response_dict
    else:
        emotion = formatted_response["emotionPredictions"][0]["emotion"] 
        anger_score = emotion["anger"]
        disgust_score = emotion["disgust"]
        fear_score = emotion["fear"]
        joy_score = emotion["joy"]
        sadness_score = emotion["sadness"]
        emotion_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        dominant_emotion = emotion_list.index(max(emotion_list))
        emotion_dict = {
            0 : "anger",
            1 : "disgust",
            2 : "fear",
            3 : "joy",
            4 : "sadness"
        }
        response_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': emotion_dict[dominant_emotion]
        }
        return response_dict