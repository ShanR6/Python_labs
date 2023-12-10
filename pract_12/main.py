import requests
import json
import zipfile


def send_request(method, url, data=None):
    response = None
    if method == "OPTION":
        response = requests.options(url)
    elif method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

    with open("result.txt", "a", encoding="utf-8") as file:
        file.write(f"Server response code: {response.status_code}\n")

        for header in response.headers:
            file.write(f"{header}: {response.headers[header]}\n")

        file.write("Response body:\n")
        file.write(response.text + "\n")

        if method == "GET" or method == "POST":
            request_body = response.request.body
            file.write("Request text:\n")
            file.write(f"{request_body}\n")
    return response


my_url = "https://httpbin.org"

option_response = send_request("OPTION", my_url)
get_response = send_request("GET", my_url)
post_response = send_request("POST", my_url, data={"key": "value"})

with zipfile.ZipFile("result.zip", "w") as zip_file:
    zip_file.write("main.py")
    zip_file.write("result.txt")
