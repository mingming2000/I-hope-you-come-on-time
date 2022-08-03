print('<일찍 와주길 바라>\n')
num = int(input('수업에 참여한 학생의 수를 입력하시오.(예: 5)'))
sum = 0
max_h = 0
max_m = 0
for i in range(0, num) :
  h = int(input('몇 시에 수업에 참여했는지 입력하시오.(예: 07)'))
  m = int(input('몇 분에 수업에 참여했는지 입력하시오.(예 56)'))
  sum += 60 * h + m

  if max_h < h :
    max_h = h
    max_m = m
  elif max_h == h :
    if max_m < m :
      max_m = m

sum //= num
mv_h = sum // 60 
mv_m = sum % 60

print("평균 출석 시간은 ", mv_h, "시 ", mv_m, "분 입니다.\n")
print("가장 늦은 학생은 ", max_h,"시 ",max_m,"분에 출석했습니다.\n다음 수업은 늦지 않길 바라요!")
