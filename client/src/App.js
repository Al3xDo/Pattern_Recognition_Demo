import React from 'react';
import { useState } from 'react';
import './App.css';
import Classifier from './components/classifier';
import Header from './components/header';
import Information from './components/information';
import noImage from "./asset/image/noImage.jpg"


function App() {
  const [label, setLabel] = useState(null)
  var initData = {
    text: 'No Description',
    url_1: noImage,
    url_2: noImage,
    link: '#',
  }
  const [data, setData] = useState(
    initData
  )

  const onChangeLabel = (newLabel, newData = initData) => {
    setLabel(newLabel)
    setData({ ...newData })
  }
  return (
    <div className="App">
      <Header />
      <div className="container-lg">
        <div className="row">
          <div className="col-7">
            <Classifier onChangeLabel={onChangeLabel} />
          </div>
          <div className="col-5">
            <Information label={label} url1={data.url_1} link={data.link} text={data.text} url2={data.url_2} />
          </div>

        </div>
      </div>
    </div>
  );
}

export default App;
