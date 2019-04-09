#About page
from flask import Flask, request, url_for, Markup, render_template

app = Flask(__name__)

@app.route('/')

def webpage():
    return '''

<html>
    <head>
		<title>About</title>
    </head>
	<body style="font-family:helvetica; background-color:gainsboro;">
	<center>
		<h1>BLCA</h1>
		<h3> <u>B</u>ayesian <u>L</u>owest <u>C</u>ommon <u>A</u>ncestor - A Web-Based 16s rRNA Classifier </h3>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

		<div class="topnav" id="myTopnav">
		  <a href="#home" class="active">Home</a>
		  <a href="#tutorial">Tutorial</a>
		  <a href="#contact">Contact</a>
		  <a href="#about">About</a>
		 
		</div>

	</center>
	<style>
	div {
	  text-align: justify;
	  text-justify: inter-word;
	}
	</style>
        <h3> Introduction </h3>
		<div> Microorganism are almost ubiquitous in their varying degree. This poses a challenge of being able to catalogue and classify all known and newly identified organism into an organized or taxonomic system for ease of study and use. In times past, microbiologists were able to achieve this classification by merely studying microbial morphological representation and reactions to coloring technique. However, with molecular studies in genetic materials of living organisms, it was observed that the 16s subunit of the ribosomal RNA sequence are unique and conserved across bacteria with little variations enough to distinguish each bacterium from another. Simply put, 16srRNA from bacteria A is compared against other know bacteria 16srRNAs and classified based on percent similarity between the sequences. As such, molecular microbiologists now advanced to using this 16s rRNA to identify and taxonomically classify bacteria. Subsequently, many software tools have been developed that will leverage on the marker sequence (16s rRNA) to classify bacteria. However, most of these tools lack species-level classification power as they are only able to classify to genus level. Even some current tools that classify further to species level suffer limitations; Firstly, by using nucleotide k-mer frequency to measure similarity between query and database sequence thereby wrongly assuming that these k-mer sequence are independent and that their position in the DNA are not important. Secondly by lacking a solid probabilistic-based criterion on which to base the confidence of the taxonomic assignment results.</div>
		<p><div> To this end, the Bayesian Lowest Common Ancestor (BLCA) was developed to tackle these limitations and provide probabilistic taxonomic classification to species level with confidence scores!</div></p> 
		<h3> Uses of BLCA... </h3>
	
	</body>
</html>'''
