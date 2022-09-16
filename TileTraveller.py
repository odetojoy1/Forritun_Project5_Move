

# def direction(position, travel):
#     if position == '1,1':
#         print("you can travel North")
    

# position = '1,1'
# #direction = 'NnSsWwEe'
# direction_allowed = 'NnSsWwEe'

# Input_direction = 'N'
# while Input_direction[0] == direction_allowed:
#     Input_direction = input("Direction:")


# def You_can_travel(position):
#     if position == 11:
#         travel = 'Nn'
#     return travel
       
def direction_str(position):
    if position == '1,1' or position == '2,1':
        direction = 'N'    

    if position == '1,2' or position == '3,2':
        direction = 'NS'

    if position == '1,3':
        direction = 'SE' #str(south + east)

    if position == '2,3':
        direction = 'WE' #str(west + east)

    if position == '2,2' or position == '3,3':
        direction = 'WS' #str(west + south)
       
    return direction

def next_cell(position,direction):
    if position == '1,1':
        cells = '1,2'
    if position == '1,2':
        if direction == 'N':
            cells = '1,3'
        if direction == 'E':
            cells = '2,2'
        if direction == 'S':
            cells = '1,1'

    if position == '1,3':
        if direction =='S':
            cells = '1,2'
        if direction == 'E':
            cells = '2,3'
   
    if position == '2,3':
        if direction =='W':
            cells = '1,3'
        if direction == 'E':
            cells = '3,3'

    if position == '2,2':
        if direction == 'W':
            cells = '1,2'
        if direction == 'S':
            cells = '2,1'

    if position == '2,1':
        cells = '2,2'

    if position == '3,3':
        if direction == 'W':
            cells = '2,3'
        if direction == 'S':
            cells = '3,2'

    if position == '3,2':
        if direction == 'N':
            cells = '3,3'
        if direction == 'S':
            cells = '3,1'
    return cells

north = 'N'
south = 'S'
west = 'W'
east = 'E'

position = '1,1'
possible_direction = 'N'
direction = 'N'
while position != '3,1':
    possible_direction = str(direction_str(position))
    print('You can travel: ', possible_direction)
    direction = str(input('Direction: '))
    
    if possible_direction.find(direction) >= 0:
        position = next_cell(position, direction)
    else:
        print('Not a valid direction!')
print("Victory!")