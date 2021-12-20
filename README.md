# FaceRecognitionSystem
Install requirements.txt<br><br>
<code>pip install -r requirements.txt</code><br>
<br>Install dlib if not installed correctly by above <code>requirements.txt</code> file.
<br><h2>Installing DLIB library.</h2><br>Download the given dlib wheel file above and run the command. <code>pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f</code>
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
Run the <code>python face-recog.py</code> & attendance will be marked for every student once a day. No duplicates will be recorded for a day.<br><br>Sample output of the <code>attendance.csv</code><br>
![image](https://user-images.githubusercontent.com/72505269/146651058-18e51a9a-1c83-4254-9e0e-2199b455e678.png)
