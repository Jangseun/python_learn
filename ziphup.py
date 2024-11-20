# 집합 자료형(통칭 set자료형)
# s1 = set([1,2,3])
# s2 = {1,2,3} # 근데 아무리 생각해도 얘가 젤 편함
# print(f's2 : {type(s2)}')

s1 = set("Hello")
print(s1)

#error : 집합은 순서가 없음 so 인덱스 사용x
#  + 중복은 제거됨 -> 중복이 아니게 되
print(s1[0])


