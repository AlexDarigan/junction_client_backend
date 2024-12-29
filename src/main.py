from appwrite.client import Client

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('67717c4e003447c84281') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

functions = Functions(client)
print("Hello World")

return {"greeting": "hello"}
