f = open("pelican.txt", "r")
content = f.read()
print(content)
print(type(f.read()))

# f_list = f.split(",")
# f.close()
# print(f_list)

content_list = content.split(",")

print(content_list)

print(len(content_list))

for i in content_list:
    print(i.strip())

f.close()