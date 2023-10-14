# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:15:06 2023

@author: OWNER
"""

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

     <!-- Main Input For Receiving Query to our ML -->
    <form action="{{ url_for('predict')}}"method="post">
    	<br>
    <label for="Age">Age</label>
    <select id="Age" name="Age">
    <br>
      <option value="0">15-18</option>
      <option value="1">19-21</option>
      <option value="2">21-24</option>
      <option value="3">24-27</option>
      <option value="4">27-30</option>
    </select>
    <br>
    <br>
    <label for="Sex">Sex</label>
    <select id="Sex" name="Sex">
    <br>
      <option value="0">Female</option>
      <option value="1">Male</option>
    </select>
    <br>
    <br>
    <label for="Faculty">Faculty</label>
    <select id="Faculty" name="Faculty">
    <br>
      <option value="0">Art</option>
      <option value="1">Education</option>
      <option value="2">Management Science</option>
      <option value="3">Science</option>
      <option value="4">Social Science</option>
    </select>
    <br>
       <br>
   <label for="Year of Study">Year of Study</label>
   <select id="Year of Study" name="Year of Study">
   <br>
     <option value="0">100</option>
     <option value="1">200</option>
     <option value="2">300</option>
     <option value="3">400</option>
   </select>
   <br>
   <br>
    <label for="CGPA">CGPA</label>
    <select id="CGPA" name="CGPA">
    <br>
      <option value="0">1.50-2.39</option>
      <option value="1">2.40-3.49</option>
      <option value="2">3.50-4.49</option>
      <option value="3">4.50-5.0</option>
    </select>
    <br>
    <br>
    <label for="Marital Status">Marital Status</label>
    <select id="Marital Status" name="Marital Status">
    <br>
      <option value="0">Married</option>
      <option value="1">Single</option>
    </select>
    <br>
    <br>
    <label for="When was the last time you were really happy?">When was the last time you were really happy?</label>
    <select id="When was the last time you were really happy?" name="When was the last time you were really happy?">
    <br>
      <option value="0">Few years ago</option>
      <option value="1">Few days ago</option>
      <option value="2">Few months ago</option>
      <option value="3">Few weeks ago</option>
      <option value="4">I don't remember</option>
    </select>
    <br>
    <br>
    <label for="When was the last time you felt good about yourself?">When was the last time you felt good about yourself?</label>
    <select id="When was the last time you felt good about yourself?" name="When was the last time you felt good about yourself??">
    <br>
      <option value="0">Few years ago</option>
      <option value="1">Few days ago</option>
      <option value="2">Few months ago</option>
      <option value="3">Few weeks ago</option>
      <option value="4">I don't remember</option>
    </select>
    <br>
    <br>
    <label for="When was the last time you had a positive outlook on life?">when was the last time you had a positive outlook on life?</label>
    <select id="when was the last time you had a positive outlook on life?" name=when was the last time you had a positive outlook on life?">
    <br>
      <option value="0">Few years ago</option>
      <option value="1">Few days ago</option>
      <option value="2">Few months ago</option>
      <option value="3">Few weeks ago</option>
      <option value="4">I don't remember</option>
    </select>
    <br>
    <br>
    <label for="During your past semesters how often has your mental health affected your ability to study?">During your past semesters how often has your mental health affected your ability to study?</label>
    <select id="During your past semesters how often has your mental health affected your ability to study?" name=During your past semesters how often has your mental health affected your ability to study?">
    <br>
      <option value="0">Always</option>
      <option value="1">Never</option>
      <option value="2">Often</option>
      <option value="3">Rarely</option>
      <option value="4">Sometimes</option>
    </select>
    <br>
    <br>
    <label for="How is your quality of Sleep?">How is your quality of sleep?</label>
    <select id="How is your quality of sleep?" name=How is your quality of sleep?">
    <br>
      <option value="0">Bad</option>
      <option value="1">Good</option>
      <option value="2">Normal</option>
      <option value="3">Very bad</option>
    </select>
    <br>
    <br>
    <label for="Are you in a relationship?">Are you in a relationship?</label>
    <select id="Are you in a relationship?" name=Are you in a relationship?">
    <br>
      <option value="0">No</option>
      <option value="1">Yes</option>
    </select>
    <br>
    <br>
    <label for="Are you going through a tough emotional situation">Are you going through a tough emotional situation?</label>
    <select id="Are you going through a tough emotional situation?" name=Are you going through a tough emotional situation?">
    <br>
      <option value="0">No</option>
      <option value="1">Yes</option>
    </select>
    <br>
	<br>
    <label for="Are you on any medication?">Are you on any medication?</label>
    <select id="Are you on any medication?" name=Are you on any medication?">
    <br>
      <option value="0">Maybe</option>
      <option value="1">No</option>
      <option value="1">Yes</option>
     </select>
     <br>
     <br>
    <label for="Have you been feeling loved?">Have you been feeling loved?</label>
    <select id="Have you been feeling loved?" name=Have you been feeling loved?">
        <br>
          <option value="0">Maybe</option>
          <option value="1">No</option>
          <option value="1">Yes</option>
        </select>
        <br>
        <br>
        <label for="Have you been feeling Confident">Have you been feeling Confident?</label>
        <select id="Have you been feeling Confident?" name=Have you been feeling Confident?">
        <br>
          <option value="0">Maybe</option>
          <option value="1">No</option>
          <option value="1">Yes</option>
        </select>
        <br>
         <br>
         <label for="Have you been dealing with emotional situations well?">Have you been dealing with emotional situations well?</label>
         <select id="Have you been dealing with emotional situations well?" name=Have you been dealing with emotional situations well?">
         <br>
           <option value="0">Maybe</option>
           <option value="1">No</option>
           <option value="1">Yes</option>
         </select>
         <br>
          <br>
          <label for="Have you been feeling useful?">Have you been feeling useful?</label>
          <select id="Have you been dfeeling useful?" name=Have you been feeling useful?">
          <br>
            <option value="0">Maybe</option>
            <option value="1">No</option>
            <option value="1">Yes</option>
          </select>
          <br>
          
          <br>
          <label for="Do you have problems accomodation?">Do you have problems accomodation?</label>
          <select id="Do you have problems accomodation?" name=Do you have problems accomodation?">
          <br>
            <option value="0">Maybe</option>
            <option value="1">No</option>
            <option value="1">Yes</option>
          </select>
          <br>
          <br>
          <label for="Do you have problems with finances?">Do you have problems with finances?</label>
          <select id="Do you have problems with finances?" name=Do you have problems with finances?">
          <br>
            <option value="0">Maybe</option>
            <option value="1">No</option>
            <option value="1">Yes</option>
          </select>
          <br>
         
        <br>
        <label for="Do you have problems with family?">Do you have problems with family?</label>
        <select id="Do you have problems with family?" name=Do you have problems with family?">
        <br>
          <option value="0">Maybe</option>
          <option value="1">No</option>
          <option value="1">Yes</option>
        </select>
        <br>
         <br>
         <label for="Do you have problems with friends?">Do you have problems with friends?</label>
         <select id="Do you have problems with friends?" name=Do you have problems with friends?">
         <br>
           <option value="0">Maybe</option>
           <option value="1">No</option>
           <option value="1">Yes</option>
         </select>
         <br>
          <br>
          <label for="Do you have problems with studies">Do you have problems with studies?</label>
          <select id="Do you have problems with studies?" name=Do you have problems with studies?">
          <br>
            <option value="0">Maybe</option>
            <option value="1">No</option>
            <option value="1">Yes</option>
          </select>
          <br>
            <br>
            <label for="Do you feel discriminated?">Do you feel discriminated?</label>
            <select id="Do you feel discriminated?" name=Do you feel discriminated?">
            <br>
              <option value="0">Maybe</option>
              <option value="1">No</option>
              <option value="1">Yes</option>
            </select>
            <br>
           
         
		



        <button type="submit" class="btn btn-primary btn-block btn-large">Predict</button>
    </form>

   <br>
   <br>
   {{ prediction_text }}

 </div>


</body>
</html>