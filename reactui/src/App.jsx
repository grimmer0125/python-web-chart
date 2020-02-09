import React, { useState, useEffect } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import DateFnsUtils from "@date-io/date-fns";
import {
  MuiPickersUtilsProvider,
  KeyboardTimePicker,
  KeyboardDatePicker
} from "@material-ui/pickers";

import logo from "./logo.svg";
import "./App.css";

// https://material-ui.com/components/pickers/
function MaterialUIPickers(props) {
  const { label, date, handleDateChange } = props;

  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Grid container justify="space-around">
        <KeyboardDatePicker
          margin="normal"
          id="date-picker-dialog"
          label={label}
          format="MM/dd/yyyy"
          value={date}
          onChange={handleDateChange}
          KeyboardButtonProps={{
            "aria-label": "change date"
          }}
        />
        {/* <KeyboardTimePicker
          margin="normal"
          id="time-picker"
          label="Time picker"
          value={selectedDate}
          onChange={handleDateChange}
          KeyboardButtonProps={{
            "aria-label": "change time"
          }}
        /> */}
      </Grid>
    </MuiPickersUtilsProvider>
  );
}

function App() {
  // for testing react hooks
  const [count, setCount] = useState(0);

  const [selectedDateStart, setSelectedDateStart] = React.useState(
    new Date("2020-02-08") // "2020-02-02T21:11:54"
  );
  const [selectedDateEnd, setSelectedDateEnd] = React.useState(
    new Date("2020-02-09") //
  );

  useEffect(() => {
    // 使用瀏覽器 API 更新文件標題
    // document.title = `You clicked ${count} times`;

    console.log("window.location.href:", window.location.href);

    const paths = window.location.href.split("?");
    if (paths.length > 1) {
      const parameters = paths[1].split("&");
      if (parameters.length > 1) {
        const time1 = parameters[0].split("time1=")[1];
        const time2 = parameters[1].split("time2=")[1];
        const dateStart = new Date(parseInt(time1));
        const dateEnd = new Date(parseInt(time2));
        console.log(dateStart, dateEnd);

        setSelectedDateStart(dateStart);
        setSelectedDateEnd(dateEnd);
      }
      // http://localhost:3000/?time1=1408367514000&time2=1409317860000
    }
  }, []);

  const handleDateChange = (date, ifEnd) => {
    console.log(date);
    // const timestamp = Math.round(date.getTime() / 1000); //ms ->s
    const unixTimestamp = date.getTime(); //ms ->s

    if (ifEnd) {
      console.log("end");
      setSelectedDateEnd(date);
    } else {
      console.log("start");
      setSelectedDateStart(date);
    }
  };

  const handleClick = () => {
    console.log(
      `You are running this application in ${process.env.NODE_ENV} mode.`
    );

    const hostname = window.location.hostname; //localhost
    console.log("window.location.hostname:", window.location.hostname); // href

    const time1 = selectedDateStart.getTime();
    const time2 = selectedDateEnd.getTime();

    const timeParameters = `?time1=${time1}&time2=${time2}`;
    const djangoURL = `http://${hostname}:8000/${timeParameters}`;
    const debugReactURL = `http://${hostname}:3000${timeParameters}`;
    if (process.env.NODE_ENV === "development") {
      window.open(djangoURL);
      window.location.href = debugReactURL;
    } else {
      window.location.href = djangoURL;
    }

    setCount(count + 1);
  };

  return (
    <div className="App">
      <p>You submitted {count} times</p>
      <MaterialUIPickers
        label="Date picker dialog - start date"
        date={selectedDateStart}
        handleDateChange={date => handleDateChange(date, false)}
      />
      <MaterialUIPickers
        label="Date picker dialog - end date"
        date={selectedDateEnd}
        handleDateChange={date => handleDateChange(date, true)}
      />
      <Button onClick={handleClick} variant="contained" color="primary">
        Submit
      </Button>
    </div>
  );
}

export default App;
