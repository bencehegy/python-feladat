'''
The standard ACL numbers are between 1 and 99 (inclusive)
The extended ACL numbers are between 100 199 (inclusive)
Other ACL numbers are nor standard nor extended.
Input an ACL number and categorize it!
'''

def categorize_acl(acl_number):
    if 1 <= acl_number <= 99:
        print("The ACL number is Standard.")
    elif 100 <= acl_number <= 199:
        print("The ACL number is Extended.")
    else:
        print("The ACL number is neither Standard nor Extended.")

# Example usage
acl_number = int(input("Enter an ACL number: "))
categorize_acl(acl_number)