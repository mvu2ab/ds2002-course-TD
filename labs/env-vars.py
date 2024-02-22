import os
#!//Library/Frameworks/Python.framework/Versions/3.12/bin/python3
chmod 755 env-vars.py
os.environ["FAV_SUBJECT"] = "ENGLISH"
os.environ["FAV_SPORT"] = "TRACK"
os.environ["UVA_YEAR"] = "THIRD"
FAV_SUBJECT = input ('WHAT IS YOUR FAVORITE SUBJECT?')
FAV_SPORT = input ('WHAT IS YOUR FAVORITE SPORT?')
UVA_YEAR = input ('WHAT YEAR ARE YOU AT UVA?')
print(FAV_SUBJECT)
print(FAV_SPORT)
print(UVA_YEAR)
os.environ["UVA_YEAR"] = "THIRD"
YEAR_ENV = os.getenv("UVA_YEAR")
print(os.getenv("UVA_YEAR"))

