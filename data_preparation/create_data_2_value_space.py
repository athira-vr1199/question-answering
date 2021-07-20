from xeger import Xeger 
import json
import random
import time

# from  import nouns
value = ""
value1=""
input_text_list=["reserves","total"]
input_text_list1=["reserves total"]
input_text_list2=["total reserves"]
# Usrache =["Sachschaden","Brand u. Explpsion","Personenschaden","VK-Tatbestand,sonstige","Glasbruch"]
# Versicherungsschutz = ["KH","Kasko"]
x = Xeger(limit=10)
data_json ={}
data_json["version"]="v2.0"
data_json["data"]=[]
data ={}
data["title"] =x.xeger("([a-z]+)")
data["paragraphs"]=[]



for i in range(100):
    random.shuffle(input_text_list)
    paragraphs ={}
    paragraphs["qas"]=[]
    context=""
    for input in input_text_list:
        qas={}
        
        value = x.xeger("([0-9]+)")
        context += input+" : "+value+" "
        
        qas["question"]=input+"?"
        qas["id"]=x.xeger("([0-9][a-z]+)")
        answers ={}
        answers["text"]=value
        context_length = len(context)
        # print(value)
        value_length = len(value)
        answers["answer_start"] = context_length - value_length
        qas["answers"]=[]
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)
    # print(context)


    paragraphs["context"]= context
    data["paragraphs"].append(paragraphs)

for i in range(50):
    # random.shuffle(input_text_list)
    paragraphs ={}
    paragraphs["qas"]=[]
    context=""
    for input in input_text_list2:
        qas={}
        
        value = x.xeger("([0-9]+)")
        value1 = x.xeger("([0-9]+)")
        context += input+" : "+value
        
        question1,question2 = input.split(" ")
        qas["question"]=question1+"?"
        qas["id"]=x.xeger("([0-9][a-z]+)")
        answers ={}
        answers["text"]=value
        context_length = len(context)
        # print(value)
        value_length = len(value)
        answers["answer_start"] = context_length - value_length + 1
        qas["answers"]=[]
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)

        qas={}
        qas["question"]=question2+"?"
        qas["id"]=x.xeger("([0-9][a-z]+)")
        answers ={}
        answers["text"]=value1
        context += " "+ value1+" "
        context_length = len(context)
        # print(value)
        value_length = len(value1)
        answers["answer_start"] = context_length - value_length
        qas["answers"]=[]
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)
    # print(context)

    

    paragraphs["context"]= context
    data["paragraphs"].append(paragraphs)
    
for i in range(50):
    # random.shuffle(input_text_list)
    paragraphs ={}
    paragraphs["qas"]=[]
    context=""
    for input in input_text_list1:
        qas={}
        
        value = x.xeger("([0-9]+)")
        value1 = x.xeger("([0-9]+)")
        context += input+" : "+value
        
        question1,question2 = input.split(" ")
        qas["question"]=question1+"?"
        qas["id"]=x.xeger("([0-9][a-z]+)")
        answers ={}
        answers["text"]=value
        context_length = len(context)
        # print(value)
        value_length = len(value)
        answers["answer_start"] = context_length - value_length + 1
        qas["answers"]=[]
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)

        qas={}
        qas["question"]=question2+"?"
        qas["id"]=x.xeger("([0-9][a-z]+)")
        answers ={}
        answers["text"]=value1
        context += " "+ value1+" "
        context_length = len(context)
        # print(value)
        value_length = len(value1)
        answers["answer_start"] = context_length - value_length
        qas["answers"]=[]
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)
    # print(context)

    

    paragraphs["context"]= context
    data["paragraphs"].append(paragraphs)

data_json["data"].append(data)
with open('val1000space.json', 'w') as outfile:
    json.dump(data_json, outfile)