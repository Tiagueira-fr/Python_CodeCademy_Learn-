# Gradebook Project
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# 1, 2  

subjects = ["physics" , "calculus" , "poetry" , "history"]
grade = [98 , 97 , 85 , 88]

# 3, 4
gradebook = [
  ["physics" , 98 ] , 
  ["calculus" , 97 ] ,
  ["poetry" , 85 ] , 
  ["history" , 88 ]
]
print(gradebook)

# 5
gradebook.append(["computer science" , 100])
print(gradebook)
# 6
gradebook.append(["visual arts", 93])
print(gradebook)

# 7
gradebook[-1][-1] = 98
print(gradebook)

# 8
gradebook[2].remove(85)
print(gradebook)

# 9 
gradebook[2].append("Pass")
print(gradebook)

# 10
full_gradebook = last_semester_gradebook + gradebook
print('')
print(full_gradebook)