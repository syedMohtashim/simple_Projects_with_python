# To search and replace 
file_name = 'project_1/file_1.txt'
def search_and_replace(file_path , search_char , new_char):
        with open(file_path , 'r') as f:
            content = f.read()
        if search_char in content.lower():
            print(search_char , ' will be replaced by ' , new_char)
            print()
            print(content.replace(search_char , new_char).format(name = 'Wikipedia'))
        else: print('Nothing detected') 

search_and_replace(file_name , 'by' , 'BYE')