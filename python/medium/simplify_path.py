"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        splited = path.split('/')
        canonical = []
        
        for item in splited:
            if (item == '' or item == '.'):
                continue
            
            if (item == '..'):
                # Go back
                if (canonical): 
                    canonical.pop()
                continue
            
            # add path to canonical
            canonical.append(item)
        
        return  '/' + '/'.join(canonical)
    
    
s = Solution()
print(s.simplifyPath('/home/')) # /home
print(s.simplifyPath('/../')) # /
print(s.simplifyPath('/home//foo/')) # /home/foo
print(s.simplifyPath('/home/../foo/')) # /foo

