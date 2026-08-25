import google.genai as genai

# Print available client/API methods
client = genai.Client(api_key="test")
print("Client methods:", [x for x in dir(client) if not x.startswith('_')])
