/**
 * This is a React web application (client side rendering)
 */

const modeOptions = [
  { value: 'mode1', text: 'live mode (last 30 mins)' },
  { value: 'mode2', text: '6/25' }
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
