/**
 * This is a React web application (client side rendering)
 */

const { Button, FocusStyleManager, Classes } = Blueprint.Core;
FocusStyleManager.onlyShowFocusOnTabs();

const {
  DateRange,
  DatePicker,
  DateRangePicker,
  TimePrecision
} = Blueprint.Datetime;

function incrementCounter() {
  console.log("incrementCounter");
}

const modeOptions = [
  {
    value: "mode1",
    text: "live mode (last 30 mins)"
  },
  {
    value: "mode2",
    text: "6/25"
  }
];

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      selectedMode: null,
      maxDateIndex: 0,
      minDateIndex: 0
    };
  }

  handleDateChange = dateRange => {
    this.setState({ dateRange });
  };

  handleSwitchMode = (e, obj) => {
    const { value } = obj;

    console.log("switch file:", value);

    this.setState({
      selectedMode: value
    });

    if (value === "mode1") {
      // reload mode1 html
      window.location.href = "http://127.0.0.1:8000/chart/mode1";
    } else if (value === "mode2") {
      // reload mode2 html
      window.location.href = "http://127.0.0.1:8000/chart/mode2";
    }
  };

  render() {
    const MIN_DATE_OPTIONS = [
      { label: "None", value: undefined },
      {
        label: "4 months ago",
        value: moment()
          .add(-4, "months")
          .toDate()
      },
      {
        label: "1 year ago",
        value: moment()
          .add(-1, "years")
          .toDate()
      }
    ];

    const MAX_DATE_OPTIONS = [
      { label: "None", value: undefined },
      {
        label: "1 month ago",
        value: moment()
          .add(-1, "months")
          .toDate()
      }
    ];

    const { minDateIndex, maxDateIndex, ...props } = this.state;

    const minDate = MIN_DATE_OPTIONS[minDateIndex].value;
    const maxDate = MAX_DATE_OPTIONS[maxDateIndex].value;

    const { selectedMode } = this.state;
    return (
      <div>
        <Title />
        {/* Custom2 menus part by using Reactjs, when users choose different menus,
        a different chart url request will be sent{" "} */}
        <div>
          <div>
            {/* <Button icon="refresh" intent="danger" text="Reset" /> */}
            {/* <Button
              icon="refresh"
              intent="success"
              text="button content"
              onClick={incrementCounter}
            /> */}

            <DatePicker
              // className={Classes.ELEVATION_1}
              onChange={this.handleDateChange}
            />

            {/* <DateRangePicker
              className={Classes.ELEVATION_1}
              maxDate={maxDate}
              minDate={minDate}
              onChange={this.handleDateChange}
            /> */}

            {/* <Dropdown
              placeholder="Select Mode"
              selection="selection"
              onChange={this.handleSwitchMode}
              optionsball2={modeOptions}
              value={selectedMode}
            /> */}
          </div>{" "}
        </div>{" "}
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
