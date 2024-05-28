Basic command with curl:

`curl -X POST
 -H "Authorization: Bearer xoxc-sometoken"
 -H 'cookie: d-s=1699388598; b=.e3e46a669301xxx; x=e3e46a669301fdba71c24428.xxxx; d=xoxd-2p1KUKA9369bmxxxx'
 https://slack.com/api/conversations.info\?channel\=SOMECHANID`

## Required cookies

These cookies and the Bearer token can be retrieved from a web request to the slack web app.
- b
- d
- d-s
- x

Tentative code to parse a request is in parse_curl_request.py

## Flow

- Check if we have cookies and token
    - If not, ask for them
- Check auth.test endpoint to see if auth is valid
- Either look up channel id if given a name and/or check if channel id is valid and reachable by the user
- Request conversation.history
- Look up user ids and replace IDs with name in messages
    - Possibly cache the names
- Output messages
- Use timestamp or last message ID to retrieve new messages, loop
