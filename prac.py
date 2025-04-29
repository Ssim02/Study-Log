# 조건을 활용한 리스트 내포
array = ["사과", "자두", "초콜릿", "바나나", "체리"]

output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)