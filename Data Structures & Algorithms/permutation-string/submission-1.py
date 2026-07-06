class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        window1=[0]*26
        window2=[0]*26

        for i in range(len(s1)):
            window1[ord(s1[i])-ord('a')]+=1
            window2[ord(s2[i])-ord('a')]+=1

        if window1==window2:
            return True

        l=0

        for r in range(len(s1),len(s2)):
            window2[ord(s2[r])-ord('a')]+=1
            window2[ord(s2[l])-ord('a')]-=1
            l+=1

            if window2==window1:
                return True
        return False