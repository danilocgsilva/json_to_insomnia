from random import random
import math
import json

def generate_hexadecimal():
    string_to_return = ""
    charactersHexa = "0123456789abcdef"
    for i in range(1,32):
        string_to_return += charactersHexa[math.ceil(random() * 15)]
    return string_to_return

dictionary = {
    "_type": "export",
    "__export_format": 4,
    "__export_date": "2024-11-22T15:52:03.019Z",
    "__export_source": "insomnia.desktop.app:v2023.5.8",
    "resources": [
        {
            "_id": "req_a7f2d3e8b4c5a1d6e9f3b2c7d8a0e1f",
            "parentId": "wrk_ed31ef85796444faafcdc83f75440355",
            "modified": 1732290693730,
            "created": 1732290685432,
            "url": "http://localhost",
            "name": "New Request",
            "description": "",
            "method": "GET",
            "body": {},
            "parameters": [],
            "headers": [
                {
                    "name": "User-Agent",
                    "value": "insomnia/2023.5.8"
                }
            ],
            "authentication": {},
            "metaSortKey": -1732290685432,
            "isPrivate": False,
            "settingStoreCookies": True,
            "settingSendCookies": True,
            "settingDisableRenderRequestBody": False,
            "settingEncodeUrl": True,
            "settingRebuildPath": True,
            "settingFollowRedirects": "global",
            "_type": "request"
        },
        {
            "_id": "req_c8f1a4e7b2d6f3a9d0e5b3c7a8f2d1",
            "parentId": "wrk_ed31ef85796444faafcdc83f75440355",
            "modified": 1732290693730,
            "created": 1732290685432,
            "url": "http://localhost",
            "name": "New Request 2",
            "description": "",
            "method": "GET",
            "body": {},
            "parameters": [],
            "headers": [
                {
                    "name": "User-Agent",
                    "value": "insomnia/2023.5.8"
                }
            ],
            "authentication": {},
            "metaSortKey": -1732290685432,
            "isPrivate": False,
            "settingStoreCookies": True,
            "settingSendCookies": True,
            "settingDisableRenderRequestBody": False,
            "settingEncodeUrl": True,
            "settingRebuildPath": True,
            "settingFollowRedirects": "global",
            "_type": "request"
        },
        {
            "_id": "wrk_ed31ef85796444faafcdc83f75440355",
            "parentId": None,
            "modified": 1732290683084,
            "created": 1732290683084,
            "name": "Simple Model",
            "description": "",
            "scope": "collection",
            "_type": "workspace"
        },
        {
            "_id": "env_80d987381dd7abd77899d5c30acf298e03d3848d",
            "parentId": "wrk_ed31ef85796444faafcdc83f75440355",
            "modified": 1732290683086,
            "created": 1732290683086,
            "name": "Base Environment",
            "data": {},
            "dataPropertyOrder": None,
            "color": None,
            "isPrivate": False,
            "metaSortKey": 1732290683086,
            "_type": "environment"
        },
        {
            "_id": "jar_80d987381dd7abd77899d5c30acf298e03d3848d",
            "parentId": "wrk_ed31ef85796444faafcdc83f75440355",
            "modified": 1732290683089,
            "created": 1732290683089,
            "name": "Default Jar",
            "cookies": [],
            "_type": "cookie_jar"
        }
    ]
}

pre_result_string = json.dumps(dictionary, indent=4)
pre_result_string = pre_result_string.replace("true", "True")
pre_result_string = pre_result_string.replace("false", "False")


print(pre_result_string)