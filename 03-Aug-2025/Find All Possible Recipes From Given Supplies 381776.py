# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        setSupplies = set(supplies)
        self.n = len(recipes)
        self.ans = []
        self.suppliesmap = {}
        self.hmap = {}
        for supply in supplies:
            self.suppliesmap[supply] = True
        for i, recip in enumerate(recipes):
            self.hmap[recip] = i

        def createRecipes(recipe):
            self.suppliesmap[recipe] = False
            if recipe not in self.hmap:
                return False
            

            for need in ingredients[self.hmap[recipe]]:
                if need in self.suppliesmap:
                    if self.suppliesmap[need] == False:
                        return False
                    elif self.suppliesmap[need] == True:
                        continue
                else:
                    if not createRecipes(need):
                        return False
            
            self.suppliesmap[recipe] = True
            if recipe in self.hmap: self.ans.append(recipe)
            return True

        for r in recipes:
            if r not in self.suppliesmap:
                createRecipes(r)
        return self.ans