import matplotlib.pyplot as plt
ages=[12,15,13,16,15,14,13,16,15,14]

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(ages,bins=5,color='skyblue',edgecolor='black')
plt.title('age distribution')
plt.xlabel('age')
plt.ylabel("number of students")

subjects=['Math','science','english','history']
students=[4,3,2,1]

plt.subplot(1,2,2)
plt.pie(students,labels=subjects,autopct='%1.1f%%',colors=['gold','lightgreen','skyblue','lightcoral'])
plt.title("favorite subjects")

plt.tight_layout()
plt.show()