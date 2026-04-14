from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winDict = defaultdict(int)
        totalDict = defaultdict(int)
        for winner, loser in matches: #store each players total games and win loss as +1 or -1
            winDict[winner] += 1 #update pos for win
            winDict[loser] += 0 #update neg for loss
            
            #they both played a match
            totalDict[winner] += 1
            totalDict[loser] += 1

        answer = [[],[]]
        print(winDict.items())
        print(totalDict.items())
        for key in winDict.keys():
            totWins = winDict[key]
            totGame = totalDict[key]
            diff = totGame - totWins
            print(key, diff)
            if diff < 2:
                answer[diff].append(key)

        answer[0].sort()
        answer[1].sort()
        return answer

        
                
