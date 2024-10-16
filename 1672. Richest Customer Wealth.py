def maximumWealth(accounts):
    people = len(accounts)
    richman = 0

    for i in range(people):
        wealthNum = len(accounts[i])
        sum = 0
        
        for j in range(wealthNum):
            sum = sum + accounts[i][j]
        if(sum >= richman):
            richman = sum
        
    return richman

        

testaccounts = [[1,2,3],[2,8,7],[12,15]]
result = maximumWealth(testaccounts)
print(result)