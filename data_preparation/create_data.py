from xeger import Xeger 
import json
import random
import time

from word_list import nouns

input_text_list=["SC-Aufwand","reserve","Usrache","Schadentag","Schadennummer","Gesamtschadenaufwand","Versicherungsschutz"]
Usrache =["Sachschaden","Brand u. Explpsion","Personenschaden","VK-Tatbestand,sonstige","Glasbruch"]
Versicherungsschutz = ["KH","Kasko"]
x = Xeger(limit=10)
data_json ={}
data_json["version"]="v2.0"
data_json["data"]=[]
data ={}
data["title"] =x.xeger("([a-z]+)")
data["paragraphs"]=[]



for i in range(2):
    random.shuffle(input_text_list)
    paragraphs ={}
    paragraphs["qas"]=[]
    context=""
    for input in input_text_list:
        qas={}
        if(input =="Usrache"):
            value = random.choice(Usrache)
            context += input+": "+ value+ " "
        elif(input == "Versicherungsschutz"):
            value = random.choice(Versicherungsschutz)
            context += input+": "+ value+ " "
        elif(input == "Schadentag"):
            value = str(random.randint(1,28))+"/"+str(random.randint(1,12))+"/"+str(random.randint(1960,2020))
            context += input+": "+ value+ " "
        elif(input =="Schadennummer"):
            value = str(random.randint(1000000000000,9999999999999))
            context += input+": "+ value+ " "            
        else:
            value = x.xeger("([0-9]+)")
            context += input+": "+ value +" "
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
        # qas["answers"].append(answers)
        # qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)
    # print(context)




    paragraphs["context"]= context
    data["paragraphs"].append(paragraphs)

print("First loop")
for i in range(100):
    # print(i)
    paragraphs ={}
    paragraphs["qas"]=[]
    context=""
    for j in range(6):
        qas={}
        start = time.time()
        # input = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)
        input = random.choice(nouns)
        # print(time.time()-start)
        if (input == None):
            continue
        if(j<3):
            value = x.xeger("([0-9]+)")
            # print(value)
            # print(input)
            context += input+": "+ value +" "
        else:
            # value = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)
            value = random.choice(nouns)
            if(value == None):
                value = x.xeger("([a-z]+)")
            context += input+": "+ value +" "
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
        # qas["answers"].append(answers)
        # qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)
    # print(context)




    paragraphs["context"]= context
    data["paragraphs"].append(paragraphs)




data_json["data"].append(data)
with open('data_test2.json', 'w') as outfile:
    json.dump(data_json, outfile)