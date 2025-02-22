def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    k=0
    for i in data:
        if i["age"]==age:
            k+=1
    return k
data = [
  {
    'name': 'John',
    'age': 27
  },
  {
    'name':'Mary', 
    'age': 42
  },
  {
    'name':'Ann',
    'age': 27
  }
  ]
print(count_users_with_age(data,27))