# FaceRecognitionSystem
Install requirements.txt<br><br>
<code>pip install -r requirements.txt</code><br>
<br>Install dlib if not installed correctly by above <code>requirements.txt</code> file.
<br><h2>Installing DLIB library.</h2><br>Download the given dlib wheel file above and run the command. <code>pip install dlib-19.19.0-cp37-cp37m-win_amd64.whl</code>
<!--<strong> OR</strong>
Visit <a href src="https://pypi.org/simple/dlib/"> pypi </a>& download the dlib version of your choice in my case-> <b>(dlib-19.19.0-cp37-cp37m-win_amd64.whl)</b><br>
-->
This will successfully install the dlib library.<br>
<h2>Sample Imaging</h2>
Include the images of the students and rename them accordingly.<br>
<ol>
  <li>Name1</li>
  <li>Name2</li>
  <li>Name3</li>
</ol><br>
Run the <code>python face-recog.py</code> & attendance will be marked for every student once a day. No duplicates will be recorded for a day.<br><br>Sample output of the <code>attendance.csv</code><br>![image](https://user-images.githubusercontent.com/72505269/146650764-0efd71c7-f3b3-4f64-ada6-fa8677ecb530.png)
