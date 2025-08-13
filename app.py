from flask import Flask, render_template, redirect
from objects import Circle, Square, Polygon
import random
import importlib
from physics_2d import update_positions
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

physics_module = importlib.import_module("physics_2d")

objects = []

@app.route("/")
def index(): 
    return render_template('index.html')

def sim_loop(): 
    while True: 
        update_positions(objects)

        socketio.emit('object_update', [obj.to_dict() for obj in objects])
        freq = 1 / 60
        socketio.sleep(freq)

@app.route('/reset_objects', methods=['POST'])
def reset_objects():
    global objects
    objects = []
    return redirect("/")

@socketio.on('mouse_click')
def handle_mouse_click(data): 
    x = data['x']
    y = data['y']
    mouse_pos = (x, y)
    # generate random RGB values
    red_amt = random.randint(0, 255)
    green_amt = random.randint(0, 255)
    blue_amt = random.randint(0, 255)
    color = (red_amt, green_amt, blue_amt)
    # generate random object type
    object_type_num = random.randint(1, 3)
    # generate random velocity
    random_vel_x = random.randint(-10, 10)
    random_vel_y = random.randint(-10, 10)

    while random_vel_x == 0 and random_vel_y == 0: 
        random_vel_x = random.randint(-10, 10)
        random_vel_y = random.randint(-10, 10)
    
    # circle
    if object_type_num == 1: 
        # generate random radius
        radius = random.randint(10, 50)
        # create circle object and add to objects list
        newCircle = Circle(radius, mouse_pos, color, (random_vel_x, random_vel_y))
        objects.append(newCircle)
    # square
    elif object_type_num == 2: 
        # generate random side length
        side = random.randint(10, 50)
        # update coords for mouse position so that they are for center of square
        x, y = mouse_pos
        x -= side/2
        y -= side/2
        mouse_pos = (x, y)
        # create square object and add to objects list
        newSquare = Square(side, mouse_pos, color, (random_vel_x, random_vel_y))
        objects.append(newSquare)
    elif object_type_num == 3: 
        # generate random circumradius
        circrad = random.randint(10, 50)
        # generate random num sides
        num_sides = random.randint(3, 12)
        # create polygon object and add to objects list
        newPoly = Polygon(num_sides, circrad, mouse_pos, color, (random_vel_x, random_vel_y))
        objects.append(newPoly)

@socketio.on('connect')
def connected(): 
    print("SocketIO connected")

if __name__ == "__main__": 
    socketio.start_background_task(sim_loop)
    socketio.run(app, debug=True)  # Use socketio.run instead of app.run