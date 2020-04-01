import pandas as pd 

#build df with all products for sale
pi = pd.read_csv('products_forsale.csv')  
to_sell = pd.DataFrame(pi)
to_sell["Level Down: Base Products"] = [] #fix this next 
print(to_sell["fully_qualified_name"][400:])

#create nb recipes df
nbr = pd.read_csv('nb_recipes.csv')  
nb_recipes = pd.DataFrame(nbr)
nb_recipes = nb_recipes.drop([26,27,28,29,30,39,40]).drop(columns = ['Ingredient', 'Unit'])
index = ['Kosher Sea Salt (lb)', 'Organic Honey (lb)', 'Organic Coconut Oil (lb)', 'RPS- Conventional roasted split peanuts (lb)', 'Pecans - Large Pieces (lb)', 'Dry Roasted Mission Type Almonds (lb)', 'Organic Cashew Kernels LWP (lb)', 'Chai Spice Mix - No Sugar (lb)', 'TCHO Chocolate - 81% Drops (lb)',  'Lemon Powder (lb)','Cocoa Nibs, Bulk (lb)', 'Minor Monuments Espresso (lb)', 'Crystallized Ginger Mini Chips 2-5 mm (lb)', 'Guajillo Chile Powder (lb)', 'Habanero Chile Powder (lb)',  'Ancho Chile Powder, Bulk (lb)', 'Unsweetened Coconut Chips (lb)',  'Coconut Crystals (lb)', 'Sugar, Raw Demerara (lb)', 'Vanilla Powder, Bulk (lb)', 'Hazelnut Kernels (lb)', 'Vietnamese Cinnamon, Ground (lb)', 'Organic Maple Powder (lb)', 'Organic Maple Granules (lb)', 'TCHO Chocolate - 81% Drops (lb)', 'Organic Chia Seeds (lb)', 'Total Weight (lbs)', 'Total Weight (oz)', '13oz', '10oz', '3oz', '1lb', '4lb', '8lb']
nb_recipes.index = index

#create bar recipes df
br = pd.read_csv('bar_recipes.csv')  
bar_recipes = pd.DataFrame(br)
bar_recipes = bar_recipes.drop(columns = ['Unnamed: 1','Unnamed: 11','NEW #1','Unnamed: 17' ,'Unnamed: 10','Unnamed: 2','Unnamed: 4','Unnamed: 5', 'Unnamed: 18','NEW #2','Unnamed: 16','Unnamed: 13','Unnamed: 19','Unnamed: 8' ,'Unnamed: 20', 'Unnamed: 7','Unnamed: 14'])
bar_recipes = bar_recipes.fillna(0)


#build df with base products each product implies
#columns = [product_name, sku, level_down = [(base product, sku, num_needed)]]

# pr_to_bpr = pd.DataFrame(columns = ['Product Name','sku','Level Down: Base Products'])
# pr_tobpr[]

#build df with ingredients each base product implies
#columns = [base_prodct_name, sku, level_down = [(ingredient name, sku, amt_needed)]]
#base_products = df

# bpr_to_ingredients = pd.DataFrame(columns = ['Base Product Name','sku','Level Down: Ingredients'])


#pull orders 
#transform orders ->  to lists of sku's

class Order:
    """
    Class attributes:
    order: the order itself, represented as a list of sku's.
    length: length of order, how many products did they order?
    base: dictionary corresponding to order: keys = base products (sku) the order requires, 
                                             values = num of each base product
    """

    # Constructor method.
    def __init__(self, order):
        self.order = order
        self.length = len(order)
        self.base = None

    def get_base(self):
        '''
        get_base: this method gets the dictionary base 

        '''
        base = {}
        for sku in self.order: # for product in order get base products
            base_products = products[products['sku'] == sku]['level_down'] 
            
            #accumulate all base products needed and amt 
            for product in base_products:
                name = product[0]
                sku = product[1]
                num = product[2]

                base[sku] = num #add to dict

        self.base = Order(self.base)
        return

def baseproducts_needed(orders):
    '''
    order --> base products

    '''
        
    needed ={}
    for order in orders:
        A = Order(order)
        A.get_base()
        to_add = A.base

        for sku in to_add.keys():
            if sku in needed:
                needed[sku] += to_add[sku]
            else:
                needed[sku] = to_add[sku]

    return needed

def ingredients_needed(base_products):
    '''
    base products --> ingredients 

    '''

    ingredients_final ={}
    for base_pr in base_products.keys():
        num = base_products[base_pr]
        ingredients = base_products[base_products['sku'] == sku]['level_down'] 

        for ingredient in ingredients:
            name  = ingredient[0] 
            sku = ingredient[1]
            amt = ingredient[2] 
            new_amt = amt*num #need to check units on these ...

            if sku in ingredients_final:
                ingredients_final[sku] += new_amt 

            elif sku not in ingredients_final:
                ingredients_final[sku] = new_amt

    return ingredients_final



