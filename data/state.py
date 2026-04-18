def state(name:str="Player 1") -> dict:
    return {
        "score":0, 
        "lives":3, 
        "atlantic_wins":0, 
        "pacific_wins":0, 
        "name":name
    }
    