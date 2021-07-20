from xeger import Xeger 
import json
import random
import time

from word_list import nouns

input_text_list=["SC-Aufwand","total","reserve","Usrache","Schadentag","Schadennummer","Gesamtschadenaufwand","Versicherungsschutz"]
Usrache =["Sachschaden","Brand u. Explosion","Personenschaden","VK-Tatbestand,sonstige","Glasbruch"]
Versicherungsschutz = ["KH","Kasko"]
x = Xeger(limit=10)
data_json ={}
data_json["version"]="v2.0"
data_json["data"]=[]
data ={}
data["title"] =x.xeger("([a-z]+)")
data["paragraphs"]=[]

for i in range(1000):
    dict_new ={}
    context_list=[]
    for input in input_text_list:
        qas={}
        if(input =="Usrache"):
            value = random.choice(Usrache)
            dict_new[input] = value
            context_list.append(input)
            context_list.append(value)
            # context +=input+ " "+value+ " "
        elif(input == "Versicherungsschutz"):
            value = random.choice(Versicherungsschutz)
            dict_new[input] = value
            context_list.append(input)
            context_list.append(value)
        elif(input == "Schadentag"):
            value = str(random.randint(1,28))+"/"+str(random.randint(1,12))+"/"+str(random.randint(1960,2020))
            dict_new[input] = value
            context_list.append(input)
            context_list.append(value)
        elif(input =="Schadennummer"):
            value = str(random.randint(1000000000000,9999999999999))
            dict_new[input] = value 
            context_list.append(input)
            context_list.append(value)
        else:
            value = x.xeger("([0-9]+)")
            dict_new[input] = value
            context_list.append(input)
            context_list.append(value)

    for i in range(2):
        random_no = random.randint(0,len(context_list)-1)
        # print(random_no)
        if(random_no%2 == 1 and random_no+1 < len(context_list)) :
            # print(context_list[random_no])
            next_value = context_list[random_no+1]
            context_list[random_no+1] = context_list[random_no]
            context_list[random_no] = next_value
        elif(random_no%2 == 0 and random_no-1 >0 and random_no-1 < len(context_list)) :
            # print(context_list[random_no])
            next_value = context_list[random_no-1]
            context_list[random_no-1] = context_list[random_no]
            context_list[random_no] = next_value
    # print(context_list)
    context =""

    new_list =[]
    for i,input in enumerate(context_list):
        if(i+1 <len(context_list)) :
            if(input in input_text_list and context_list[i+1] not in input_text_list) :
                # print(input)  
                context +=input+" : "
                new_list.append(input)
                new_list.append(" : ")
            elif(input not in input_text_list and context_list[i+1] in input_text_list) :
                context +=input+" ! "
                new_list.append(input)
                new_list.append(" ! ")
            elif(input in input_text_list and context_list[i+1] in input_text_list) :
                context +=input+" "
                new_list.append(input)
                new_list.append(" ")
            elif(input not in input_text_list and context_list[i+1] not in input_text_list) :
                context +=input+" "
                new_list.append(input)
                new_list.append(" ")
        else:
            context +=input+" !"
            new_list.append(input)
            new_list.append(" ! ")


   


    paragraphs ={}
    paragraphs["qas"]=[]
    for input in input_text_list:
        qas={}        
        
        qas["question"]=input+"?"
        qas["id"]=x.xeger("([0-9][a-z]+)")
        answers ={}
        answr =dict_new[input]
        answers["text"]= answr
        answer_start = 0
        for word in new_list:
            if (word == answr):
                # answer_start +=1
                break
            else:
                answer_start += len(word)
        
        answers["answer_start"] = answer_start+1 
        qas["answers"]=[]
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)

    paragraphs["context"]= context
    data["paragraphs"].append(paragraphs)

#######################################################################################
for i in range(3000):
    dict_new ={}
    context_list=[]
    input_text_list =[]
    for i in range(10):
        qas={}
        input = random.choice(nouns)
        input_text_list.append(input)
            # print(time.time()-start)
        if (input == None):
            continue
        if(i<6):
            value = x.xeger("([0-9]+)")
            dict_new[input] = value
            context_list.append(input)
            context_list.append(value)
            # context += input+": "+ value +" "
        else:
            value = random.choice(nouns)
            if(value == None):
                value = x.xeger("([a-z]+)")
            dict_new[input] = value
            context_list.append(input)
            context_list.append(value)
        
    # print(context_list)
    for i in range(2):
        random_no = random.randint(0,len(context_list)-1)
        # print(random_no)
        if(random_no%2 == 1 and random_no+1 < len(context_list)) :
            # print(context_list[random_no])
            next_value = context_list[random_no+1]
            context_list[random_no+1] = context_list[random_no]
            context_list[random_no] = next_value
        elif(random_no%2 == 0 and random_no-1 >0 and random_no-1 < len(context_list)) :
            # print(context_list[random_no])
            next_value = context_list[random_no-1]
            context_list[random_no-1] = context_list[random_no]
            context_list[random_no] = next_value
    # print(context_list)
    context =""

    new_list =[]
    for i,input in enumerate(context_list):
        if(i+1 <len(context_list)) :
            if(input in input_text_list and context_list[i+1] not in input_text_list) :
                # print(input)  
                context +=input+" : "
                new_list.append(input)
                new_list.append(" : ")
            elif(input not in input_text_list and context_list[i+1] in input_text_list) :
                context +=input+" ! "
                new_list.append(input)
                new_list.append(" ! ")
            elif(input in input_text_list and context_list[i+1] in input_text_list) :
                context +=input+" "
                new_list.append(input)
                new_list.append(" ")
            elif(input not in input_text_list and context_list[i+1] not in input_text_list) :
                context +=input+" "
                new_list.append(input)
                new_list.append(" ")
        else:
            context +=input+" ! "
            new_list.append(input)
            new_list.append(" ! ")

    # print(new_list)
    # print(context)
    # for i in range(1):
    paragraphs ={}
    paragraphs["qas"]=[]
    for input in input_text_list:
        qas={}        
        
        qas["question"]=input+"?"
        qas["id"]=x.xeger("([0-9][a-z]+)")
        answers ={}
        answr =dict_new[input]
        answers["text"]= answr
        answer_start = 0
        for word in new_list:
            if (word == answr):
                # answer_start +=1
                break
            else:
                answer_start += len(word)
    
        answers["answer_start"] = answer_start+1 
        qas["answers"]=[]
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["answers"].append(answers)
        qas["is_impossible"]="false"
        paragraphs["qas"].append(qas)

    paragraphs["context"]= context
    data["paragraphs"].append(paragraphs)


data_json["data"].append(data)
with open('data3_val.json', 'w') as outfile:
    json.dump(data_json, outfile)
