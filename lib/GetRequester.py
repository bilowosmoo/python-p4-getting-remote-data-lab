import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Return raw bytes for test comparison
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Convert bytes to Python data
        response_data = self.get_response_body()
        try:
            return json.loads(response_data)
        except json.JSONDecodeError:
            return None



