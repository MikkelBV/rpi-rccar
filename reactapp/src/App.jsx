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
    const datastr = `${255 - left}:${255 - right}`;
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

  handleDrive = () => {
    const url = `http://${window.location.hostname}:8081/drive`;
    fetch(url).catch((error) => console.error(error));
  }

  handleReverse = () => {
    const url = `http://${window.location.hostname}:8081/reverse`;
    fetch(url).catch((error) => console.error(error));
  }

  render() {
    return (
      <div className="app">
        <LeftSlider
          value={this.state.left}
          onChange={this.onLeftChange}
        />
        <div className="gear-selector">
          <button onClick={this.handleDrive}>&#8613;</button>
          <br />
          <button onClick={this.handleReverse}>&#8615;</button>
        </div>
        <MasterSlider
          master={this.state.master}
          onChange={this.onMasterChange}
        />
        <RightSlider
          value={this.state.right}
          onChange={this.onRightChange}
        />
      </div>
    );
  }
}

export default App;
