import requests

import google.auth.transport.requests
import google.oauth2.id_token

def authorized_get_request(target_url, params=None):
    '''
    Description
        Cloud Functions(HTTPトリガー)に対して、起動元の認証を実装
    Args
        target_url:Cloud FunctionのトリガーURL
        params:HTTP(GET)のパラメータ
    '''
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, target_url)
    headers = {
        "Authorization": f"Bearer {id_token}"
    }
    
    response = requests.get(target_url,headers=headers, params=params)

    return response


if __name__ == "__main__":
    target_url ="Write Here Cloud Function Trigger URL"
    result = authorized_get_request(
        target_url = target_url,
        params = {
            "message":"sample message"
        }
    )
    print(result.text)