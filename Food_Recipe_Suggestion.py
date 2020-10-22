import urllib.request
    import re  

    recipes={}
    recipe_file = "r_data.txt"
    current_ingredients = []
    
    def getdata():
        r = [item for item in input("Enter the  Ingredients you have: ").split()]
        return r
    def read_file():
        with open(recipe_file, 'r') as f:
            for line in f:
                words = line.strip().split(",")
                if words:
                    recipes[words[0]] = words[1:]
    def Search_recipe():
        r={}
        global curret_ingredients
        for recipe, ingredients in recipes.items():
            
            type=ingredients[0]
            i=ingredients[1:]
            for ingredient in i:
                if ingredient not in current_ingredients:
                    break
            else:
                r[recipe]=type 
        return r
        
    def printdata(k):
        for recipe,ingredient in k.items():
            print('You have the ingredients to make: ',recipe)
            print("and it is a ",ingredient)
            print("Here is Video Link for this recipe :",get_videolink(recipe))
            print("")
    
    def get_videolink(name):
        name=name.lower()
        Query="+".join(name.split())
        url="https://www.youtube.com/results?search_query=recipe+for+"+Query
        html = urllib.request.urlopen(url)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        link="https://www.youtube.com/watch?v="+ video_ids[0]
        return link
       
current_ingredients=getdata()
read_file()
r=Search_recipe()
printdata(r)
