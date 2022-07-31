import json

# open the json file
with open("example.json") as json_file:
    data = json.load(json_file)
    print(f"Printing file: {json_file}")
    print(f"Type: ", type(data))
    # return JSON object as a dictionary
    with open('converted.txt', 'w') as converted_file:
        converted_file.write(json.dumps(data))


  

