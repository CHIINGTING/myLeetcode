class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.compare(s) == self.compare(t)

    def compare(self,s):
        t=[]
        for i in iter(s):
            if i == '#':
                if len(t)>0:
                    t.pop()
            else:
                t.append(i)
        return ''.join(t)