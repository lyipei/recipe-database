import sqlite3

conn = sqlite3.connect('recipes.db')
print ("Opened database successfully")

# create table
conn.execute(''' CREATE TABLE IF NOT EXISTS recipes
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             ingredients TEXT,
             instructions TEXT);''')

# insert default sample data when table is empty
cursor = conn.execute('SELECT COUNT(*) FROM recipes')
count = cursor.fetchone()[0]
if count == 0: # if table is empty, insert sample data = egg tart
    conn.execute(''' 
            INSERT INTO recipes (name, ingredients, instructions)
             values (?, ?, ?)''',
             ('Egg Tart', '2 eggs, sugar: 50g, milk: 60g', '1. Preheat oven to 180C. 2. Mix all ingredients. 3. Pour into tart shells. 4. Bake for 20 minutes.'))
    # insert sample data - brownies
    conn.execute(''' 
            INSERT INTO recipes (name, ingredients, instructions)
             values (?, ?, ?)''',
             ('Brownies', '2 eggs, powered sugar, unsweetened cocoa powder, oil, vanilla: 1/2 teaspoon', '1. Preheat oven to 325F. 2. Mix together the dry and wet ingredients in two separate bowls. 3. Combine the wet and dry ingredients. 4. Pour the batter into baking pan. 5. Bake for 40 - 50 minites!'))

    conn.commit()
    print("Recipes inserted SUCCESSFULY!")

# ALLOW USER ADD MORE RECIPES
def add_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients: (e.g., Eggs: 2, Sugar: 100g) ")
    instructions = input("Enter the instructions: (e.g. 1. Preheat oven to 180c. 2...)")
    
    conn.execute('INSERT INTO recipes (name, ingredients, instructions) values (?, ?, ?)',
                 (name, ingredients, instructions))
    conn.commit()
    print(f"Recipe '{name}' added SUCCESSFULY!")

# ALLOW USER VIEW RECIPES
def view_recipe():
    cursor = conn.execute('SELECT id, name from recipes')
    print("\n ------- RECIPES LIST ------- ")
    for row in cursor:
        print(f"\n ID: {row[0]}  -  Name: {row[1]}")

def view_recipe_details():
    recipe_id = input("Enter the recipe ID to view details: ")
    cursor = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
    row = cursor.fetchone()
    if row: 
        print(f'\nName: {row[1]}')
        print(f'Ingredients:\n {row[2]}')
        print(f'Instructions:\n {row[3]}')
    else:
        print("Recipe not found. Please check the ID and try again.")

# ALLOW USER DELETE RECIPES

def delete_recipe():
    recipe_id = input("Enter the recipe ID to delete: ")
    conn.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
    conn.commit()
    print(f'Recipe deleted SUCCESSFULY!')


# ALLOW USER EDIT RECIPES
def edit_recipe():
    recipe_id = input("Enter the recipe ID to edit: ")
    cursor = conn.execute('SELECT name, ingredients, instructions FROM recipes WHERE id = ?', (recipe_id,)) 
    row = cursor.fetchone()
    if not row:
        print("Recipe not found. Please check the ID and try again.")
        return

    # Prompt user for new values 
    name = input(f'Enter new name: ') 
    ingredients = input(f'Enter new ingredients: ')
    instructions = input(f'Enter new instructions: ')

    conn.execute('''
                UPDATE recipes
                SET name = ?, ingredients = ?, instructions = ?
                WHERE id = ? ''',
                (name if name else row [0], ingredients if ingredients else row [1], instructions if instructions else row [2], recipe_id))
    conn.commit()
    print(f'Recipe updated SUCCESSFULY!')
    
while True:
    # display menu
    print("\n ------- RECIPE DATABASE MENU ------- ")
    print("1. View recipes")
    print("2. view recipe details")
    print("3. Add a new recipe")
    print("4. Edit a recipe")
    print("5. Delete a recipe")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        view_recipe()
    elif choice == '2':
        view_recipe_details()
    elif choice == '3':
        add_recipe()
    elif choice == '4':
        edit_recipe()
    elif choice == '5':
        delete_recipe()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()
    
