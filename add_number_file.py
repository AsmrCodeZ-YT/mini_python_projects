import os 

items = os.listdir(".")
print(len(items))

def rename_dir(old_name , new_name):
    os.rename(old_name, new_name)

num = 0
list_dirs = []

type_mission = int(input("Prees ur Mission : "))

for i,item in enumerate(items):
    if os.path.isdir(item):

        # print(i,item)
        
        if type_mission == 1:
            rename_dir(item , f"{num:02}__{item}")
            num += 1
        
        elif type_mission == 2:
            pre_name = item.split("__")[-1]   
            rename_dir(item , f"{num:02}__{pre_name}") 
            num += 1
            