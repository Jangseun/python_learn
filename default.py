import os

전직 = "no"


class 모험가:
    def __init__(self,sp,st,na):
        self.스피드 = sp
        self.힘 = st
        self.닉네임 = na

    sp = 10
    st = 10
    
    def 걷는다(self):
        print(f"{self.스피드}로 걷는다")

    def 싸운다(self):
        print(f"{self.힘}으로 팬다")


class 법사(모험가):
    def 파이어볼(self):
        print("가랏 파이어볼!!!!!!")
        print(f"{self.힘} DAMAGE!")

class 힐러(모험가):
    def 물리(self):
        print("에잇 십자가로 때리기!!!")
        print(f"{self.힘} DAMAGE!")

class 용사(모험가):
    def 기본배기(self):
        print("휙-")
        print(f"{self.힘} DAMAGE!")

class 테이머(모험가):
    def 브레스(self):
        print("가자 용용아!")
        print(f"{self.힘} DAMAGE!")


# B = 법사(sp=10, st=300, na="seoul")
# B.파이어볼()

# C = 법사( 100, 1000,"타락법사")
# C.파이어볼()
# A = 모험가(100,100,"jeju")
# A.스피드 = 4000
# A.걷는다()
# A.힘 = 200
# A.싸운다()

print("상대방이 결투를 신청했따! 이대로만 당할 수는 없지!!")
print("일단 캐릭터를 키워보자!!")
os.system('cls')



input("상대방이 공격을 해왔다! 이대로만 당할 수는 없지!!")

while True:
    if 전직 == "no":
        print("전직을 해보자!")
        print("=======================================")
        print("1.")
        print("=======================================")
