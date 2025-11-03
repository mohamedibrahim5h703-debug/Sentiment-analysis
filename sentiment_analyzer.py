from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

# ⚠️ استبدل المفاتيح أدناه بالمفاتيح الحقيقية الخاصة بك من IBM Cloud
API_KEY = "<YOUR_API_KEY>"
SERVICE_URL = "<YOUR_SERVICE_URL>"

def analyze_sentiment(text):
    """
    تحليل المشاعر باستخدام IBM Watson NLP
    """
    authenticator = IAMAuthenticator(API_KEY)
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )
    nlu.set_service_url(SERVICE_URL)

    try:
        response = nlu.analyze(
            text=text,
            features=Features(sentiment=SentimentOptions())
        ).get_result()

        label = response["sentiment"]["document"]["label"]
        score = response["sentiment"]["document"]["score"]
        return {"label": label, "score": score}

    except Exception as e:
        return {"error": str(e)}
