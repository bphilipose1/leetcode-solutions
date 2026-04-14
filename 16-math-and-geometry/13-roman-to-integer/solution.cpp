class Solution {
public:
    int romanToInt(string s) {
        int runningCount = 0;
        
        switch(s[0])    {
                case 'I': 
                    runningCount += 1;
                    break;
                case 'V': 
                    runningCount += 5;
                    break;
                case 'X': 
                    runningCount += 10;
                    break;
                case 'L': 
                    runningCount += 50;
                    break;
                case 'C': 
                    runningCount += 100;
                    break;
                case 'D': 
                    runningCount += 500;
                    break;
                case 'M': 
                    runningCount += 1000;
                    break;
            
            }
        for(int i = 1; i < s.length(); i++) {
            char first = s[i-1];
            char next = s[i];

            if(first == 'I')    {
                
                if(next == 'V') {
                    runningCount += 4 - 1;
                    continue;
                }
                if(next == 'X') {
                    runningCount += 9 - 1;
                    continue;
                }
            }
            if(first == 'X')    {
                if(next == 'L') {
                    runningCount += 40 - 10;
                    continue;
                }
                if(next == 'C') {
                    runningCount += 90 - 10;
                    continue;
                }
            }
            if(first == 'C')    {
               
                if(next == 'D') {
                    runningCount += 400 - 100;
                    continue;
                }
                if(next == 'M') {
                    runningCount += 900 - 100;
                    continue;
                }
            }

            switch(next)    {
                case 'I': 
                    runningCount += 1;
                    break;
                case 'V': 
                    runningCount += 5;
                    break;
                case 'X': 
                    runningCount += 10;
                    break;
                case 'L': 
                    runningCount += 50;
                    break;
                case 'C': 
                    runningCount += 100;
                    break;
                case 'D': 
                    runningCount += 500;
                    break;
                case 'M': 
                    runningCount += 1000;
                    break;
            
            }
            



        }
        return runningCount;
    }
};