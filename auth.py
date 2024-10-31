# auth.py

import os
from dotenv import load_dotenv
import ivolatility as ivol

def initializeIvolAuthentication(credentials_file='credentials.env'):
    load_dotenv(credentials_file)

    ivolApiKey = os.getenv('ivolApiKey')

    if ivolApiKey:
        ivol.setLoginParams(apiKey=ivolApiKey)
