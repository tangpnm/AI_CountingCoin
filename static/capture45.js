var video = document.getElementById('video');


//60130500230 get access to the camera to browser
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.srcObject = stream;
        video.play();
    });
}
// 60130500230 converts canvas from snap on camera of base64 to an image
function convertCanvasToBase64(videoId, resultImgId) {
    let video = document.getElementById(videoId)

    //60130500230 create blank canvas as a buffer for picture that has been snap and draw picture to canvas
    var canvas = document.createElement("canvas")
    canvas.width = 800;
    canvas.height = 600;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height)

    //60130500230 return dataurl base64 to png file 
    let result = canvas.toDataURL("image/png");
    document.getElementById(resultImgId).src = result;
    console.log(result)

    //60130500230 create new image and use image with png file in this image var
    var image = new Image();
    image.src = result;
    document.body.appendChild(image)

    return result
}

//60130500230 save png picture to coin_photo folder
function saveBase64AsFile(base64, fileName) {

    var link = document.createElement("a");

    link.setAttribute("href", base64);
    link.setAttribute("download", fileName);
    link.click();
}