class TimeMap:

    def __init__(self):
        self.value_map = {}  # document structure with key , timestamp,value

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.value_map:
            self.value_map[key][timestamp] = value
        else:
            self.value_map[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if self.value_map.get(key,None):
            if self.value_map[key].get(timestamp):
                return self.value_map[key][timestamp]
            else:
                return_value = ""
                for time in self.value_map[key]:
                    if time>timestamp:
                        break
                    else:
                        return_value = self.value_map[key][time]
                return return_value
        else:
            return "" 
        
