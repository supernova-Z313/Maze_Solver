#!/usr/bin/python3
try:
    import requests
except ImportError:
    raise ImportError('install requests: \npip install requests')

TOKEN = "hgy214..." # your bot token
ID = -1001.  # your bot id


def send(message, token=TOKEN, chat_id=ID):
    url = f"https://api.telegram.org/bot{token}/SendMessage?chat_id={chat_id}&text=" + str(message)
    payload = {"UrlBox": url, "AgentList": "Mozilla Firefox", "VersionsList": "HTTP/1.1", "MethodList": "GET"}
    res = requests.post(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=payload).status_code
    if res == 200:
        return "ok"
    else:
        return "error:", res.status_code

if __name__ == "__main__":
    message = input("Enter a message: ")
    send(message)
