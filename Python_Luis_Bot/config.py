#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    #PORT = 3978
    #APP_ID = os.environ.get("MicrosoftAppId", "")   app id ecddd8bb-afb2-4913-ba5a-0909e1a0bb6e
    #APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")bd8e8f6a22a446bf8bcba01b3a209d57
    #LUIS_APP_ID = os.environ.get("LuisAppId", "") https://westus.api.cognitive.microsoft.com
    #LUIS_API_KEY = os.environ.get("LuisAPIKey", "") testdispatcher key 799eb06a404b4bdfaa931e432a5cc77b
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com" test disp app id - 622acde6-7e02-4065-b97a-999d044b3b21
    #LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "") https://southcentralus.api.cognitive.microsoft.com/
    PORT = 3979
    APP_ID = ""
    APP_PASSWORD =""
    LUIS_APP_ID ="db1d775b-be3e-46b9-833e-7430284954c4"
    LUIS_API_KEY ="529ca13155bc408090417e60c52b1b6a"
    LUIS_API_HOST_NAME ="westus.api.cognitive.microsoft.com"
