import React from 'react';
import { useState } from 'react';


const Classifier = () => {
    const [selectedImage, setSelectedImage] = useState(null);

    const onClassifyImage = async (selectedImage) => {
        if (selectedImage != null) {
            //If file selected then create FormData
            const fileToUpload = selectedImage;
            const data = new FormData();
            data.append('name', 'Image Upload');
            data.append('file_attachment', fileToUpload);
            let res = await fetch(
                'http://localhost:8000/',
                {
                    method: 'post',
                    body: data,
                    headers: {
                        'Content-Type': 'multipart/form-data; ',
                    },
                }
            );
            let responseJson = await res.json();
            if (responseJson.status === 1) {
                alert('Upload Successful');
            }
        } else {
            //if no file selected the show alert
            alert('Please Select File first');
        }
    }
    return (
        <>

            <div className="w-50 p-3 mx-auto border mt-5" style={{ "height": "600px" }}>
                {selectedImage && (
                    <img alt="not fount" className='w-100' src={URL.createObjectURL(selectedImage)} />
                )}
            </div>
            <div className="mt-4">
                <input type="file" name="myImage"
                    onChange={(event) => {
                        console.log(event.target.files[0]);
                        setSelectedImage(event.target.files[0]);
                    }} />
            </div>
            <button className='btn btn-primary mt-4 btn-lg' onClick={() => onClassifyImage(selectedImage)}> Classify </button>
        </>
    );
}

export default Classifier;
