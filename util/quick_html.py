file_name = "index"

### Coursera courses summaried
### https://bulkresizephotos.com/en?quality=0.91&type=width&value=300

the_str = """
name
institute
credential
logo (fa-icon)
type (A or B)
courses (names)


IBM AI Engineering <small> Professional Certificate</small>
IBM
5VNYW898L2X9
<i class="fas fa-flag-checkered"></i>
A
Machine Learning with Python
Scalable Machine Learning on Big Data using Apache Spark
Introduction to Deep Learning & Neural Networks with Keras
Deep Neural Networks with PyTorch
Building Deep Learning Models with TensorFlow
AI Capstone Project with Deep Learning


DeepLearning.AI TensorFlow Developer <small> Professional Certificate</small>
DeepLearning.AI
D3ATD54NQQ74
<i class="far fa-lightbulb"></i>
A
Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning
Convolutional Neural Networks in TensorFlow
Natural Language Processing in TensorFlow
Sequences, Time Series and Prediction


Google Data Analytics <small> Professional Certificate</small>
Google
3B9PVVBSANNS
<i class="fab fa-google"></i>
A
Foundations: Data, Data, Everywhere
Ask Questions to Make Data-Driven Decisions
Prepare Data for Exploration
Process Data from Dirty to Clean
Analyze Data to Answer Questions
Share Data Through the Art of Visualization
Data Analysis with R Programming
Google Data Analytics Capstone: Complete a Case Study


Fundamentals of Parallelism on Intel Architecture
Intel
D3X88XPBDWQC
<i class="fas fa-microchip"></i>
C
Vectorization, OpenMP, Memory Optimization, Clusters and MPI


Advanced Machine Learning on Google Cloud
Google Cloud
H7EKZL2N3BKR
<i class="fab fa-cloudversify"></i>
B
End-to-End Machine Learning with TensorFlow on GCP
Production Machine Learning Systems
Image Understanding with TensorFlow on GCP
Sequence Models for Time Series and Natural Language Processing
Recommendation Systems with TensorFlow on GCP


Machine Learning for Trading
Google Cloud, New York Institute of Finance
ZDZNN7YTWMU4
<i class="fas fa-chart-line"></i>
B
Introduction to Trading, Machine Learning & GCP
Using Machine Learning in Trading and Finance
Reinforcement Learning for Trading Strategies


Machine Learning with TensorFlow on Google Cloud Platform
Google Cloud
X6SMHCN6VM73
<i class="fas fa-layer-group"></i>
B
How Google does Machine Learning
Launching into Machine Learning
Introduction to TensorFlow
Feature Engineering
Art and Science of Machine Learning


Deep Learning
DeepLearning.AI
629H5B983QTX
<i class="fas fa-grip-vertical"></i>
B
Neural Networks and Deep Learning
Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization
Structuring Machine Learning Projects
Convolutional Neural Networks
Sequence Models


Applied Data Science with Python
University of Michigan
FXFS2CDJUK2Q
<i class="fab fa-python"></i>
B
Introduction to Data Science in Python
Applied Plotting, Charting & Data Representation in Python
Applied Machine Learning in Python
Applied Text Mining in Python
Applied Social Network Analysis in Python
"""

generated_html = ""
for the_block in the_str.split("\n\n\n")[1:]:
  fields = the_block.split("\n")
  
  is_active = ' class="active"' if fields[0] == the_str.split("\n")[9] else ""
  the_color = "blue" if fields[4]=="A" else "purple"
  num_courses = len(fields) - 5
  courses_txt = "</li><li>".join(fields[5:]) if len(fields[5:]) else "-"

  generated_html += f"""
  <li{is_active}>
  <div class="collapsible-header">{fields[3]}{fields[0]}<span class="badge {the_color} lighten-5" data-badge-caption="courses">{num_courses}</span></div>
  <div class="collapsible-body row">
    <div class="col s5">
      <img class="materialboxed" width="99%" src="/cv/images/thumbnail/CERTIFICATE_LANDING_PAGE~{fields[2]}.jpg" data-enlarge-image="/cv/images/full/CERTIFICATE_LANDING_PAGE~{fields[2]}.jpeg">
      <p class="center-align">
        tap to enlarge<br/>
        <a target="_blank" href="http://coursera.org/verify/professional-cert/{fields[2]}"><i class="material-icons tiny">open_in_new</i>  Verify</a>
      </p>
    </div>
    <div class="col s7">
       <p>by <i>{fields[1]}</i></p>
       <ul class="browser-default"><li>{courses_txt}</li></ul>
    </div>
  </div>
  </li>
  """

  

### Update the HTML files
  
# take a backup
the_html = open(f"./{file_name}.html", "r")
contents = the_html.read()
the_bak = open(f"./util/{file_name}.bak", "w+")
the_bak.write(contents)
the_bak.close()
the_html.close()

# override the index
the_html = open("./index.html", "w+")
pos1 = contents.find("<!--UTIL FLAG A-->")
pos2 = contents.find("<!--UTIL FLAG A END-->")
the_html.write(contents[:pos1] + "<!--UTIL FLAG A-->\n" + generated_html + contents[pos2:])
the_html.close()
