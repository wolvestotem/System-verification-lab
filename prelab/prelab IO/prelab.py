import sys

def solution(result):
    if(len(sys.argv)==1):
        return
    key = sys.argv[1]
    source = open("covid-confirmed-us-subset.txt","r")
    lists = source.readlines()
    for place in lists:
        # print(place.find(key))
        if(place.find(key)!=-1):
            result.write(place)
    source.close()


if __name__ == "__main__":

  # Write your code here
  # Hint: you can access the command line arguments using sys.argv list
    result = open("result.txt","w")
    solution(result)
    result.close()


