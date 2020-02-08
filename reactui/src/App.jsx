import React, { useState } from "react";
import Button from "@material-ui/core/Button";

import logo from "./logo.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div className="App">
      <p>You clicked {count} times</p>
      <Button onClick={handleClick} variant="contained" color="primary">
        Click me
      </Button>
      You are running this application in <b>{process.env.NODE_ENV}</b> mode.
    </div>
  );
}

export default App;
