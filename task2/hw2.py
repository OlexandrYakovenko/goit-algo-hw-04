# аналізує файл по шляху і повертає список словників з інформацією про кожного кота з файлу
def get_cats_info(path):
    outlist=[]
    lines=""
    try:
        with open(path,"r",encoding="utf-8") as file:
            lines=file.read()
    except Exception as e:
        print(f"Exception: {e}")
    
    print(lines)
    
    for line in lines.split("\n"): #розділяємо по символу нової стрічки
        list_substrings=line.split(",") #розділяємо по комі
        if len(list_substrings) <3: #пуста чи нестандартна стрічка попалася
            continue
        id = list_substrings[0] #id
        id=id.strip() #забираємо пробіли зліва і справа
        if id == "": # пусту стрічку пропускаємо
            continue
        
        name=list_substrings[1] 
        name=name.strip()
        if name == "": # пусту стрічку пропускаємо
            continue
        
        age=list_substrings[2] 
        age=age.strip()
        age=int(age)
        if age == 0: # нульове значення  пропускаємо
            continue
            
        outlist.append({"id":id,"name":name,"age":age})
    
    return outlist  

path=r".\cats.txt"
outlist = get_cats_info(path)
print(outlist)