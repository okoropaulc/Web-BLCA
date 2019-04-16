#HTML of Flask app
from flask import Flask, request, url_for, Markup, render_template

app = Flask(__name__)

#Home Page
@app.route('/home')

def home():
    user = {'username': 'Pauls'}
    return '''

<html>
<head>
	<title>Home</title>
</head>
    <body style="font-family:helvetica; background-color:gainsboro;">
	<center>
		<h1>BLCA</h1>
		<h3> <u>B</u>ayesian <u>L</u>owest <u>C</u>ommon <u>A</u>ncestor - A Web-Based 16s rRNA Classifier </h3>
		<div class="topnav" id="myTopnav">
			<a href="home" class="active">Home</a>
			<a href="tutorial">Tutorial</a>
			<a href="about">About</a>
			<a href="contact">Contact</a>
	<hr>
	</center>
	</div>
	
	<h3>Home</h3>
	<h6>This will essentially be ''' + user['username'] + ''' page</h6>
		
    </body>
</html>'''


#Tutorial Page
@app.route('/tutorial')

def tutorial():
    return '''

<html>
<head>
	<title>Tutorial</title>
<style>
	#box1 {
	  box-sizing: content-box;  
	  width: 300px;
	  height: 100px;
	  padding: 10px;  
	  border: 2px solid black;
	}

	#box2 {
	  box-sizing: border-box;
	  width: 300px;
	  height: 100px;
	  padding: 10px;  
	  border: 2px solid black;
	}
	</style>
</head>
	
	<body style="font-family:helvetica; background-color:gainsboro;">
	<center>
		<h1>BLCA</h1>
		<h3> <u>B</u>ayesian <u>L</u>owest <u>C</u>ommon <u>A</u>ncestor - A Web-Based 16s rRNA Classifier </h3>
		<div class="topnav" id="myTopnav">
			<a href="home" class="active">Home</a>
			<a href="tutorial">Tutorial</a>
			<a href="about" class="active">About</a>
			<a href="contact" class="active">Contact</a>
		</div>
	<hr>
	</center>
	
    <h3> Tutorial </h3>
		<p> With the BLCA 
		<p> 1. Enter your sequence by uploading your fasta file </p>
		<p> <u> OR </u> </p>
		<p> 2. Paste in your sequence(s): </p>
		<div id="box1"> Sequences </div>
	
	</body>
</html>'''


#About Page
@app.route('/about')

def about():
    return '''

<html>
    <head>
		<title>About</title>
    </head>
	<body style="font-family:helvetica; background-color:gainsboro;">
	<center>
		<h1>BLCA</h1>
		<h3> <u>B</u>ayesian <u>L</u>owest <u>C</u>ommon <u>A</u>ncestor - A Web-Based 16s rRNA Classifier </h3>
		<center><div class="topnav" id="myTopnav"></center>
			<a href="home" class="active">Home</a>
			<a href="tutorial">Tutorial</a>
			<a href="about">About</a>
			<a href="contact">Contact</a>
		</div>

	<hr>

	</center>
	<style>
	div {
	  text-align: justify;
	  text-justify: inter-word;
	}
	</style>
        <h3> Introduction </h3>
		<div> Microorganism are almost ubiquitous in their varying degree. This poses a challenge of being able to catalogue and classify all known and newly identified organism into an organized or taxonomic system for ease of study and use. In times past, microbiologists were able to achieve this classification by merely studying microbial morphological representation and reactions to coloring technique. However, with molecular studies in genetic materials of living organisms, it was observed that the 16s subunit of the ribosomal RNA sequence are unique and conserved across bacteria with little variations enough to distinguish each bacterium from another.</div>
		<p><div>Simply put, 16srRNA from bacteria A is compared against other known bacteria and classified based on percent similarity between the sequences. As such, molecular microbiologists now advanced to using this 16s rRNA to identify and taxonomically classify bacteria. Subsequently, many software tools have been developed that will leverage on the marker sequence (16s rRNA) to classify bacteria. However, most of these tools lack species-level classification power as they are only able to classify to genus level. Even some current tools that classify further to species level suffer limitations; Firstly, by using nucleotide k-mer frequency to measure similarity between query and database sequence thereby wrongly assuming that these k-mer sequence are independent and that their position in the DNA are not important. Secondly by lacking a solid probabilistic-based criterion on which to base the confidence of the taxonomic assignment results.</div>
		<p><div> To this end, the Bayesian Lowest Common Ancestor (BLCA) was developed to tackle these limitations and provide probabilistic taxonomic classification to species level with confidence scores!</div></p> 

	</body>
</html>'''


#Contact Page
@app.route('/contact')

def contact():
    return '''

<html>
<head>
	<title>Contact</title>
</head>
    <body style="font-family:helvetica; background-color:gainsboro;">
	<center>
		<h1>BLCA</h1>
		<h3> <u>B</u>ayesian <u>L</u>owest <u>C</u>ommon <u>A</u>ncestor - A Web-Based 16s rRNA Classifier </h3>
		<div class="topnav" id="myTopnav">
			<a href="home" class="active">Home</a>
			<a href="tutorial">Tutorial</a>
			<a href="about">About</a>
			<a href="contact" class="active">Contact</a>
		</div>

	<hr>
        <h3> Contact </h3>
		
		<img src="DrDong.jpg" width="500" height="333">
		<p><b> Qunfeng Dong, Ph.D. </b></p>
		<p> Dr. Dong is the Director of the Center for Biomedical Informatics and an associate professor in the Department of Public Health Sciences at the Stritch School of Medicine, Loyola University Chicago. </p>
		<p> <b>Phone:</b> (708) 327-9004 </p>
		<p><strong>Email:</strong>&nbsp;<a href="mailto:qdong@luc.edu">qdong@luc.edu</a></p>
		<p> <b>Research focus:</b> Bioinformatics </p>
		<p> <b>Research topics:</b> data analysis, genomic/metagenomic computational tool development, mining EMRs</p>
		
		<img src="Eddi.jpg" width="500" height="333">
		<p><b> Eddi Lin </b></p>
		<p> Huaiying (Eddi) Lin, MS </p>
		<p> <b>Phone:</b> (708) 327-9004 </p>
		<p><strong>Email:</strong>&nbsp;<a href="mailto:hlin2@luc.edu">hlin2@luc.edu</a></p>
		<p> <b>Job title:</b> Bioinformatician </p>
	</center>

	</body>
</html>'''
