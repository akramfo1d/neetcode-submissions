class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top,left,right,bottom=0,0,len(matrix[0]),len(matrix)
        res=[]
        while right>left and bottom>top:
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1

            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            if not(left <right and top<bottom):
                break
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1

            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        return res

        