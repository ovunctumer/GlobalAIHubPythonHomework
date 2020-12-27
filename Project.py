"""
ÖVÜNÇ TÜMER 
ovunc.tumer88862@gmail.com
"""
import numpy as np

def grades_function():
	courses_sum=0
	courses=np.zeros(5)
	t_course=np.array([	[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0]	])
	while (courses_sum <=2):
		print("Please enter '1' want to take the course or '0'")
		for i in range(0,5):
			print("course:",i+1)
			i-1
			courses[i] = int(input("do you wanna take this course:"))
			courses_sum += courses[i]
		print("courses_sum:",int(courses_sum))
		"""----------"""
		if courses_sum<=2:
			print("You cannot take course less than 3")
			break
		"""----------"""
		print("Enter the grades of the course you took")
		for i in range(0,5):
			if courses[i]==1:
				print("\ncourses:",i+1)
				i-1
				midterm=int(input("Midterm exam:"))
				final=int(input("Final:"))
				project=int(input("Project:"))
				average=0.3*midterm + 0.5*final + 0.2*project
				t_course[i]=[midterm,final,project,average]
		print("\n")
		for i in range(0,5):
			k=i+1
			if courses[i]==1:
				if t_course[i][3]>=90:
					print("course",k,": AA")
				elif t_course[i][3]>=70:
					print("course",k,": BB")
				elif t_course[i][3]>=50:
					print("course",k,": CC")
				elif t_course[i][3]>=30:
					print("course",k,": DD")
				else:
					print("course",k,": FF")
		print("\n")
		print(t_course)
		
flag =0
while (flag <= 2):
	name = input("Please enter your name: ")
	surname = input("Please enter your surname: ")
	if name == "ovunc":
		if surname == "tumer":
			print("Welcome")
			grades_function()
			break
	else:
		print("Please try again!\n")
		flag +=1
	if flag ==3:
		print("You cannot try more than 3 time")
print("program was canceled...\n")
