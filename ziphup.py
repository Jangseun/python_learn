# 집합 자료형(통칭 set자료형)
# s1 = set([1,2,3])
# s2 = {1,2,3} # 근데 아무리 생각해도 얘가 젤 편함
# print(f's2 : {type(s2)}')

# s1 = set("Hello")
# print(s1)

#error : 집합은 순서가 없음 so 인덱스 사용x
#  + 중복은 제거됨 -> 중복이 아니게 되
# print(s1[0])

a = {1,2,3}
b = {1,2,4}

# a&b : 애가 교집합
# a.intersection(b)  : 얘도 교집합
# a|b : 얘가 합집합 이려나 -> 정답이었고
# a.union(b) : 음ㅋㅋ 누가 봐도 합집합
# a-b : 얘가 차집합
# a.difference(b) : 얘도 차집합

# a.add() : 값 추가
# a.update([7,8]) : 값 여러개 추가
# a.remove() : 값 삭제


