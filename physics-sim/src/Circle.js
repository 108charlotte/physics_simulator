import React from 'react'; 

function Circle({ radius, coords }) {
  const { x_coord, y_coord } = coords;
  return (
    <circle cx={x_coord} cy={y_coord} r={radius} fill="black" stroke="black" />
  );
}

export default Circle;