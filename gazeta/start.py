import re
import os

json_path = 'D:\MySpider\gazeta\output.json'

with open(json_path, 'r+') as input_stream:
    input_stream.truncate(0)

os.system("scrapy crawl gazeta -o output.json")

with open(json_path, 'r+') as input_stream:
    text = input_stream.read()
    # remove bad ws symbols
    while '  ' in text:
        text = text.replace('  ', ' ')
    # remove html tags
    text = re.sub('<[^<]+?>', '', text)
    input_stream.truncate(0)

with open(json_path, 'w') as output_stream:
    output_stream.write(text)
