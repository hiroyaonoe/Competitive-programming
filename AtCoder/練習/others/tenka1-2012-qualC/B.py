from collections import deque
import re

s=input()

cards=deque(re.split(r'(S|H|D|C)',s))

cards.popleft()
marks=['S','H','D','C']
royal=['10','J','Q','K','A']

his={mark:[] for mark in marks}

sute={mark:[] for mark in marks}

while len(cards)>0:
    suteok={mark:True for mark in marks}
    mark=cards.popleft()
    num = cards.popleft()
    if (num in royal)&(num not in his[mark]):
        his[mark].append(num)
        suteok[mark]=False
    for mm in marks:
        if suteok[mm]:
            sute[mm].append(mark+num)
    for mm in marks:

        if len(his[mm])==5:
            if len(sute[mm])==0:
                ans=0
            else:
                ans="".join(sute[mm])
            print(ans)
            exit()







