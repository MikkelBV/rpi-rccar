import React from 'react';
import Slider from 'rc-slider';

class LeftSlider extends React.Component {
  render() {
    return (
      <div className="rc-slider-left">
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

export default LeftSlider;
