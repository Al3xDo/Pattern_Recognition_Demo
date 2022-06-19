import React from 'react';
const Information = (props) => {
    const { label, text, url1, url2, link } = props

    return (
        <div className='col-12 border mt-5 p-2'>
            <div className="row">
                <h1>Plant: {label}</h1>
            </div>
            <p>Link: <a href={link}>{link}</a></p>
            <h2 >Usage</h2>
            <p>{text}</p>
            <div className="row">
                <h2>Image related</h2>
                <div className="col-6">
                    <img src={url1} className="w-100" alt="" />
                </div>
                <div className="col-6">
                    <img src={url2} className="w-100" alt="" />
                </div>
            </div>

        </div >
    );
}

export default Information;
