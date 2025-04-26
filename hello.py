character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    value = character[key]
    if type(value) is str: # 문자열인지 확인
        print(key , ":", value)
    elif type(value) is list: # 리스트인지 확인
        for listKey in value:
            print(key, ":", listKey)
    elif type(value) is dict: # 딕셔너리인지 확인
        for dictKey in value:
            print(dictKey, ":", value[dictKey]) 
    else :
        print(key, ":", value)

    None