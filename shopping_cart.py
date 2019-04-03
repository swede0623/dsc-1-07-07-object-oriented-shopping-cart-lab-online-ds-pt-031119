from statistics import mean

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=None):
        
        
        if quantity:
            self.total += quantity*price
            for x in range(0, quantity):
                new_dict = {}
                new_dict[name] = price
                self.items.append(new_dict)
        else:
            self.total += price
            new_dict = {}
            new_dict[name] = price
            self.items.append(new_dict)
        
        return self.total
            
    def mean_item_price(self):
        price_list = []
        for k,v in [list(x.items())[0] for x in self.items]:
            price_list.append(v)
        return mean(price_list)    
            

    def median_item_price(self):
        price_list = []
        for k,v in [list(x.items())[0] for x in self.items]:
            price_list.append(v)
        
        if len(price_list) % 2 == 0:
            return price_list[int(len(price_list)/2)] + price_list[int(len(price_list)/2 - 1)] /2
        else:
            return price_list[int(len(price_list)/2-.5)]

    def apply_discount(self):
        
        if self.employee_discount:
            return self.total * ((100 - self.employee_discount) / 100)
        else:
            return "Sorry, you are not eligible for any discount"

    def void_last_item(self):
        
        
        if len(self.items) == 0:
            return "No items in shopping cart"
        else:
            last_item = self.items.pop()
            last_item_price = list(last_item.values())[0]
            self.total = self.total - last_item_price
            return self.total
        
        
        