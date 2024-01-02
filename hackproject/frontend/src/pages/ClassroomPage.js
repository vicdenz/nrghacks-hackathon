import React, { useState } from 'react';
import Draggable from 'react-draggable';

function ClassroomPage() {
  const [draggables, setDraggables] = useState([]);

  const addDraggable = () => {
    setDraggables([...draggables, '']);
  };

  const handleStart = () => { /* ... */ };
  const handleDrag = () => { /* ... */ };
  const handleStop = () => { /* ... */ };

  const handleChange = (index) => (event) => {
    const newDraggables = [...draggables];
    newDraggables[index] = event.target.value;
    setDraggables(newDraggables);
  };

  return (
    <div className="rainbow-gradient">
      <button onClick={addDraggable}>Add Student</button>
      <div className="ratings">
        <h1>Excellent</h1>
        <h1>Good</h1>
        <h1>Okay</h1>
        <h1>Satisfactory</h1>
        <h1>Needs Improvement</h1>
      </div>
      <div>
        {draggables.map((text, index) => (
          <Draggable
            key={index}
            onStart={handleStart}
            onDrag={handleDrag}
            onStop={handleStop}>
            <div className="box">
              <textarea
                onChange={handleChange(index)}
                value={text}
              ></textarea>
            </div>
          </Draggable>
        ))}
      </div>
    </div>
  );
}

export default ClassroomPage;
