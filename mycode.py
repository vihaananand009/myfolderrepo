marks=int (input ("ENTER THE NUMBER THAT STUDENT OBTAINED :\n"))
if marks >=33 and marks < 45 :
    grade="D"
elif marks >=45 and marks <60:
        grade="C"
elif marks >=60 and marks <75:
      grade ="B"
elif marks >=75 and marks <100:
      grade ="A"
else:
      grade="F"
print( "YOU OBTAINED ='" +grade +"' GRADE")
        