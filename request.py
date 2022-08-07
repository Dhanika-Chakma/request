import json
import requests


link1 = requests.get("http://saral.navgurukul.org/api/courses")
file = link1.json()
with open("dhanika.json","w") as c:
    json.dump(file,c,indent=4)

# print(file)

n = 0
id = []
for i in file["availableCourses"]:
    print(n, i["name"],":", i["id"])
    id.append(i["id"])
    n += 1
    # print(id)

user = int(input("enter your serial number:"))
i = 0
link = requests.get("http://saral.navgurukul.org/api/courses/"+id[user]+"/exercises")
file1 = link.json()
list = []
for i in file1["data"]:
    print(i,i["slug"])
    list.append(i["slug"])
    i += 1

user2 = int(input("enter the slug number:"))

link3 = requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug=" +g[user2])
file2 = link3.json()
print(file2)