from numpy import average

# аналізує файл по шляху і повертає кортеж загальну та середню суму заробітної плати всіх розробників з файлу
def total_salary(path):
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
        if len(list_substrings) <2: #пуста стрічка попалася
            continue
        salary = list_substrings[1] #second element
        salary=salary.strip() #забираємо пробіли зліва і справа
        if salary == "": # пусту стрічку пропускаємо
            continue
        
        try:
            salary = int(salary) #розраховуємо, що другий елемент буде приводитися до числа
        except Exception as e:
            print(f"Exception: {e}")
            salary = 0
            
        outlist.append(salary)
    
    total1=sum(outlist)
    average1=average(outlist)
    return (total1,average1)   

path=r".\salaries.txt"
total1, average1 = total_salary(path)
print(f"Загальна сума заробітної плати: {total1}, Середня заробітна плата: {average1}")