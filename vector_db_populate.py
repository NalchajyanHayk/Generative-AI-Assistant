from API import get_website_text
from AI_Assistant import chat_with_gpt
import json

URL_LIST = ["http://www.accel.com/", "http://www.a16z.com/", "http://www.greylock.com/",
            "http://www.benchmark.com/", "http://www.sequoiacap.com/", "http://www.kpcb.com/",
            "http://www.kpcb.com/", "http://www.lsvp.com/", "http://www.matrixpartners.com/",
            "http://www.500.co/", "http://www.500.co/", "http://www.sparkcapital.com/",
            "http://www.insightpartners.com/"]

answer_list = []
VC_company_name = []
Contacts = []
Invested_industries = []
VC_investment_rounds = []

for i in range(len(URL_LIST)):
    text = get_website_text(URL_LIST[i])
    if type(text) != int:
        message = "please return the content of this paragraph in a python dictionary form. VC name, contacts, industries that they invest in, investment rounds that they participate/lead.:" + text
        print("message is: ", message)
        answer_from_gpt = chat_with_gpt(message)
        print("gpt answer is: ", answer_from_gpt)
        answer_list.append(answer_from_gpt)

data_dicts = [json.loads(json_string) for json_string in answer_list]

file_path = "data.json"

# Write the dictionaries to the JSON file
with open(file_path, "w") as json_file:
    json.dump(data_dicts, json_file, indent=4)


print("JSON file saved successfully.")