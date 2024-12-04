# Recursion is a process where a function calls itself one or more times with modified values to accomplish a task. This technique can be particularly effective when solving complex problems that can be broken down into smaller, simpler problems of the same type. In the provided code, the count_users function uses recursion to count the number of users that belong to a group within a company's system. It does this by iterating through each member of a group, and if a member is another group, it recursively calls count_users to count the users within that subgroup. However, there is a bug in the code! Can you spot the problem and fix it?
def count_users(group):
    count = 0
    for member in get_members(group):  # Assuming get_members(group) returns the members of the group
        if is_group(member):  # Check if the member is a group
            count += count_users(member)  # Recursively count users in the subgroup
        else:
            count += 1  # Otherwise, it's a user, so increment the count
    return count

# Test cases
print(count_users("sales"))       # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone"))    # Should be 18