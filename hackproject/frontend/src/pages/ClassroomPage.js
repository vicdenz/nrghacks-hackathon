import React, { useState, useEffect } from "react";
import Draggable from 'react-draggable';

const ClassroomPage = () => {

  // This function will be called when dragging starts
  const handleStart = (e, data) => {
    console.log('Drag started at: ', data.x, data.y);
  };

  // This function will be called while dragging
  const handleDrag = (e, data) => {
    console.log('Dragging at: ', data.x, data.y);
  };

  // This function will be called when dragging stops
  const handleStop = (e, data) => {
    console.log('Drag stopped at: ', data.x, data.y);
  };

  return (
    <Draggable
      onStart={handleStart}
      onDrag={handleDrag}
      onStop={handleStop}>
      <div className="box">
        I can be dragged
      </div>
    </Draggable>
  );
};

export default ClassroomPage;
