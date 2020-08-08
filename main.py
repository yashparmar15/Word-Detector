import os

def check_word(filename,word_to_find):
    count = 0
    with open(filename , "r") as f:
        content = f.read()
        content = content.split(' ')
        for word in content:
            if word.lower() == word_to_find.lower():
                count += 1
        if count:
            print(f"Found {count} {word_to_find} in {filename}")
            return count
        else:
            print(f"{word_to_find} is not present in {filename}")
            return 0
        



if __name__ == "__main__":
    print("Please Enter a word which you want to find : ",end = "")
    word = input()
    all_files = os.listdir()
    total_file = 0
    total_word = 0
    for file in all_files:
        if file != 'main.py' and file != ".git":
            print(f"Checking {word} in {file}....")
            words_in_file = check_word(file,word)
            if words_in_file:
                total_word += words_in_file
                total_file += 1
    if total_word:
        print(f"*********************We found {total_word} {word} in {total_file} different files*********************")
    else:
        print(f"*********************Sorry there is no {word} present in any of the files*********************")
    print("Thank You!!!")
            
                

                

        
    