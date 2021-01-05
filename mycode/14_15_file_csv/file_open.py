# file open /read
with open('i_have_a_dream.txt','r') as my_file:
    contents = my_file.read()
    # 공백 기준으로 단어를 분리해서 리스트로 저장
    word_list = contents.split(" ")
    # 한 줄 씩 분리해서 리스트로 저장
    line_list = contents.split("\n")

print(f"Total Number of Characters {len(contents)}")
print(f'Total Number of Words {len(word_list)}')
print(f'Total Number of Lines {len(line_list)}')