import random


dodosuko_list = ["ドド", "スコ"]
count = 0
expected_outputs = "0111" * 3
output_i = -1
while count < len(expected_outputs):
    if output_i == -1:
        output_i = random.randint(0, 1)
        print(dodosuko_list[output_i], end="")

    if str(output_i) == expected_outputs[count]:
        output_i = -1
        count += 1
    else:
        output_i = -1 if output_i == 1 else output_i
        count = 0

print("ラブ注入♡")
