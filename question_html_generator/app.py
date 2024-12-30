from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

# Function to generate HTML content
def generate_html(session_name, topic_title,total_questions, question_number, question_stem, options, correct_answer):
    # Mapping from index to alphabet letter
    option_mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    # Get the corresponding alphabet letter for the correct answer
    correct_answer_letter = option_mapping.get(correct_answer)
    question_number = int(question_number)
    total_questions = int(total_questions)
    
    # Check if it's the first or last question
    is_first_question = (question_number == 1)
    is_last_question = (question_number == total_questions)

    # Disable buttons based on the question number
    prev_button_disabled = 'disabled' if is_first_question else ''
    next_button_disabled = 'disabled' if is_last_question else ''
    # Constructing the feedback message dynamically

    html_template = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="generator" content="CoffeeCup HTML Editor (www.coffeecup.com)">
    <meta name="dcterms.created" content="Wed, 29 Oct 2014 09:19:03 GMT">
    <meta name="description" content="">
    <meta name="keywords" content="">
    <title></title>
    
   <!-- Including the javascript to disable right-click in browser-->
	<link rel="stylesheet" href="Style.css">
	<!-- Including the stylesheet-->
	<script src="disablerightclick.js" type="text/javascript">
	</script>
    <script>
    function buttonEnable() {{
       document.getElementById('submit').disabled=false;
    }}

    function isOneChecked() {{
        var chx = document.getElementsByTagName('input');
        if (chx[{correct_answer}].type == 'radio' && chx[{correct_answer}].checked) {{
            document.getElementById('fontcolor').color="green";
            document.getElementById('message').innerHTML="Yes, that's correct.";
            document.getElementById('answer').src="Images/CorrectSmiley.jpg";
            document.getElementById('answer').style.height='30px';
            document.getElementById('answer').style.width='30px';
            document.getElementById('submit').disabled=true;
            document.getElementById('A').disabled=true; document.getElementById('B').disabled=true;
            document.getElementById('C').disabled=true; document.getElementById('D').disabled=true;
            document.getElementById('divans').className="correctans";
        }} else {{
            document.getElementById('fontcolor').color="red";
            document.getElementById('message').innerHTML="No, that's incorrect. The correct selection is: ({correct_answer_letter}).";
            document.getElementById('answer').src="Images/IncorrectSmiley.jpg";
            document.getElementById('answer').style.height='30px';
            document.getElementById('answer').style.width='30px';
            document.getElementById('submit').disabled=true;
            document.getElementById('A').disabled=true; document.getElementById('B').disabled=true;
            document.getElementById('C').disabled=true; document.getElementById('D').disabled=true;
            document.getElementById('divans').className='incorrectans';
        }}
        return false;
    }}
    </script>
  </head>
  
  <body>
