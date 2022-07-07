import json
import ssl
import urllib

from config.settings.base import CLIENT_ID, CLIENT_SECRET


def papago(text):
    """
    Papago API
    """
    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", get_papago_client_id())
    request.add_header("X-Naver-Client-Secret", get_papago_client_secret())

    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, data=data.encode("utf-8"), context=context)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        # Papago API의 반환값 중에서 "translatedText" 값만 추출
        json_object = json.loads(response_body.decode('utf-8'))
        return json_object['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)
        return 'ERROR'


def get_papago_client_id():
    """Papago CLIENT ID KEY 조회 및 확인"""
    client_id = CLIENT_ID
    if client_id is None:
        from config.settings.local import CLIENT_ID as CLIENT_ID_LOCAL
        client_id = CLIENT_ID_LOCAL
    return client_id


def get_papago_client_secret():
    """Papago CLIENT SECRET KEY 조회 및 확인"""
    client_secret = CLIENT_SECRET
    if client_secret is None:
        from config.settings.local import CLIENT_SECRET as CLIENT_SECRET_LOCAL
        client_secret = CLIENT_SECRET_LOCAL
    return client_secret
