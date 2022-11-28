import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
#Commenting here
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

language_translator.set_disable_ssl_verification(True)

#Commenting here
def english_to_french(english_text):#Commenting here
    #write the code here
    if english_text=='':
        french_text = ''
    else:
        translation = language_translator.translate(text=english_text,
        model_id='en-fr').get_result()
        #print(translation['translations'][0]['translation'])
        french_text = translation['translations'][0]['translation']
    return french_text

#Commenting here
def french_to_english(french_text):#Commenting here
    #write the code here
    if french_text == '':
        english_text = ''
    else:
        translation = language_translator.translate(text=french_text,
        model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
    return english_text
