import React from 'react';
import Slider from 'rc-slider';

class RightSlider extends React.Component {
  render() {
    return (
      <div className="rc-slider-right">
        <Slider
          min={0}
          max={255}
          vertical 
          onChange={this.props.onChange}
          value={this.props.value}
        />
      </div>
    );
  }
}

export default RightSlider;
