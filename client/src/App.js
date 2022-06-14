import React from 'react';
import { useState } from 'react';
import './App.css';
import Classifier from './components/classifier';
import Header from './components/header';
import Information from './components/information';

function App() {
  const [label, setLabel] = useState(null)
  const onChangeLabel = (newLabel) => {
    setLabel(newLabel)
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
            <Information label={label} />
          </div>

        </div>
      </div>
    </div>
  );
}

export default App;
