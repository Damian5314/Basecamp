human_years=int(input("How many human years?: "))

dog_years=21+(human_years-2)*4

if human_years==1:print("Dog years: 10.5")
elif human_years==2:print("Dog years: 21")
elif human_years>=2:print("Dog years:", dog_years )
elif human_years<=0:print("Only positive numbers are allowed")
