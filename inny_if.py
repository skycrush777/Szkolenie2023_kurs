x=[1,2,3]
match x:
    case[]:
        print("pusta lista")
    case[1]:
        print("lista z jednym elementem",x)
    case[1,2]:
        print("lista z dwoma elementami",x)
    case[1,2,3]:
        print("lista z trzema elementami",x)
    case _:
        print("inny przypadek...")
        # lista z podłogą lista difoldowa, czyli taki inny "else"