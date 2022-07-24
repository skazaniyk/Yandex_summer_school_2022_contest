reference_word = input()
word_to_check = input()

answer = []

count_letter = {}
for i in range(ord('A'), ord('Z') + 1):
    count_letter[chr(i)] = 0

for i in range(len(word_to_check)):
    if word_to_check[i] == reference_word[i]:
        answer.append('correct')
    else:
        answer.append('absent')
        count_letter[reference_word[i]] += 1

for i in range(len(word_to_check)):
    if answer[i] != 'correct':
        if count_letter[word_to_check[i]] > 0:
            answer[i] = 'present'
            count_letter[word_to_check[i]] -= 1

for i in range(len(answer)):
    print(answer[i])