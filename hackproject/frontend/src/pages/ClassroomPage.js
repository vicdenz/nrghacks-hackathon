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
      <button onClick={addDraggable}>Add Draggable</button>
    </div>
  );
}

export default ClassroomPage;
