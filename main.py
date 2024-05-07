from API import get_website_text
from AI_Assistant import chat_with_gpt
import json

if __name__ == "__main__":
    print("Here You are going to insert the URL")
    user_inputted_URL = input("Please insert the URL of the Venture company: ")
    print("The information is being preprocessed by the program")
    website_text = get_website_text(user_inputted_URL)

    if type(website_text) != int:
        message = "please return the content of this paragraph in a python dictionary form. VC name, contacts, industries that they invest in, investment rounds that they participate/lead.:" + website_text
        answer_from_gpt = chat_with_gpt(message)

        new_data = json.loads(answer_from_gpt)

        with open("data.json", "w") as json_file:
            json.dump(new_data, json_file, indent=4)
    else:
        print("Unfotunately, it is impossible to get information from this website.")

