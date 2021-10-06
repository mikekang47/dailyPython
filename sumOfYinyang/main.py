def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
# zip함수는 인자를 튜플로 변환시킨다.
# 변환시킨 튜플에 한해서 sign이 양수인 경우는 넘어가고, 음수인 경우는 absolutes에 -를 붙여서 리턴한 후
# sum함수를 통해서 그 합을 구한다.
