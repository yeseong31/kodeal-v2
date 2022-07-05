import json
import ssl
import urllib

from config.settings.my_settings import CLIENT_ID, CLIENT_SECRET


def papago(text):
    """
    Papago API
    """
    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)

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