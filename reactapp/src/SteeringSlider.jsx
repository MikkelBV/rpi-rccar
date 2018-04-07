import React from 'react';
import Slider from 'rc-slider';

class SteeringSlider extends React.Component {
  render() {
    return (
      <div className="rc-slider-steering">
        <Slider
          min={0}
          max={100}
          vertical
          onChange={this.props.onChange}
          value={this.props.value}
        />
      </div>
    );
  }
}

export default SteeringSlider;
