def is_palindrome(s: str) -> bool:
    answer = []

    for x in s:
        if x.isalnum():
            answer.append(x.lower())
    return answer == answer[::-1]

