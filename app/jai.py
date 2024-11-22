body_string = """
{
    "_type": "export",
    "__export_format": 4,
    "__export_date": "2024-11-22T15:52:03.019Z",
    "__export_source": "insomnia.desktop.app:v2023.5.8",
    "resources": [
        {
            "_id": "req_38c2040e0731415cbd78f37a562eb4fe",
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
            "isPrivate": false,
            "settingStoreCookies": true,
            "settingSendCookies": true,
            "settingDisableRenderRequestBody": false,
            "settingEncodeUrl": true,
            "settingRebuildPath": true,
            "settingFollowRedirects": "global",
            "_type": "request"
        },
        {
            "_id": "wrk_ed31ef85796444faafcdc83f75440355",
            "parentId": null,
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
            "dataPropertyOrder": null,
            "color": null,
            "isPrivate": false,
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
"""

print(body_string)
