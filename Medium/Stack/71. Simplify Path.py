# https://leetcode.com/problems/simplify-path/description/

def simplifyPath(path: str) -> str:
    stack = []
    a = path.split('/')
    for i in a:
        if i == '' or i == '.':
            continue
        elif i == '..':
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return '/' + '/'.join(stack)


# path = "/home///////foo/../"
# path = "/../"
path = '/a/../../b/../c//.//"'
print(simplifyPath(path))
