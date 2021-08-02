def move_disk(disk_num, start_peg, end_peg):
    print("{}번 원판을 {}번 기둥에서 {}번 기둥으로 이동".format(disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    #base case
    if num_disks == 0:
        return None

    else:
        #6인 이유는 1,2,3 번기둥이 있을때 도착지 외의 공간을 찾기 위함
        other_peg = 6 - start_peg - end_peg
#가장 큰 거 제외하고 도착지 외 다른곳 옮기기
        hanoi(num_disks - 1 , start_peg, other_peg)
#가장 큰거 마지막으로 옮기기
        move_disk(num_disks, start_peg, end_peg)
#나머지를 마지막으로
        hanoi(num_disks - 1, other_peg, end_peg)



hanoi(3, 1, 3)