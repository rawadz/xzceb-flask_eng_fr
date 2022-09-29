import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()


apikey = os.environ['apikey']
url = os.environ['url']

def get_translator_instance():
    """Create translator instance"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)

    language_translator.set_service_url(url)
    return language_translator


def english_to_french(english_text):
    """Translate from English to French"""
    if len(english_text) < 1:
        return "Please enter a text!"
    language_translator = get_translator_instance()
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    return french_text

def french_to_english(french_text):
    """Translate from French to English"""
    if len(french_text) < 1:
        return "Veuillez entrer un texte!"
    language_translator = get_translator_instance()
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text
