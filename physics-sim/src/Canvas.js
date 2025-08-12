import logo from './logo.svg';
// import './App.css';
import React from 'react'; 
import Circle from './Circle'; 

let circles = [
  { radius: 50, coords: { x_coord: 100, y_coord: 100 } }
];

function App() {
  return (
    <div className="App">
      <svg width="400" height="400" style={{ border: "1px solid black" }}>
        {circles.map((circle) => (
          <Circle radius={circle.radius} coords={circle.coords} />
        ))}
      </svg>
    </div>
  );
}

export default App;
