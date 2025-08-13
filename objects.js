class Object {
    constructor(coords, color) {
        // unpack and assign coordinates
        const [x, y] = coords;
        this.x = x;
        this.y = y;
        this.color = color;
    }

    setCoords(new_coords) {
        const [x, y] = new_coords;
        this.x = x;
        this.y = y;
    }

    getCoords() {
        return [this.x, this.y];
    }
}

class Circle extends Object {
    constructor(radius, coords, color) {
        super(coords, color);
        this.radius = radius;
    }

    draw(ctx) {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.stroke();
    }
}

class Square extends Object {
    constructor(side, coords, color) {
        super(coords, color);
        this.side = side;
    }
    
    draw(ctx) {
        ctx.fillStyle = this.color; 
        ctx.fillRect(this.x, this.y, this.side, this.side); 
    }
}

class Polygon extends Object {
    // circumradius = distance from center to vertices
    constructor(num_sides, circumradius, center_coords, color) {
        super(center_coords, color);
        this.vertices = calcVertices(center_coords, num_sides, circumradius);
        this.num_sides = num_sides;
        this.circumradius = circumradius;
    }
    setCoords(new_coords) {
        const [x, y] = new_coords;
        this.x = x;
        this.y = y;
        this.vertices = calcVertices(new_coords, this.num_sides, this.circumradius);
    }
    getVertices() {
        return this.vertices;
    }
    
    draw(ctx) {
        ctx.beginPath();
        ctx.moveTo(this.vertices[0][0], this.vertices[0][1]);
        for (let i = 1; i < this.vertices.length; i++) {
            ctx.lineTo(this.vertices[i][0], this.vertices[i][1]);
        }
        ctx.closePath();
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.stroke();
    }
}


function calcVertices(center_coords, num_sides, circumradius) {
    // for the draw function later, and just to have
    let vertices = [];
    let curr_angle = 90;
    for (let side = 0; side < num_sides; side++) {
        vertices.push(calcVertexCoord(center_coords, curr_angle, circumradius, side, num_sides));
        curr_angle += 360 / num_sides;
    }
    return vertices;
}


function calcVertexCoord(cent_coords, curr_angle, circrad, vertex_num, num_vertices) {
    let [x, y] = cent_coords;
    // calculate angle degree
    // converted to radians
    let angle_rad = curr_angle * Math.PI / 180;
    // update x and y based on sin and cosine
    x += circrad * Math.cos(angle_rad);
    y -= circrad * Math.sin(angle_rad);
    return [x, y];
}