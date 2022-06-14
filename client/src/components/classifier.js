import React from 'react';
import { useState } from 'react';


const Classifier = (props) => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [errorText, setErrorText] = useState(null);

    const onClassifyImage = async (selectedImage) => {
        if (selectedImage !== null) {
            //If file selected then create FormData
            const data = new FormData();
            data.append('file', selectedImage);
            let res = await fetch(
                'http://127.0.0.1:8000/',
                {
                    method: 'POST',
                    body: data,
                    headers: {
                        'Access-Control-Allow-Origin': "*",
                    },
                }
            );
            let responseJson = await res.json();
            if (responseJson.hasOwnProperty('detail')) {
                props.onChangeLabel(null)
                setErrorText(responseJson.detail)
            }
            if (responseJson.hasOwnProperty('label')) {
                props.onChangeLabel(responseJson.label)
                setErrorText(null)
            }
        } else {
            //if no file selected the show alert
            setErrorText("No image selected")
        }
    }
    return (
        <>

            <div className="p-3 mx-auto border mt-5" style={{ "height": "85%", "width": "100%" }}>
                {selectedImage && (
                    <img alt="not fount" className='w-100' src={URL.createObjectURL(selectedImage)} />
                )}
            </div>
            <div className="mt-4">
                <input type="file" name="myImage"
                    onChange={(event) => {
                        setSelectedImage(event.target.files[0]);
                    }} />
            </div>
            <button className='btn btn-primary mt-4 btn-lg' onClick={() => onClassifyImage(selectedImage)}> Classify </button>
            {errorText && (
                <p className='text-danger'>{errorText}</p>
            )}
        </>
    );
}

export default Classifier;
