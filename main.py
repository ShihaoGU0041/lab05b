from ctypes.wintypes import PWORD

print("Hello world")
print("Hello world")
print("Hello world")

name="hello world"
print(type("hello world"))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())



response = input("Continue? (Y/N): ")
going = response.upper() == "Y"
print(going)