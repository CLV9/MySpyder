import os
import re
import app_config

with open(app_config.data_path, 'r+') as input_stream:
    input_stream.truncate(0)

os.system("scrapy crawl gazeta -o output.json")

with open(app_config.data_path, 'r+') as input_stream:
    text = input_stream.read()
    # remove bad ws symbols
    while '  ' in text:
        text = text.replace('  ', ' ')
    # remove html tags
    text = re.sub('<[^<]+?>', '', text)
    input_stream.truncate(0)

with open(app_config.data_path, 'w') as output_stream:
    output_stream.write(text)
