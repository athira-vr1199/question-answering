from xeger import Xeger 
import json
import random
import time

from  word_list import nouns
value = ""
value1=""
# input_texts=["Claims Paid","Claims Outstanding","Claims Paid","Claims Outstanding"]
# input_texts=["Claims Paid","Claims Outstanding"]
# input_text_list=["AD","FT","TP"]
# input_text_list1=["reserves total"]
# input_text_list2=["total reserves"]
x = Xeger(limit=10)
y = Xeger(limit=4)
data_json ={}
data_json["version"]="v2.0"
data_json["data"]=[]
data ={}
data["title"] =x.xeger("([a-z]+)")
data["paragraphs"]=[]



for i in range(6000):
    # random.shuffle(input_text_list)
    paragraphs ={}
    paragraphs["qas"]=[]
    context =""
    input_text_list =[]
    input_text1 = random.choice(nouns)
    random_value = random.choice([0,1,2])
    for k in range(3):        
        # print(k,random_value)
        input_random = y.xeger("([A-Z]+)")
        if k == random_value and len(input_random)>1:
            length = int(abs(len(input_random)/2))
            # print(length,input_random) 
            if i < 1500:         
                input_random = input_random[:length] + "&" + input_random[length:]
            elif i >= 1500 and i<3000:         
                input_random = input_random[:length] + " and " + input_random[length:]
            elif i >= 3000 and i< 4500 :         
                input_random = input_random[:length] + "." + input_random[length:]+"."
            elif i >= 3000 and i< 4500 :         
                input_random = input_random[:length] + "+" + input_random[length:]
            else:
                input_random = input_random[:length] + "/" + input_random[length:]
            input_text_list.append(input_random)
        else:
            input_text_list.append(input_random)
    # print(input_text_list)
    for j in range(2):
        # input_text1 = random.choice(nouns)
        input_text2 = random.choice(nouns)
        # context+= input_text1+" "  
        context+= input_text1+" " +input_text2+" "      
        for input in input_text_list:
            qas={}
            # input = y.xeger("([A-Z]+)")
            value = x.xeger("([0-9]+)")
            context += input+" : "+value+" "
            # context += input+" : "+value+" ! "
            # qas["question"]=input_text1+" "+ input+"?"
            qas["question"]=input_text1+" "+input_text2+" "+ input+"?"
            qas["id"]=x.xeger("([0-9][a-z]+)")
            answers ={}
            answers["text"]=value
            context_length = len(context)
            # print(value)
            value_length = len(value)
            answers["answer_start"] =  context_length - value_length 
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
with open('data/val_UK_2word_same_frst_word_30k_with_extra_symbols.json', 'w') as outfile:
    json.dump(data_json, outfile)