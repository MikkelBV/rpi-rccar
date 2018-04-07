import React from 'react';
import Slider from 'rc-slider';

class ThrottleSlider extends React.Component {
  render() {
    return (
      <div className="rc-slider-throttle">
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

export default ThrottleSlider;
