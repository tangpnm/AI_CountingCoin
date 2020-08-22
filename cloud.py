#Counting Coin project
#60130500220 Prangkwan Petcharak
#60130500230 Nichamon Thepnimitkul
#60130500237 Panumas Chuatcha
#60130500243 Prapatsorn Ouisakul
import numpy as np
import random, string, cv2, os
import glob

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
from flask import Flask, request, render_template, send_from_directory
from flask.json import jsonify

#It is the set of flask server import from flask and
#set the path where to join floder with flask server to
#collect the image
#ID: 60130500237
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = COIN_FLODER
COIN_FLODER = os.path.join('static', 'coin_photo')

#@app.route is the set of route to go in website

#"/" means go to localhost and can see the home page by it runs
#html file to show the page. Flask is use function to eun html files
#ID: 60130500237
@app.route("/")
def home():
      return render_template('home.html')

#this function for capture image from the video by run after we press the next in home page
#and this function run by "imageCap.html"
#ID: 60130500237
@app.route("/index")
def upload():

    #this function file the image which is lastest file to save in directory in path
      #ID: 60130500237
    path = 'C:/Users/Nummon/Desktop/countingcoin/static/coin_photo/'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key = os.path.getmtime)
    newest = files[-1]

    #this sentence set the file image go to flask server by send the variable "full_filename"
    #ID: 60130500237
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], newest)
    return render_template("imageCap.html", user_image = full_filename)

#this function for upload the image from lacal directory it's also run after press send button after upload
#the path to go this page is "localhost:.../img" and this function run by "imageUpload.html"
#ID: 60130500237
@app.route("/img", methods=["GET", "POST"])
def uploadImage():

    #we send the path after we upload the image and save it automatically
    #and show the information about the image for upload
      #ID: 60130500237
    target = os.path.join(APP_ROOT, 'static/coin_photo')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
   
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Save it to:", destination)
        upload.save(destination)

    return render_template("imageUpload.html")

#we send the directory when we want to make sure that the image is sent successfully
#you can open this route to check the image which you have to download
#ID: 60130500237
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

#this function use for predict the coin that come from capture or upload the file by this functions
#run when the user click the button process in the "imageCap.html" or "imageUpload.html" and then show the result
#from predict in below the page
#ID: 60130500237
@app.route('/background_process_test')
def background_process_test():

     #this function pull the lastest image which save in "path" floder
      #ID: 60130500237
    path = 'C:/Users/Nummon/Desktop/countingcoin/static/coin_photo/'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key = os.path.getmtime)
    newest = files[-1]

      #we use the cv2 for read the image which from new file in above
    #ID: 60130500237
    fileTest = cv2.imread('C:/Users/Nummon/Desktop/countingcoin/static/coin_photo/' + newest);
    #we use "cv2.cvtColor" for covert the color the image to gray or black/white and then we use "medianBlur" to blur the image
    #these 2 processes use for delete the noise in the image
    #ID: 60130500237
    gray_img = cv2.cvtColor(fileTest, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray_img, 5)

    #this use for draw the circle that it founds in the image
    #ID: 60130500237
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 150, param1 = 143,
                    param2 = 38, minRadius=50, maxRadius=141)
    circles = np.uint16(np.around(circles))

      #after we draw the circle in image we must have radius in circle when we have a circle we crop the image for prepare send this image
    #to check in cloud
    #ID: 60130500237
    count = 0;
    fileNames = []
    for i in circles[0, :]:
        
        #crops
        x = i[0]
        y = i[1]
        radius = i[2]

      #we cropped the image by start use (x, y) and then get the square that cover the coin
        #ID: 60130500237
        xStart = x - radius
        xEnd = x + radius
        yStart = y - radius
        yEnd = y + radius

        #after crop the coin we save the image from crop in "JPG" file in "cropInput" local directory by use "cv2.imwrite" to save the files
        #and count the cropped image that we save in directory
        #ID: 60130500237
        nameOfTest = str(randomString()) + '.jpg'
        cropped = fileTest[yStart:yEnd, xStart:xEnd]
        count = count + 1
        cv2.imwrite("C:/Users/Nummon/Desktop/Camera Roll/cropInput/" + nameOfTest, cropped)
        fileNames.append(nameOfTest)

      #this below calculate the amountMoney and count the number of coin by it runs following by number of image which we croppe in above
        #ID: 60130500230
    amountMoney = 0
    for i in range(len(fileNames)):

          #this link to the google cloud for connecting to predict the coin and this is generated from google cloud and then get the "result" from prediction
          #ID: 60130500230
        if __name__ == '__main__':
            file_path = "C:/Users/Nummon/Desktop/Camera Roll/cropInput/" + fileNames[i]
            project_id = "239243118815"
            model_id = "ICN2264875205962760192"
        with open(file_path, 'rb') as ff:
            content = ff.read()
        result = get_prediction(content, project_id, model_id)

      #we calculate the amount of money by check the result from google cloud
        #If result of class name matches with any text will add the "amountMoney"
        #ID: 60130500230
        if result[0]['name'] == "1front":
            amountMoney += 1
        elif result[0]['name'] == "1back":
            amountMoney += 1
        elif result[0]['name'] == "2front":
            amountMoney += 2
        elif result[0]['name'] == "2back":
            amountMoney += 2
        elif result[0]['name'] == "5front":
            amountMoney += 5
        elif result[0]['name'] == "5back":
            amountMoney += 5
        elif result[0]['name'] == "10front":
            amountMoney += 10
        elif result[0]['name'] == "10back":
            amountMoney += 10
        else:
            amountMoney += 0
            
      #we convert the integer variable change to the string variable for prepare print the result and then send the result by send it "JSON function"
            #ID: 60130500230
    numCount = str(count)
    numPrice = str(amountMoney)
    return jsonify({ 'price': numPrice, 'count': numCount })

#This function is random string whenever we want name to save the image
#ID: 60130500237
def randomString(StringLength = 10):
      letters = string.ascii_lowercase
      return ''.join(random.choice(letters) for i in range(StringLength))

#This function is for google cloud when we get result from google cloud we get the type in google cloud type
#so we must convert the type from google into the string type
#ID: 60130500237
def get_prediction(content, project_id, model_id):

      #check the result that it match with project id and model id
      #ID: 60130500237
  prediction_client = automl_v1beta1.PredictionServiceClient()
  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  response = prediction_client.predict(name, payload, params)
  predResults = []
  for result in response.payload:
      name = result.display_name
      score = result.classification.score
      predResults.append({ 'name': name, 'score': score })     
  return predResults

#this is for flask to run in server by run in localhost
#ID: 60130500237
if __name__ == "__main__":
      app.run(debug=True)
