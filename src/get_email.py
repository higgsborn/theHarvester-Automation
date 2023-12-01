import json
import os
import re

def get_json_files(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    return json_files

folder_path = '../data/results-test'

json_files = get_json_files(folder_path)
#print(json_files)

def extract_domain(host):
    match = re.search(r"@([\w.]+)", email)
    if match:
        return match.group(1)
    else:
        return None

def transform_json(input_json, domain):
    result_json = {}
    if "emails" in input_json:
        for email in input_json["emails"]:
            result_json.setdefault(domain, []).append(email)                                        
    else:
        result_json.setdefault(domain, []).append("")

    return result_json

email_list = []
def get_all_emails(input_json):
    if "emails" in input_json:
        for email in input_json["emails"]:
            # print(email)
            email_list.append(email)

## Specify the file path
#file_path = 'data.json'
#
## Open and read the JSON file

output_json_list = []
for file_path in json_files:
    with open(f'../data/results-test/{file_path}', 'r') as file:
        # Load JSON data froIm the file
        json_data = json.load(file)
        domain = file_path

        # Now json_data contains the content of the file as a Python dictionary
        email_json = transform_json(json_data, domain)
        output_json_list.append(email_json)

        email_test = get_all_emails(json_data)
        # print(email_json)

# Convert JSON strings to Python dictionaries
json_data = [json.loads(json.dumps(json_string, indent=2)) for json_string in output_json_list]

# Specify the file path
file_path = '../data/output.json'

# Write the list of dictionaries to a JSON file
with open(file_path, 'w') as file:
    json.dump(json_data, file, indent=2)

    print(f"JSON data has been written to {file_path}")

# write to a file
with open('../data/output.txt', 'w') as file:
    file.write('\n'.join(email for email in email_list))
