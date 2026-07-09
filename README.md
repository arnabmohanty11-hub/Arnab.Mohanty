c1=65
c2=20
c3=90
c4=75
c5=85

total=c1+c2+c3+c4+c5
average=total / 5

print("Total points    :", total )
print("Average per classroom   :", average )

stars_per_point=2
reward_stars=total*stars_per_point

print("Total stars   : ",reward_stars)

boxes= reward_stars // 25
leftover= reward_stars % 25

Last_week=300

print("Better than last week?   :", total > Last_week)
print("Same as last week?    :", total == Last_week)
print("At least as good?    :", total >= Last_week )

total += 30

print("After bonus points    :", total)

total -=15
print("After missed tasks:", total)

boxes= reward_stars // 25

print("Final boxes packed   :", boxes)
