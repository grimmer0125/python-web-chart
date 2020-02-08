import React, { useState } from "react";
import Button from "@material-ui/core/Button";

import logo from "./logo.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  function handleClick() {
    console.log(
      `You are running this application in ${process.env.NODE_ENV} mode.`
    );

    const hostname = window.location.hostname; //localhost
    console.log("window.location.hostname:", window.location.hostname); // href

    const timeParameters = "?time1=10&time2=20";
    const djangoURL = `http://${hostname}:8000/chart/mode1${timeParameters}`;
    const debugReactURL = `http://${hostname}:3000${timeParameters}`;
    if (process.env.NODE_ENV === "development") {
      window.open(djangoURL);
      window.location.href = debugReactURL;
    } else {
      window.location.href = djangoURL;
    }

    setCount(count + 1);
  }

  return (
    <div className="App">
      <p>You clicked {count} times</p>
      <Button onClick={handleClick} variant="contained" color="primary">
        Click me
      </Button>
    </div>
  );
}

export default App;
