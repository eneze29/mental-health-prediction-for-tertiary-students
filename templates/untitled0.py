

<!DOCTYPE html>
<html >
<!--From https://codepen.io/frytyler/pen/EGdtg-->
<head>
  <meta charset="UTF-8">
  <title>ML API</title>
  <link href='https://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Arimo' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Hind:300' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>
  
</head>

<body>
 <div class="login">
	<h1>Mental Health Prediction</h1>
	<h2> Please Take Note of the Following before filling!</h2>
	<h2> For Age: "0" =15-18, "1"=19-21 , "2" = 21-24, "3" = 24-27, "4" =27-30</h2>
	<h2> For Sex: "0" =Female, "1"=Male, </h2>
	<h2>For Faculty: "0" = Arts, "1" = Education , "2" =Management Science, "3" = Science, "4" = "Social Science"</h2>
	

     <!-- Main Input For Receiving Query to our ML -->
    <form action="{{ url_for('predict')}}"method="post">
    	<input type="text" name="Age" placeholder="Age" required="required" />
        <input type="text" name="Sex" placeholder="Sex" required="required" />
		<input type="text" name="Faculty" placeholder="Faculty" required="required" />
		<input type="text" name="Year of Study" placeholder="Year of Study" required="required" />
		<input type="text" name="CGPA" placeholder="CGPA" required="required" />
        <input type="text" name="Marital Status" placeholder="Marital Status" required="required" />
		<input type="text" name="When was the last time you were really happy?" placeholder="When was the last time you were really happy?" required="required" />
		<input type="text" name="When was the last time you felt good about yourself?" placeholder="When was the last time you felt good about yourself?" required="required" />
		<input type="text" name="when was the last time you had a positive outlook on life?" placeholder="When was the last time you had a positive outlook on life?" required="required" />
        <input type="text" name="During your past semesters how often has your mental health affected your ability to study" placeholder="During your past semesters how often has your mental health affected your ability" required="required" />
		<input type="text" name="How is your quality of sleep?" placeholder="How is your quality of sleep?" required="required" />
		<input type="text" name="Are you in a relationship?" placeholder="Are you in a relationship?" required="required" />
		<input type="text" name="Are you going through a tough emotional situation?" placeholder="Are you going through emotional situation?" required="required" />
        <input type="text" name="Are you on any medication" placeholder="Are you on any medication" required="required" />
		<input type="text" name="Have you been feeling confident?" placeholder="Have you been feeling confident?" required="required" />
		<input type="text" name="Have you been feeling Loved?" placeholder="Have you been feeling Loved?" required="required" />
		<input type="text" name="Have you been dealing with emotional problems well?" placeholder="Have you been dealing with emotional problems well" required="required" />
		<input type="text" name="Have you been feeling useful?" placeholder="Have you been feeling useful?" required="required" />
        <input type="text" name="Do you have problems accomodation?" placeholder="Do you have problems with accomodation?" required="required" />
		<input type="text" name="Do you have problems with Finances?" placeholder="Do you have problems Finances?" required="required" />
		<input type="text" name="Do you have problems with Family?" placeholder="Do you have problems Family?" required="required" />
		<input type="text" name="Do you have problems wiith Friends?" placeholder="Do you have problems with Friends? required="required" />
        <input type="text" name="Do you have problems with workloads?" placeholder="Do you have problems with bullying?" required="required" />
		<input type="text" name="Do you feel discriminated?" placeholder="Do you feel discriminated?" required="required" />

	

        <button type="submit" class="btn btn-primary btn-block btn-large">Predict</button>
    </form>

   <br>
   <br>
   {{ prediction_text }}

 </div>


</body>
</html>