<center>
<!--Add the Book Name here -->
 <b><font face="Calibri" color="#111C9E" size="6">DOTS Dynamics - Exploring Advanced Concepts in Unity DOTS </font></b> <br/><br/>
 <!-- outer table -->
  <table style="width:1000px; height:600px; box-shadow: 2px 2px 2px #111C9E; border-radius:10px; background-color:#FFFFFF">
  <!-- first row of outer table.-->
  <tr><td style="vertical-align:top; text-align:left;">
  <font face="Calibri" color="#000000" size="3">
  <!-- Add Session Name >> Topic Name here-->
  <b>{session_name} >> {topic_title}</b>
  </font>
  <hr/>
  </td></tr>
  <!-- second row of outer table-->
  <tr><td style="vertical-align:top; text-align:left;">
  <center>
  <!--inner table 1-->
  <table style="width:880px; height:400px; box-shadow: 2px 2px 2px #9E4211; border-radius:10px; background-color:#FFFFFF">
  <!-- first row of inner table 1-->
  <tr><td style="vertical-align:top; text-align:left;">
  <img src="Images/QIcon.jpg" alt="Online Varsity" height="55" width="55">
  <b><font face="Verdana" color="#000000" size="5"> Knowledge Check </font></b><br/><br/>
  <hr/>
  </td></tr>
  <!-- second row of inner table 1-->
  <tr><td style="vertical-align:top; text-align:left;">
   <!-- Add the question number and question stem here-->
 Q{question_number}. {question_stem}
  <br/><br/>
  <font color="green">Select an option and then click <b>Submit</b>. </font>
  <br/> <br/>
 
  <!-- inner table2-->
  <table class="inner2">
  <tr><td>(A)</td>
  <td> <!-- Add the first option here-->
  {options[0]}        
  </td>
    <td> <input type = "radio" name = "answer" id = "A" value = "A" onchange="buttonEnable()" /> <br/> </td>
  </tr>
  <tr ><td >(B)</td>
  <td><!-- Add the second option here-->
  {options[1]}        
        </td>
  <td><input type = "radio" name = "answer" id = "B" value = "B" onchange="buttonEnable()" /> <br/></td>
  </tr>
  <tr ><td >(C)</td>
  <td> <!-- Add the third option here-->
  {options[2]}        
      </td>
   <td><input type = "radio" name = "answer" id = "C" value = "C" onchange="buttonEnable()" /> <br/></td>
  </tr>
  <tr ><td >(D)</td>
  <td> <!-- Add the fourth option here-->
  {options[3]}        
      </td>
   <td><input type = "radio" name = "answer" id = "D" value = "D"  onchange="buttonEnable()"/></td>
  </tr>
  </table>
   </td></tr>
   
   <!-- third row of inner table 1-->
   <tr><td style="text-align:left;">
  <br/> 
  <button id="submit" name="Submit" style="background-color:#F5A9A9; width:75px; height:25px; font:bold 13px Verdana; border:0px solid; border-radius:5px; box-shadow: 2px 2px 2px #9E4211;" onclick="isOneChecked()" disabled><b>Submit</b></button>
  <br/><br/>
  <div id="divans" style="height:40px; width:length;" >
  &nbsp;<img id="answer" src=""/>
  <font id="fontcolor" color="#FF0000"><b><span id="message" /></b> </p></font>
  </div>
  <br/>
  </td></tr>
   
  <tr> <td> <!-- Specify the question number and total questions here-->
  <div style="float: left; width:80px; text-align:center"> <b>{question_number} of {total_questions}</b></div>
   <div style="float: right; width:70px">
   <!-- Specify the next question page name here. In case there is no next page, set the disabled property-->
  <form action="Q{int(question_number)+1}.html"> <button id="next" name="Next" style="background-color:#A6AEE4; width:length;" {next_button_disabled}><b>Next</b></button> </form>
  </div>
  
  <div style="float: right; width:70px;">
  <!-- Specify the previous question page name here. In case there is no previous page, set the disabled property-->
  <form action="Q{int(question_number)-1}.html"> <button id="prev" name="Prev" style="background-color:#A6AEE4; width:length;" {prev_button_disabled}><b>Prev</b></button> </form>
  </div>
   
 
  <br/>
  </td> </tr>
  </table>
   
  </center>
  
 <!-- closing of outer table-->

  <br/><br/>
 
  </table>
  </center>
  </body>
</html>
"""
    file_name = f"Q{question_number}.html"
    with open(file_name, "w") as file:
        file.write(html_template)
    
    return file_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    book_name = request.form['book_name']
    session_name = request.form['session_name']
    topic_title = request.form['topic_title']
    total_questions= request.form['total_questions']
    question_number = request.form['question_number']
    question_stem = request.form['question_stem']
    options = [request.form[f'option_{i}'] for i in range(1, 5)]
    correct_answer = int(request.form['correct_answer']) - 1  # Zero-based index for options
    
    generated_file = generate_html(session_name, topic_title, total_questions, question_number, question_stem, options, correct_answer)
    
    return send_file(generated_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
