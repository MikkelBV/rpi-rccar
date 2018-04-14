import React from 'react';
import Slider from 'rc-slider';

class MasterSlider extends React.Component {
  render() {
    return (
      <div className="rc-slider-master">
        <Slider
          min={0}
          max={255}
          vertical 
          onChange={this.props.onChange}
          value={this.props.master}
          handleStyle={{
            backgroundColor: 'grey',
            borderColor: 'grey'
          }}
        />
      </div>
    );
  }
}

export default MasterSlider;