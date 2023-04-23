class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=''
        carry=0
        a_ptr,b_ptr=len(a)-1,len(b)-1
        while a_ptr>=0 or b_ptr>=0:
            if a_ptr>=0:
                carry+=int(a[a_ptr])
                a_ptr-=1
            if b_ptr>=0:
                carry+=int(b[b_ptr])
                b_ptr-=1
            res=str(carry%2)+res
            carry=carry//2           
        return str(carry)+res if carry else res