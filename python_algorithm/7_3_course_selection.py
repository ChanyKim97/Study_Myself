def course_selection(course_list):
    sorted_list = sorted(course_list, key=lambda x : x[1])

    #첫번째 수업은 가장 빨리 끝나는 것
    final_course_list = [sorted_list[0]]

    for course in sorted_list:
        if course[0] > final_course_list[-1][1]:
            final_course_list.append(course)

    return final_course_list



# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
