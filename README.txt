cloud.py
|_templates
      |_ home.html => main page of our browser and this page will let user snap photo and upload photo to predict.
      |_ imageCap.html => this page will show the picture that snaped and show the total price and amount of coin. Also have speak function.
      |_ imageUpload.html => this page will show the total price and amount of coin. Also have speak function of photo that has been upload.
      		
	  imageCap.html and imageUpload.html will show file that user want to predict from home.html and show the latest picture in "static" folder. 
		|_ coin_photo => foder that will collect all of picture that user snap and upload for predict.
		|_ capture45.js => draw picture that user snap on home.html on canvas and save pictureURL of base64 to .png file. 
|_Camera roll
	|_ croupInput => pictures that has been crop for prepareing these pictures to chack with google cloud.