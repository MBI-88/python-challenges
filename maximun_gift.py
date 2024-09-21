def maximunGift(arr:list[tuple], weight:int) -> int:
    global maximun
    def backtracking(index, tv, tw,):
        global maximun
        if tv > maximun and tw <= weight:
            maximun = tv
        
        if tw > weight:
            return 
        
        for i in range(index, len(arr)):
          backtracking(i+1, tv + arr[i][0], tw +  arr[i][1])

    backtracking(0,0,0)

    return maximun


if __name__ == "__main__":
    maximun = 0
    gift1 = [(10,2), (5,4), (6,1), (8,3)] # [(value, weght)]
    gift2 = [(20,10), (15,15), (7,1), (3,3)]
    gift3 = [(8,2), (9,4), (16,4), (20,3)]
    back = 5 

    print(f"Maximun gift {maximunGift(gift1,back)}")
    print(f"Maximun gift {maximunGift(gift2,back)}")
    print(f"Maximun gift {maximunGift(gift3,back)}")


    