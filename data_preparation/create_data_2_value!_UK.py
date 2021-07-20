from xeger import Xeger 
import json
import random
import time

# from  import nouns
value = ""
value1=""
# input_texts=["Claims Paid","Claims Outstanding","Claims Paid","Claims Outstanding"]
input_texts=["claims paid","claims outstanding"]
# input_text_list0=["AD","FT","TP"]
# input_text_list1=["ADFT&W/S","F+T","T.P."]
# input_text_list2=["AD","F&T","T and P"]



input_text_list0=["AB","HK","YW"]
input_text_list1=["TK","HQ","MK"]
input_text_list2=["AG","ZA","CH"]
# input_text_list1=["reserves total"]
# input_text_list2=["total reserves"]
x = Xeger(limit=10)
data_json ={}
data_json["version"]="v2.0"
data_json["data"]=[]
data ={}
data["title"] =x.xeger("([a-z]+)")
data["paragraphs"]=[]



for i in range(100):
    if (i<33):
        input_text_list = input_text_list0
    elif (i>=33 and i<66):
        input_text_list = input_text_list1
    elif(i>=66):
        input_text_list = input_text_list2
    # input_text_list = input_text_list0
    random.shuffle(input_text_list)
    paragraphs ={}
    paragraphs["qas"]=[]
    context =""
    for input_text in input_texts:
        context+= input_text+"  "
        for input in input_text_list:
            qas={}
            
            value = x.xeger("([0-9]+)")
            context += input+" : "+value+" "
            # context += input+" : "+value+" ! "
            
            qas["question"]=input_text+" "+ input+"?"
            qas["id"]=x.xeger("([0-9][a-z]+)")
            answers ={}
            answers["text"]=value
            context_length = len(context)
            # print(value)
            value_length = len(value)
            answers["answer_start"] = context_length - value_length  
            qas["answers"]=[]
            qas["answers"].append(answers)
            # qas["answers"].append(answers)
            # qas["answers"].append(answers)
            qas["is_impossible"]="false"
            paragraphs["qas"].append(qas)
        # print(context)
        context+= "! "

    paragraphs["context"]= context
    data["paragraphs"].append(paragraphs)




data_json["data"].append(data)
with open('data/test_UK_100_claims_lowercase_without_symbols_random.json', 'w') as outfile:
    json.dump(data_json, outfile)