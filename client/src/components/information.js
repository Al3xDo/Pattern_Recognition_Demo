import React from 'react';
import mock_2 from "../asset/image/mock_2.jpg"
const Information = (props) => {
    const { label } = props
    return (
        <div className='col-12 border mt-5 p-2'>
            <div className="row">
                <h1>Plant: {label}</h1>
            </div>
            <h2 >Usage</h2>
            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.</p>
            <div className="row">
                <h2>Image related</h2>
                <div className="col-6">
                    <img src={mock_2} className="w-100" alt="" />
                </div>
                <div className="col-6">
                    <img src={mock_2} className="w-100" alt="" />
                </div>
            </div>
        </div>
    );
}

export default Information;
