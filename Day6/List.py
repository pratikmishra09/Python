# # """ Today topic is List So we are going to practice the list"""

# # l = [1,3,5, "Pratik",True]
# # print(l)
# # print(l[0])
# # print(l[1])
# # print(l[2])
# # print(l[3])
# # print(l[4])
# # print(len(l))
# # print("From hear start negative index")

# # print(l[-3])  #negative
# # print(l[len(l)-3]) #positive 



# # c = list["abc"]
# # print(c)


""" List some important method"""
marks = [90,53,55,53,93,23,38]
marks.append(100)
print(marks)
marks.extend([111,222])
print(marks)
marks.append([333,444])
print(marks)
marks.insert(0,100)
print(marks)
marks.pop()
print(marks)
marks.pop(2)
print(marks)

print(marks.index(111))

print(marks.count(100))
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
mark = marks.copy()
print(mark)
