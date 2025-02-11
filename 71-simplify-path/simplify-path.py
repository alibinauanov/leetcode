class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        arr = path.split("/")
        res = []
        for i in range(len(arr)):
            if arr[i] == "" or arr[i] == ".":
                continue
            
            if arr[i] == "..":
                if res:
                    res.pop()
            else:
                res.append(arr[i])
        return "/" + "/".join(res)