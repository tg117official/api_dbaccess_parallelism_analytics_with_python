
# 40% increment below 19,999 | 20% increment above 20,000
l1 = [15000, 45000, 36000, 50000, 18000]


for ele in l1 :
    if ele > 19999:
        print(f"For {ele} 20% increment : {ele*1.20}")
    else :
        print(f"For {ele} 40% increment : {ele*1.40}")

index = 0
while index < len(l1) :
    if l1[index] > 19999:
         print(f"For {l1[index]} 20% increment : {l1[index]*1.20}")
    else :
         print(f"For {l1[index]} 40% increment : {l1[index]*1.40}")
    index = index + 1
