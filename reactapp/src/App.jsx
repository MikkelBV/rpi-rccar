import React from 'react';
import RightSlider from './RightSlider';
import LeftSlider from './LeftSlider';
import MasterSlider from './MasterSlider';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      left: 0,
      right: 0,
      master: 0,
    }
  }
  componentDidMount = () => {
    this.socket = new WebSocket(`ws://${window.location.hostname}:8000`);
  }
  sendDataToServer = () => {
    const { left, right } = this.state;
    const datastr = `${left}:${right}`;
    this.socket.send(datastr);
  }
  onRightChange = (right) => {
    this.setState({ right }, this.sendDataToServer);
  }
  onLeftChange = (left) => {
    this.setState({ left }, this.sendDataToServer);
  }
  onMasterChange = (value) => {
    this.setState({ 
      left: value,
      right: value,
      master: value,
    }, this.sendDataToServer);
  }
  render() {
    return (
      <div className="app">
        <LeftSlider
          value={this.state.left}
          onChange={this.onLeftChange}
        />
        <RightSlider
          value={this.state.right}
          onChange={this.onRightChange}
        />
        <MasterSlider
          master={this.state.master}
          onChange={this.onMasterChange}
        />
      </div>
    );
  }
}

export default App;
