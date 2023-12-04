#Write a program that displays a logical error. Be creative!
print("""Welcome to the GOlden NecklaCe Game!
Mary has 5 sets of 3 golden rings which she wants to join to make a necklace.
The last ring has a closing mechanism, illustrated with a @ sign.
How many rings will she have to break and weld back together \
to make her necklace ?
This is how it looks:
OOO
OOO
OOO
OOO
OO@
Give the position of each O ring you want to break to build the necklace. 
A broken ring O will turn into a C and will serve to join the rings.
""")
start_rings = ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","@"]
user_choice = 0
user_positions = []

# Error handling, ensuring user is within range and uses positive integers
while True:
    user_choice = input("Please enter a position or type 'end' to exit): ")
    if user_choice.lower() == "end":
        break
    try:
        position = int(user_choice)
        if position > 15:
            raise ValueError("You only have fifteen rings...")
        elif position < 1:
            raise ValueError("This ring does not exist")
        elif position in user_positions:
            raise ValueError("This ring has already been broken")
        elif position == 15:
            raise ValueError("This is the opening mechanism, why break it?")
        user_positions.append(position)
    except ValueError as e:
        print(e)  
print(f"Your broken rings are: {user_positions}")
new_ring_wrong = ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","@"]
new_ring_right = ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","@"]

#Progran will match selected rings against the existing and replace with 'C'
for i in range(len(start_rings)):
    if i in user_positions:
        new_ring_wrong[i+1] = "C" #Logical:Should be 'i-1'. Select wrong ring
        new_ring_right[i-1] = "C"

# Here we print the 2 solutions, 1 with the logical error, and 1 without.
print("With logical error, and without:\n",
*new_ring_wrong[0:3],"\t\t",*new_ring_right[0:3],"\n",
*new_ring_wrong[3:6],"\t\t",*new_ring_right[3:6],"\n",
*new_ring_wrong[6:9],"\t\t",*new_ring_right[6:9],"\n",
*new_ring_wrong[9:12],"\t\t",*new_ring_right[9:12],"\n",
*new_ring_wrong[12:16],"\t\t",*new_ring_right[12:16])

#Depending on your choices, you have these 3 different outcomes
if user_positions == [1,2,3] or user_positions == [4,5,6] or user_positions \
== [7,8,9] or user_positions == [10,11,12]:
    print("Your necklace looks like this:\n O O O C O O O C O O O C O O @\n\
WELL DONE, you have found the minimum number of breaks and weldings: 3.")
elif user_positions == [3,6,9,12]:
    print("Your necklace looks like this:\n O O C O O C O O C O O C O O @\n\
Not bad, but you can do better...")
else:
    print("Doesn't look like a necklace to me...")