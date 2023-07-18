```python
import requests
import os
import json

class DataCollector:
    def __init__(self):
        self.data = []

    def collect_text_data(self, url):
        response = requests.get(url)
        text_data = response.text
        self.data.append(text_data)

    def collect_image_data(self, url, filename):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as out_file:
                out_file.write(response.content)
            self.data.append(filename)

    def collect_video_data(self, url, filename):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as out_file:
                out_file.write(response.content)
            self.data.append(filename)

    def collect_data_from_user(self, user_input):
        self.data.append(user_input)

    def save_data(self, filename):
        with open(filename, 'w') as outfile:
            json.dump(self.data, outfile)

def collect_data():
    collector = DataCollector()
    # Add your data collection logic here
    # For example:
    # collector.collect_text_data('http://example.com')
    # collector.collect_image_data('http://example.com/image.jpg', 'image.jpg')
    # collector.collect_video_data('http://example.com/video.mp4', 'video.mp4')
    # collector.collect_data_from_user('User input data')
    collector.save_data('data.json')

if __name__ == "__main__":
    collect_data()
```