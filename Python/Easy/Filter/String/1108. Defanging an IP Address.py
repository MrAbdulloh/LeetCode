"""
https://leetcode.com/problems/defanging-an-ip-address/description/
"""


def defangIPaddr(address: str) -> str:
    ## first method

    # return '[.]'.join(address.split('.'))

    ## second method

    return address.replace('.', '[.]')


address = "255.100.50.0"
print(defangIPaddr(address))
