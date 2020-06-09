import shutil
import re

extract_path = 'assets/potential-contacts.txt'
write_path = 'assets/'

def extract_phone_number(extract_path, write_path):
  with open(extract_path, 'r') as f:
    contents= f.read()
  # captures all that i need  (\.)([(]?\d{3}\S)?(\d{3}\S\d{4})([x]{0,1}\d{0,5})
  pattern1 = r"\.[(]?\d{3}\S\d{3}\S\d{4}[x]{0,1}\d{0,5}" #includes brackets
  numbers = re.findall(pattern1,contents)
  numbers = list(set(numbers))
  numbers = [num.replace(".","") for num in numbers ]
  numbers = [num.replace(")","") for num in numbers ]
  numbers = [num.replace("(","") for num in numbers ]
  numbers = [num.replace("-","") for num in numbers ]
  numbers.sort(reverse= False)
  print("these are the numbers from pattern 1", numbers)
  phone_numbers = []
  for num in numbers:
    str = ""
    for i,char in enumerate(num):
      if i ==2 or i==5:
        str+=char+"-"
      else:
        str+= char
    phone_numbers.append(str)
  print("new list", phone_numbers)

  with open(write_path+"phone.txt", 'w') as f:
    for num in phone_numbers:
      f.write(num)
      f.write("\n")

def extract_email(extract_path, write_path):
  with open(extract_path, 'r') as f:
    contents= f.read()
  pattern = r"[^\W][a-zA-Z0-9]{1,}@[\S\w\d]{1,}\.[a-z]{2,}"
  emails = re.findall(pattern,contents)
  print(len(emails))
  emails = list(set(emails))
  print(len(emails))
  emails.sort(reverse=False)
  print(emails)

  with open(write_path+"emails.txt", 'w') as f:
    for addr in emails:
      f.write(addr)
      f.write("\n")





if __name__ == "__main__":
  # extract_phone_number(extract_path, write_path)
  extract_email(extract_path, write_path)
