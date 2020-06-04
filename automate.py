import shutil
import re

extract_path = 'assets/potential-contacts.txt'
write_path = 'assets/'

def extract_phone_number(extract_path, write_path):
  with open(extract_path, 'r') as f:
    contents= f.read()
  pattern1 = r"[(]?\d{3}\S\d{3}\S\d{4}" #includes brackets
  numbers = re.findall(pattern1,contents)
  numbers = list(set(numbers))
  numbers = [num.replace(".","-") for num in numbers ]
  numbers = [num.replace(")","-") for num in numbers ]
  numbers = [num.replace("(","") for num in numbers ]
  numbers.sort(reverse= False)
  print(numbers)

  with open(write_path+"phone.txt", 'w') as f:
    for num in numbers:
      f.write(num)
      f.write("\n")

def extract_email(extract_path, write_path):
  with open(extract_path, 'r') as f:
    contents= f.read()
  print(contents)




if __name__ == "__main__":
  extract_phone_number(extract_path, write_path)
  extract_email(extract_path, write_path)
