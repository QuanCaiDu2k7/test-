import requests

cookies = {
    'sb': 'a8d2YnSjeYFJiU3qY6egXovV',
    'wd': '1366x617',
    'datr': 'a8d2YjyilBh5e_x1bZxWhoQq',
    'locale': 'vi_VN',
    'c_user': '100070031963966',
    'xs': '16%3AWGJQ4afB4WoOEw%3A2%3A1652348011%3A-1%3A6299',
    'fr': '0aMPsOVI087swZRr5.AWUB9OacGvaSfu9PPm3Kb29W-DE.BifNRB.rw.AAA.0.0.BifOOr.AWVkv4o2bho',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    # Requests sorts cookies= alphabetically
    'cookie': 'sb=a8d2YnSjeYFJiU3qY6egXovV; wd=1366x617; datr=a8d2YjyilBh5e_x1bZxWhoQq; locale=vi_VN; c_user=100070031963966; xs=16%3AWGJQ4afB4WoOEw%3A2%3A1652348011%3A-1%3A6299; fr=0aMPsOVI087swZRr5.AWUB9OacGvaSfu9PPm3Kb29W-DE.BifNRB.rw.AAA.0.0.BifOOr.AWVkv4o2bho',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}

response = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token', cookies=cookies, headers=headers).url
print(response.split('#access_token=')[1].split('&data_access')[0])