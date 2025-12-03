# Smart Traffic Light System
# DO NOT use max(), sorted(), or any built-in sorting methods.
# Use ONLY if-elif-else statements for all logic.

# Use this Input structure
traffic = {
    "North": {"density": "Medium", "emergency": False},
    "South": {"density": "High", "emergency": False},
    "East": {"density": "High", "emergency": True},
    "West": {"density": "Low", "emergency": False}
}
direction = ["North", "South", "East", "West"]
density = 0
#Create function to change density to numeric values
def denseChange(density):
    if "density" == "Low":
        density = 1
    elif "density" == "Medium":
        density = 2
    else:
        density = 3

denseVar = denseChange(density)

#Create function to decide with traffic direction goes first and create priority list incase there is more than 1 direction has an emergency
def wayFirst(direction):
    for directions in direction:
        if "emergency" == True:
            print("East has green light")
        else:
            if "emergency" == False and denseVar == 3:
                print("South has green light")
            if "emergency" == False and density == 2:
                print("North has green light")
            if "emergency" == False and density == 1:
                print("West has green light")

# Call the function
wayFirst(direction)

#FAILED TO SUCCEED IN MODIFYING CODE SO FAR
