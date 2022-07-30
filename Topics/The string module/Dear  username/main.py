import string

a = "Dear $name! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $name!"
print(string.Template(a).substitute(name=input()))
