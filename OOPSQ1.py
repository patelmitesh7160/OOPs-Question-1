class Horse:
    def __init__(self, name, max_fence_height, percentage_success):
        assert type(name) == str, "Not name"
        assert max_fence_height in range(100,150), "Not in Range"
        assert percentage_success > 70, "Very good"
        self.name = name  
        self.max_fence_height = max_fence_height 
        self.percentage_success = percentage_success  

    def get_name(self):
        return self.name

    def get_max_fence_height(self):
        return self.max_fence_height

    def success(self, fence_height):
      
        if fence_height > self.max_fence_height:
            return 0 
        else:
            return self.percentage_success
        
horse1 = Horse("1Storm", 140, 80)

print("Horse Name:", horse1.get_name())
print("Max Fence Height:", horse1.get_max_fence_height())

print("Fence 130cm ", horse1.success(130)) 
print("Fence 145cm ", horse1.success(145))  
