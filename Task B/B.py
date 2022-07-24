n = int(input())
vacancies = {}

for i in range(n):
    name_of_vacancy, maximum_number_of_places_per_vacancy = input().split(',')
    vacancies[name_of_vacancy] = {}
    vacancies[name_of_vacancy]['maximum_number_of_places_per_vacancy'] = int(maximum_number_of_places_per_vacancy)
    vacancies[name_of_vacancy]['candidates'] = []

total_candidates = int(input())
for i in range(total_candidates):
    candidate_id, name_of_vacancy, solved_task, fine = input().split(',')

    vacancies[name_of_vacancy]['candidates'].append(
        {'total_solved_tasks': int(solved_task), 'fine': int(fine), 'id': candidate_id})

answer = []
for name_of_vacancy in vacancies:
    vacancies[name_of_vacancy]['candidates'].sort(
        key=lambda candidate: (-candidate['total_solved_tasks'], candidate['fine']))

    vacancies[name_of_vacancy]['candidates'] = vacancies[name_of_vacancy]['candidates'][
                                            :vacancies[name_of_vacancy]['maximum_number_of_places_per_vacancy']]
    answer.extend(vacancies[name_of_vacancy]['candidates'])

answer.sort(key=lambda candidate: candidate['id'])
for candidate in answer:
    print(candidate['id'])
