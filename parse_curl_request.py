# This is code to parse a curl request copied from Chrome
# When executed it takes the curl command pasted in and outputs the token and required headers
import json
import curlparser

print(
    "Enter/Paste your curl request from Chrome. Ctrl-D or Ctrl-Z ( windows ) to parse it."
)
contents = list()
while True:
    try:
        line = input()
    except EOFError:
        break
    # contents.append(line.strip())
    contents.append(line)

contents = "\n".join(contents)

result = curlparser.parse(contents)

print(result)

try:
    data = json.loads(result.data)
    token = data.get("token")
except json.decoder.JSONDecodeError:
    token = next(x for x in result.data.split("\\r\\n") if x.startswith("xoxc-"))

# print(type(result.data))
# token = result.data['token']
required_cookies = ("b", "d", "d-s", "lc", "x")
cookies = "; ".join(
    [
        x
        for x in result.header["cookie"].split("; ")
        if x.split("=")[0] in required_cookies
    ]
)

print(token)
print(cookies)
