/**
 * This is a React web application (client side rendering)
 */

/**
tag of drop down manual
*/
const modeOptions = [
  { value: 'mode1', text: 'random number' },
  { value: 'mode2', text: '4 hour' },
  { value: 'mode3', text: '12 hour' },
  { value: 'mode4', text: '1 day' },
  { value: 'mode5', text: '7 days' },
  { value: 'mode6', text: '10 days' }
];

const Dropdown = semanticUIReact.Dropdown;

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      selectedMode: null,
    };
  }

  handleSwitchMode = (e, obj) => {
    const { value } = obj;

    console.log('switch file:', value);

    this.setState({ selectedMode: value });

    if (value === "mode1") {
      // reload mode1 html
      window.location.href = "http://127.0.0.1:8000/chart/mode1"
    } else if (value === "mode2") {
      // reload mode2 html
      window.location.href = "http://127.0.0.1:8000/chart/mode2"
    } else if (value === "mode3") {
      // reload mode3 html
      window.location.href = "http://127.0.0.1:8000/chart/mode3"
    } else if (value === "mode4") {
      // reload mode4 html
      window.location.href = "http://127.0.0.1:8000/chart/mode4"
    } else if (value === "mode5") {
      // reload mode5 html
      window.location.href = "http://127.0.0.1:8000/chart/mode5"
    } else if (value === "mode6") {
      // reload mode6 html
      window.location.href = "http://127.0.0.1:8000/chart/mode6"
    }
  }

  render() {
    const { selectedMode } = this.state;
    return (<div>
      Custom2 menus part by using Reactjs, when users choose different menus, a different chart url request will be sent
      <div>
        <div>
          <Dropdown
            placeholder="Select Mode"
            selection="selection"
            onChange={this.handleSwitchMode}
            options={modeOptions}
            value={selectedMode}
          />
        </div>
      </div>
    </div>);
  }
}

ReactDOM.render(<App/>, document.getElementById('app'));
