


#downloads = [500, 50, 250, 101]

#for count in downloads:
 #   if count > 100:
  #      print("Alert!")

   #     downloads = {
    #"John": 500,
    #"Mary": 50,
    #"Steve": 250
#}

downloads = {
    "John": 500,
    "Mary": 50,
    "Steve": 250
}

for username, count in downloads.items():
    print(username, count)