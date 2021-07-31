#optional parameter는 마지막에 쓰럿
def myself(name, age, nation ="korea"):
    print("내이름은 {}".format(name))
    print("나이는 {}".format(age))
    print("국적은 {}".format(nation))


myself("김찬휘", 25)
myself("Emma", 30, "USA")