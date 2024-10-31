# auth.py

import os
from dotenv import load_dotenv
import ivolatility as ivol

def initializeIvolAuthentication(credentials_file='credentials.env'):
    load_dotenv(credentials_file)

    ivolApiKey = os.getenv('ivolApiKey')
    ivolUserName = os.getenv('ivolUserName')
    ivolUserPassword = os.getenv('ivolUserPassword')

    if ivolApiKey:
        ivol.setLoginParams(apiKey=ivolApiKey)
    elif ivolUserName and ivolUserPassword:
        ivol.setLoginParams(username=ivolUserName, password=ivolUserPassword)
    else:
        raise ValueError("Authorization parameters are not specified.")
