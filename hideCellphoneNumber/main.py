def solution(phone_number):
    answer = ''
    answer += (len(phone_number)-4)*'*'
    for i in phone_number[-4:]:
        answer += i
    return answer