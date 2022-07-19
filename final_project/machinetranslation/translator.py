"""
Python file to translate text using IBM Watson Language Translator

"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#function to translate english to french
def english_to_french(english_text):
    #write the code here
    """
    First we verified if the input value is null
    """
    if english_text is not None:
        french_text = language_translator.translate(
            text = english_text,
            model_id='en-fr').get_result()
        print(json.dumps(french_text, indent=4, ensure_ascii=False))
        return french_text['translations'][0]['translation']
    return None
#function to translate french to englsh
def french_to_english(french_text):
    #write the code here
    """
    First we verified if the input value is null
    """
    if french_text is not None:
        english_text = language_translator.translate(
            text = french_text,
            model_id='fr-en').get_result()
        print(json.dumps(english_text, indent=4, ensure_ascii=False))
        return english_text['translations'][0]['translation']
    return None
    