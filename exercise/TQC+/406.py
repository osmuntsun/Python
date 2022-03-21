# TQC+ 程式語言Python 406 不定數迴圈-BMI計算
# 設計說明：
# 請撰寫一程式，以不定數迴圈的方式輸入身高與體重，計算出BMI之後再根據以下對照表，印出BMI及相對應的BMI代表意義（State）。
# 假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：
# BMI值	代表意義
# BMI < 18.5	under weight
# 18.5 <= BMI < 25	normal
# 25.0 <= BMI < 30	over weight
# 30 <= BMI	fat
# 提示：BMI=體重(kg)/身高2(m)，輸出浮點數到小數點後第二位。 不需考慮男性或女性標準。

while True:
    x=eval(input("輸入身高："))
    if x==-9999:
        break
    y=eval(input("輸入體重："))
    z=y/((x/100)**2)
    if z<18.5:
        print("BMI：%.2f\nState：under weight"%z)
    elif z>=18.5 and z<25:
        print("BMI：%.2f\nState：normal"%z)
    elif z>=25.0 and z<30:
        print("BMI：%.2f\nState：over weight"%z)
    elif z>=30:
        print("BMI：%.2f\nState：fat"%z)

# 輸入輸出：
# 輸入說明
# 兩個正數（身高cm、體重kg），直至-9999結束輸入
# 輸出說明
# 輸出BMI值
# BMI值代表意義
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# 176
# 80
# BMI: 25.83
# State: over weight
# 170
# 100
# BMI: 34.60
# State: fat
# -9999