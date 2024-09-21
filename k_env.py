

def Kenv(s:int,k:int) -> list[int]:
    global env
    global  track

    def backtracking(index:int):
        global env
        global  track
        if index > 0:
            if len(track) == k:
                env.append(track)
                return
        
        for i in range(index, s):
            track.append(i)
            backtracking(i+1)
            track = track[:len(track) - 1]

    backtracking(0)
    
    return env


if __name__ == "__main__":
    env:list[list[int]] = []
    track:list[int] = []
    Kenv(10,4)
    for t in env: 
        print(t)