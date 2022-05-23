class HashTable(object):
    """
    HashTable: Class to create an instance of a HashTable data structure.

    """
    def __init__(self,size = 1024):
        self.size = size
        self.table = [None] * size

  
    def set(self,key,value):
        """
        set(self, key, value): method that takes key and value. This method hash the key, and add the key and value pair to the table, handling collisions as needed.

        """
            
        index = self.hash(key)
        
        if self.table[index]:
            if key in self.keys():
                for dic in self.table[index]:
                    if key in dic.keys():
                        dic[key] = value
            else:
                self.table[index].append({f"{key}":f"{value}"})
        else:
            self.table[index] = [{f"{key}":f"{value}"}]        
                            
    def get(self,key):
        """
        get(self, key): method that takes in the key and returns its value from the table.

        """
        if type(key) is not str:
            raise Exception("Key must be a string")
        
        index = self.hash(key)
        
        if not self.table[index]:
            return None
        
        for dic in self.table[index]:
            if key in dic.keys():
                return dic[key]
   
    def contains(self,key):
        """
        contains(self, key): method that takes in the key and returns a boolean, indicating if the key exists in the table already.
        """
        if type(key) != str:
            raise Exception("Key must be a string")
        
        index = self.hash(key)
        
        if not self.table[index]:
            return False
        
        for dic in self.table[index]:
            if key in dic.keys():
                return True
            return False
     
    def keys(self):
        """
        keys(self): a method that returns the collection of keys.
        """
        keys = []
        for index in self.table :
            if index:
                for dic in index:
                        [keys.append(key) for key in dic.keys()]
                        
        return keys


# if __name__ == "__main__":
#     hashtable = HashaTable()
#     hashtable.add("cloud", "AWS")
#     hashtable.add("cloud", "Azure")
#     hashtable.add("could", "Rainy")
#     hashtable.add("name", "Python")
#     print(hashtable["name"])