#!/usr/bin/python
import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from csv import writer
import csv

#Note that MNDPH has been frequently altering their website.
#It is possible that an update will cause errors here and the code
#would need to be edited to address these changes

URL = "https://www.health.state.mn.us/diseases/coronavirus/situation.html"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0'}

page = requests.get(URL, headers = headers)



#testing html block

test_html = """
<!doctype html>
<html lang="en">
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- JAVASCRIPT --> 
<script type="text/javascript" src="/macros/js/jquery.min.js"></script>
<script type="text/javascript" src="/macros/js/bootstrap.js"></script>
<script type="text/javascript" src="/macros/js/banner.js"></script>
<script type="text/javascript">
var $window = $(window);

function checkWidth() {
    if ($window.width() < 600) {
	var el1 = document.getElementById('sidebar_left');
	var el2 = document.getElementById('sidebar_right');
	if (el1 && el2) {
  	while (el2.firstChild) el1.appendChild(el2.firstChild);
	}

	// Remove el2 if required
	el2.parentNode.removeChild(el2);
    };
}

</script>

<!-- CSS STYLES --->
<link rel="stylesheet" type="text/css" href="/macros/css/bootstrap/bootstrap.css" />
<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css" rel="stylesheet">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
<link rel="stylesheet" href="/macros/responsive/styles.css"> 
<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>


</head>
<body onLoad="checkWidth()">
<div id="skiptocontent"><a href="#body" class="skip">Skip to Content</a></div>
<script>
   $( document ).ready(function() {
        $(".skip").click(function(event){   
            var skipTo="#"+this.href.split('#')[1];
            $(skipTo).attr('tabindex', -1).on('blur focusout', function () {
                $(this).removeAttr('tabindex');    
            }).focus();
        });
    });
</script>
<!-- MDH CURRENT BANNER CONTENT --->
<!-- Start Banner Include -->

<!-- Specify MDH main phone numbers for Google Searches; added 3-14-15 --> 
<script type="application/ld+json">
{ "@context" : "http://schema.org",
  "@type" : "Organization",
  "url" : "http://www.health.state.mn.us",
  "contactPoint" : [
    { "@type" : "ContactPoint",
      "telephone" : "+1-888-345-0823",
      "contactType" : "customer service",
      "contactOption" : "TollFree",
      "areaServed" : "US"
    } , {
      "@type" : "ContactPoint",
      "telephone" : "+1-651-201-5000",
      "contactType" : "customer service"
    } ] }
</script>

<!-- MDH BANNER HTML --------------------------------------------------------------------------->
<div id="mdhHeaderDiv">
  <header class="banner"> <a href="/index.html"><img class="bannerImg no_print" src="/images/logo-reverse.png" alt="Department of Health Logo"/></a>
    <img class="bannerImg-small hidden" src="/images/portal-logo-screen_tcm1077-226393.png" alt="Minnesota logo" /><img src="/images/logo_print.png" alt="MDH Logo" width="250" height="37" class="printOnly" />
	
	  
    <div class="title hidden" tabindex=0>Minnesota Department of Health</div>
  
    <div id="navigation">
      <ul id="navbar" class="clearfix">
        <li><a href="/index.html" id="home">HOME</a></li>
        <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" id="topic">TOPICS <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="/data/index.html">Data, Statistics and Legislation</a></li>
            <li><a href="/diseases/index.html">Diseases and Conditions</a></li>
            <li><a href="/facilities/index.html">Health Care Facilities, Providers, and Insurance</a></li>
            <li><a href="/communities/index.html">Healthy Communities, Environment and Workplaces</a></li>
            <li><a href="/people/index.html">Individual and Family Health</a></li>
          </ul>
        </li>
        <li><a href="/about/index.html" id="about">ABOUT US</a></li>
      </ul>

	<div id="searchform">
            <form id="cse-search-box" name="seek" action="https://mn.gov/mdh/search/" onsubmit="return validateSearch(this);">
      <div id="searchbox">
        <label style="position: absolute; left:-1100px" for="q">search input field</label>
        <button type="submit" class="searchbutton"><span class="sr-only">Search</span> </button>
        <input type="text" name="query" placeholder="Search" id="q" size="30" class="searchtext" value="" onfocus="return clearSearchDefault;" 
         />
			   
        
      </div>
      </form>
    </div>         
  </div>	
  </header>
	
	</div>
	
	
	
<!--------------------------------------------------------------------------------------------->

<!-- End Banner Include -->

<!-- Begin Main Content -->

<title>Situation Update for Coronavirus Disease 2019 (COVID-19) - Minnesota Dept. of Health</title>

<!-- Start Dublin Core - Please add content for the Tags in This Block -->

<meta name="DC.Title" content="Situation Update for Coronavirus Disease 2019 (COVID-19) - Minnesota Dept. of Health">
<meta name="DC.Subject" scheme="LIV-MN" content="COVID-19">
<meta name="DC.Subject" scheme="LIV-MN" content="Novel Coronavirus">
<meta name="DC.Subject" scheme="LIV-MN" content="Virus Diseases">
<meta name="DC.Creator.CorporateName" scheme="AACR2" content="Minnesota Dept. of Health">
<meta name="DC.Creator.PersonalName" scheme="AACR2" content="Como-Sabetti, Kathy">
<meta name="DC.Creator.PersonalName" scheme="AACR2" content="Pretzel, Elly">
<meta name="DC.Date.Created" scheme="ISO 8601" content="2020-01-23">
<meta name="DC.Date.Modified" scheme="ISO 8601" content="2020-04-03">
<meta name="DC.Language" scheme="ISO639-1" content="en">
<link rel="schema.dc" href="http://purl.org/metadata/dublin_core_elements">

<!-- End Dublin Core - Please Modify This Block -->
<link rel="stylesheet" href="/macros/responsive/styles.css">
</head>
<body>
<!-- Begin Main Content -->
<div id="container">
	<div id="content" class="clearfix">
		<div id="sidebar_left">


<h2>Coronavirus Disease 2019 (COVID-19)</h2>
<ul>
<li><a href="/diseases/coronavirus/index.html">COVID-19 Home</a></li>
	<li><a href="/diseases/coronavirus/action.html">Strategies to Slow the Spread</a>
<li><a href="/diseases/coronavirus/situation.html">Situation Update</a></li>
<li><a href="/diseases/coronavirus/basics.html">About COVID-19</a></li>
<li><a href="/diseases/coronavirus/prevention.html">Protecting Yourself and Family</a></li>
<li><a href="/diseases/coronavirus/communities.html">Community Settings</a></li>
<li><a href="/diseases/coronavirus/travel.html">Travelers</a></li>
<li><a href="/diseases/coronavirus/hcp/index.html">Health Care</a></li>
<li><a href="/diseases/coronavirus/schools.html">Schools and Child Care</a></li>
<li><a href="/diseases/coronavirus/businesses.html">Businesses and Employers</a></li>
<li><a href="/diseases/coronavirus/responders.html">First Responders</a></li>
<li><a href="/diseases/coronavirus/mdh.html">What MDH is Doing</a></li>
<li><a href="/diseases/coronavirus/materials/index.html">Materials and Resources</a></li>
<li><a href="/diseases/coronavirus/guidance.html">Guidance Library</a></li>
</ul>
<h2>Related Topics</h2>
<ul>
	<li><a href="/communities/ep/behavioral/covid19.html">Behavioral Health and COVID-19</a></li>
	<li><a href="/diseases/respiratory/index.html">Infectious Respiratory Illness</a></li>
</ul>

		</div>
<!---- for mobile menu. Do not edit ---->
<input type="checkbox" id="nav-trigger" class="nav-trigger">
<label for="nav-trigger"></label>
<div class="site-wrap">
		<div id="body">

<h1>Situation Update for Coronavirus Disease 2019 (COVID-19)</h1>
<span class="small"><p class="addthis_toolbox addthis_default_style"><a href="javascript:window.open('http://service.govdelivery.com/service/subscribe.html?code=MNMDH_486', 'Popup','width=700,height=440,toolbar=no,scrollbars=yes,resizable=yes'); void('');" onClick="window.status='Subscribe'; return true" onMouseOver="window.status='Subscribe'; return true" onMouseOut="window.status=''; return true" class="email" alt="Subscribe Coronavirus Disease 2029 (COVID-19) Updates">Subscribe: COVID-19 updates</a> <br>
	Sign up to receive email or mobile alerts when this data is updated, as well as other periodic COVID-19 updates.</p></span>
<p>Data is for cases that were tested and returned positive. Numbers are cumulative since Jan. 20, 2020. All data are preliminary and may change as  cases are investigated. </p>
<p>Not  all suspected cases of COVID-19 are tested, so this data is not representative  of the total number of people in Minnesota who have or had COVID-19.</p>
<p class="small">Updated April 3, 2020 <br>
  Updated daily at 11 a.m., with data current as of 4 p.m. the previous day.
</p>
<h2>Testing</h2>
<p><strong>Total approximate number of completed tests:</strong> 24,227 </p>
<ul>
  <li>Total approximate number of completed tests from the MDH Public Health Lab: 8,682</li>
  <li>Total approximate number of completed tests from external laboratories: 15,545</li>
</ul>

<h2>Minnesota Case Information</h2>
<ul>
  <li><strong>Total positive:</strong> 789
    <ul>
      <li>Patients who no longer need to be isolated: 410</li>
      </ul>
  </li>
  </ul>
<img src="/diseases/coronavirus/statsgraph.png" width="100%" alt="Cumulative total and daily confirmed cases in Minnesota: Date reported, Positive cases, Total Positive:
3/6, 1,	1
3/7, 0, 1
3/8, 1,	2
3/9, 0, 2
3/10, 1, 3
3/11, 2, 5
3/12, 4, 9
3/13, 5, 14
3/14, 7, 21
3/15, 14, 35
3/16, 19, 54
3/17, 6, 60
3/18, 17, 77
3/19, 12, 89
3/20, 26, 115
3/21, 22, 137
3/22, 32, 169
3/23, 66, 235
3/24, 26, 261
3/25, 26, 287
3/26, 59, 346
3/27, 52, 398
3/28, 43, 441
3/29, 62, 503
3/30, 73, 576
3/31, 53, 629
4/1, 60, 689
4/2, 53, 742
4/3, 47, 789
"/>
<h3>Deaths</h3>
<ul>
  <li><strong>Total deaths:</strong> 22</li>
  </ul>
<img src="/diseases/coronavirus/statsdeath.png" width="100%" alt="Deaths of confirmed cases in Minnesota: Date reported, deaths, Total deaths:
3/21, 0, 0
3/22, 1, 1
3/26, 1, 2
3/27, 2, 4
3/28, 1, 5
3/29, 4, 9
3/30, 1, 10
3/31, 2, 12
4/1, 5, 17
4/2, 1, 18
4/3, 4, 22		
"/>
<h3>Hospitalization</h3>
<ul>
  <li><strong>Total cases requiring hospitalization:</strong> 156
    <ul>
      <li>Hospitalized as of today: 86
        <ul>
          <li>Hospitalized in ICU as of today: 40</li>
          </ul>
        </li>
      </ul>
  </li>
  </ul>
<p><img src="/diseases/coronavirus/statshosp.png" width="100%" alt="Minnesota COVID-19 hospitalizations date reported, hospitalized not in ICU, number in ICU, total cumulative hospitalizations, total cumulative in ICU:
3/19, 6, 1, 7, 1
3/20, 3, 2, 7, 2
3/21, 2, 4, 12, 5
3/22, 5, 5, 12, 5
3/23, 7, 5, 21, 5
3/24, 8, 7, 21, 7
3/25, 14, 12, 35, 12
3/26, 18, 13, 41, 13
3/27, 17, 17, 51, 17
3/28, 17, 13, 57, 17
3/29, 23, 16, 75, 24
3/30, 32, 24, 92, 25
3/31, 30, 26, 112, 32
4/1, 27, 27, 122, 40
4/2, 37, 38, 138, 49
4/3, 46, 40, 156, 62		
"/></p>

<h3>Demographics</h3>
<!--<ul>
  <li>Health care workers: </li>
  <li>Worked in or attended school or child care: </li>
</ul>-->
<h4>Age</h4>
<img src="/diseases/coronavirus/statsage.png" width="100%" alt="Age Range for confirmed COVID-19   cases in Minnesota: Age range,	number positive:
0 - 5 years, 3
6 - 19 years, 23
20 - 44 years, 328
45 - 64 years, 263
65+ years, 172
"/>
<table width="100%" border="1">
  <tbody>
    <tr class="table_head_shade">
      <th scope="col">&nbsp;</th>
      <th scope="col">Median Age</th>
      <th scope="col">Age Range</th>
    </tr>
    <tr>
      <th scope="row">All cases</th>
      <td>48</td>
      <td>4 months - 104 years</td>
    </tr>
    <tr>
      <th scope="row">Non-hospitalized cases </th>
      <td>42</td>
      <td>4 months - 104 years</td>
    </tr>
    <tr>
      <th scope="row">Hospitalized cases  </th>
      <td>64</td>
      <td>6 - 98 years</td>
    </tr>
    <tr>
      <th scope="row">Hospitalized cases in ICU</th>
      <td>66</td>
      <td>25 - 95 years</td>
    </tr>
    <tr>
      <th scope="row">Deaths</th>
      <td>84</td>
      <td>58 - 95 years</td>
    </tr>
  </tbody>
</table><br>
<h4>Gender</h4>
<ul>
  <li>51% female, 49% male,  0% other</li>
</ul>
<h3>Likely Exposure</h3>
<img src="/diseases/coronavirus/statsexpo.png" width="100%" alt="Likely exposure for confirmed COVID-19   cases in Minnesota: data in table below.
"/>
<table width="70%" border="1">
  <tbody class="small">
    <tr class="table_head_shade">
      <th scope="col">Likely Exposure</th>
      <th scope="col">Percent of Cases</th>
    </tr>
    <tr>
      <th scope="row">Cruise ship</th>
      <td>3%</td>
    </tr>
    <tr>
      <th scope="row">International travel</th>
      <td>14%</td>
    </tr>
    <tr>
      <th scope="row">Known exposure to a case</th>
      <td>22%</td>
    </tr>
    <tr>
      <th scope="row">Travel to another state <br>
        (with no known exposure)</th>
      <td>19%</td>
    </tr>
    <tr>
      <th scope="row">Community transmission in MN </th>
      <td>32%</td>
    </tr>
    <tr>
      <th scope="row">Unknown/missing</th>
      <td>10%</td>
    </tr>
  </tbody>
</table>
<h3>Cases by County of Residence</h3>
<p>County of residence is confirmed  during the case interview. At the time of this posting not all interviews have  been completed. The data on this map may not  equal the total number of reported positive cases. </p>
<p><iframe width="500" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" title="MN COVID-19 Case Tracking Web Map" src="//mdh.maps.arcgis.com/apps/Embed/index.html?webmap=442e9e2e8b1b4844950935da211b2ed4&extent=-99.0558,44.4889,-87.608,48.3857&zoom=false&previewImage=false&scale=false&legend=true&disable_scroll=false&theme=light"></iframe>
</p>
<table width="70%" border="1">
  <tbody class="small">
    <tr class="table_head_shade">
      <th>County</th>
      <th>Cases</th>
    </tr>
    <tr>
      <td>Anoka</td>
      <td >34</td>
    </tr>
    <tr>
      <td>Beltrami</td>
      <td >4</td>
    </tr>	  
    <tr>
      <td>Benton</td>
      <td >1</td>
    </tr>
    <tr>
      <td>Big Stone</td>
      <td >1</td>
    </tr>
    <tr>
      <td>Blue Earth</td>
      <td >10</td>
    </tr>
    <tr>
      <td>Brown</td>
      <td >2</td>
    </tr>
    <tr>
      <td>Carlton</td>
      <td >5</td>
    </tr>
    <tr>
      <td>Carver</td>
      <td >10</td>
    </tr>
    <tr>
      <td>Cass</td>
      <td >1</td>
    </tr>
    <tr>
      <td>Chisago</td>
      <td >4</td>
    </tr>
    <tr>
      <td>Clay</td>
      <td >8</td>
    </tr>
    <tr>
      <td>Clearwater</td>
      <td >2</td>
    </tr>
    <tr>
      <td>Cottonwood</td>
      <td >5</td>
    </tr>		  
    <tr>
      <td>Crow Wing</td>
      <td >3</td>
    </tr>
    <tr>
      <td>Dakota</td>
      <td >54</td>
    </tr>
    <tr>
      <td>Dodge</td>
      <td >10</td>
    </tr>
    <tr>
      <td>Douglas</td>
      <td >1</td>
    </tr>		  
    <tr>
      <td>Faribault</td>
      <td >3</td>
    </tr>	  
    <tr>
      <td>Fillmore</td>
      <td >9</td>
    </tr>
    <tr>
      <td>Freeborn</td>
      <td >7</td>
    </tr>
    <tr>
      <td>Goodhue</td>
      <td >5</td>
    </tr>
    <tr>
      <td>Hennepin</td>
      <td >242</td>
    </tr>
    <tr>
      <td>Isanti</td>
      <td >2</td>
    </tr>	  
    <tr>
      <td>Itasca</td>
      <td >2</td>
    </tr>
    <tr>
      <td>Jackson</td>
      <td >1</td>
    </tr>		  
    <tr>
      <td>Kandiyohi</td>
      <td >2</td>
    </tr>
    <tr>
      <td>Koochiching</td>
      <td >1</td>
    </tr>
    <tr>
      <td>Lac qui Parle</td>
      <td >1</td>
    </tr>
    <tr>
      <td>Le Sueur</td>
      <td >19</td>
    </tr>
    <tr>
      <td>Lincoln</td>
      <td >1</td>
    </tr>	  
    <tr>
      <td>Lyon</td>
      <td >3</td>
    </tr>
    <tr>
      <td>Mahnomen</td>
      <td >1</td>
    </tr>
    <tr>
      <td>Martin</td>
      <td >32</td>
    </tr>
    <tr>
      <td>Meeker</td>
      <td >1</td>
    </tr>
    <tr>
      <td>Mower</td>
      <td >15</td>
    </tr>
    <tr>
      <td>Nicollet</td>
      <td >3</td>
    </tr>
    <tr>
      <td>Olmsted</td>
      <td >76</td>
    </tr>
    <tr>
      <td>Otter Tail</td>
      <td >1</td>
    </tr>	  
    <tr>
      <td>Ramsey</td>
      <td >71</td>
    </tr>
    <tr>
      <td>Renville</td>
      <td >2</td>
    </tr>
    <tr>
      <td>Rice</td>
      <td >3</td>
    </tr>
    <tr>
      <td>Scott</td>
      <td >11</td>
    </tr>
    <tr>
      <td>Sherburne</td>
      <td >8</td>
    </tr>
    <tr>
      <td>Sibley</td>
      <td >1</td>
    </tr>
    <tr>
      <td>St. Louis</td>
      <td >13</td>
    </tr>
    <tr>
      <td>Stearns</td>
      <td >5</td>
    </tr>
    <tr>
      <td>Steele</td>
      <td >6</td>
    </tr>
    <tr>
      <td>Traverse</td>
      <td >2</td>
    </tr>
    <tr>
      <td>Wabasha</td>
      <td >6</td>
    </tr>
    <tr>
      <td>Waseca</td>
      <td >3</td>
    </tr>
    <tr>
      <td>Washington</td>
      <td >51</td>
    </tr>
    <tr>
      <td>Watonwan</td>
      <td >3</td>
    </tr>
    <tr>
      <td>Wilkin</td>
      <td >2</td>
    </tr>
    <tr>
      <td>Winona</td>
      <td >11</td>
    </tr>
    <tr>
      <td>Wright</td>
      <td >7</td>
    </tr>
    <tr>
      <td>Yellow Medicine</td>
      <td >1</td>
    </tr>
    </tbody>
</table>
<p class="small">We will not release specific locations for any patients being tested in order to protect patient privacy. </p>
<p class="small">Choosing a county on the interactive map above will provide the case count, the legend is  located in the upper left. This map will not work if your browser is in compatibility mode.</p>
<h3 class="small">Residence Type</h3>
<p><img src="/diseases/coronavirus/statsres.png" width="100%" alt="Residence type for confirmed COVID-19   cases in Minnesota: data in table below.
"/></p>
<table width="70%" border="1">
  <tbody class="small">
    <tr class="table_head_shade">
      <th scope="col">Residence Type</th>
      <th scope="col">Percent of Cases</th>
    </tr>
    <tr>
      <th scope="row">Private residence
</th>
      <td>82%</td>
    </tr>
    <tr>
      <th scope="row">Long-term care facility</th>
      <td>3%</td>
    </tr>
    <tr>
      <th scope="row">Long-term acute living</th>
      <td>&lt;1%</td>
    </tr>
    <tr>
      <th scope="row">Assisted living</th>
      <td>2%</td>
    </tr>
    <tr>
      <th scope="row">Homeless shelter</th>
      <td>&lt;1%</td>
    </tr>
    <tr>
      <th scope="row">Jail/prison</th>
      <td>0</td>
    </tr>
    <tr>
      <th scope="row">College dorm</th>
      <td>0</td>
    </tr>
    <tr>
      <th scope="row">Other</th>
      <td>1%</td>
    </tr>
    <tr>
      <th scope="row">Unknown/missing</th>
      <td>11%</td>
    </tr>
  </tbody>
</table>
<!--<h4>Long-term Care Facilities with Outreaks, by County</h4>-->
<hr>

<p><a href="https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html">CDC: Coronavirus Disease 2019 (COVID-19) Cases in the U.S.</a>.</p>
</div>
  <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=mnhealth" async="async"></script>
  <div id="sidebar_right">
			<ul id="socialMedia">
				<li class="addthis_toolbox addthis_default_style"><a href="http://www.addthis.com/bookmark.php?v=250&amp;pub=mnhealth" class="addthis_button share">Share This</a>
				</li><br />				
	  			<li class="addthis_toolbox addthis_default_style"><a href="javascript:window.open('http://service.govdelivery.com/service/subscribe.html?code=MNMDH_486', 'Popup','width=700,height=440,toolbar=no,scrollbars=yes,resizable=yes'); void('');" onClick="window.status='Subscribe'; return true" onMouseOver="window.status='Subscribe'; return true" onMouseOut="window.status=''; return true" class="email" alt="Subscribe Coronavirus Disease 2029 (COVID-19) Updates">Subscribe: COVID-19 updates</a> </li>
			</ul>	
<!--Begin text area: you can modify -->
	  <p><a href="/diseases/coronavirus/materials/hmong.html">2019 Novel Coronavirus</a>
        <br>(Hmong) 
    <p><a href="/diseases/coronavirus/materials/somali.html">Koronafayraska Cusub ee 2019</a><br>
  (Somali)
</p>
<p><a href="/diseases/coronavirus/materials/spanish.html">Enfermedad del Coronavirus 2019 (COVID-19)</a><br>
  (Spanish)
</p>
	  <p><a href="/diseases/coronavirus/materials/asl.html">American Sign Language (ASL) Videos</a></p>
	  <hr>

<h2>COVID-19 Hotlines:</h2>
<p>Interpreters available</p>
<p><strong>Health  questions:</strong><br />
651-201-3920 or 1-800-657-3903<br />
7 a.m. to 7 p.m.</p>
<p><strong>Schools and child care questions:</strong><br>
  651-297-1304 or 1-800-657-3504<br>
  7 a.m. to 7 p.m.
</p>
<hr>
<h2 class="small">Contact us:</h2>
<p class="small">If you have questions or comments about this page, use our <a href="https://survey.vovici.com/se/56206EE321296199">IDEPC Comment Form</a> or call 651-201-5414 for the MDH <a href="/about/org/idepc/index.html"> Infectious Disease Epidemiology, Prevention and Control Division</a>.</p>
  </div>
	</div>
</div>
      <footer>
<!-- close content --></div></div>
<!-- Begin Footer Include -->
<div id="footer">
	<div id="footerContainer">
		<div class="footerTopics">
			<ul class="clearfix">
				<li><a href="/people/index.html">Individual &amp; Family Health</a></li>
				<li><a href="/facilities/index.html">Health Care Facilities, Providers <br>
&amp; Insurance</a></li>
				<li><a href="/data/index.html">Data, Statistics and Legislation</a></li>
                <li><a href="/diseases/index.html">Diseases &amp; Conditions</a></li>
                <li><a href="/communities/index.html">Healthy Communities, Environment <br>
              &amp; Workplaces</a></li>
                <li><a href="/about/index.html">About MDH</a></li>
                <li><a href="/about/locations/index.html">Locations &#38; Directions</a></li>
                <li><a href="/forms/feedback/mail.html">Comments &#38; Questions</a></li>
                <li><a href="/about/privacy.html">Privacy Statement &amp; Disclaimer</a></li>
                <li><a href="/about/equalopp.html">Equal Opportunity</a>		</li>
			</ul>
		</div>
      <div class="footerTopics"> 
      <p>651-201-5000 Phone<br />
				888-345-0823 Toll-free</p>
			<p>Information on this website is available in alternative formats upon request. </p>
		<p style="text-align:center; overflow:hidden"><a href="https://mn.gov/portal/" onClick="return OuttaHere(); return false;"><img src="https://mn.gov/portal/assets/mn.logo.footer_tcm1077-65019.png" alt="Minnesota.gov" /></a></p><p style="text-align:center"><a href=			"https://www.phaboard.org/"><img src="/images/phabseal.png"  width="125" height="125" alt="Public Health Accreditation Board" /></a></p>
	  </div>
	</div>
</div>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-20272425-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

<script type="text/javascript">
/*<![CDATA[*/
(function() {
var sz = document.createElement('script'); sz.type = 'text/javascript'; sz.async = true;
sz.src = '//siteimproveanalytics.com/js/siteanalyze_6486.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sz, s);
})();
/*]]>*/
</script>

<script>
$(document).ready(function() {
	if(document.URL.indexOf("health.state.mn.us/macros/topics/orginfo.html") != -1) {
		$("#about").addClass("activeBanner");
	}
	else if(document.URL.indexOf("health.state.mn.us/index.html") != -1) {
		$("#home").addClass("activeBanner");
	}

});
</script>
</footer>

<p>Updated Friday, 03-Apr-2020 10:35:43 CDT </p>
</body>
</html>
"""

#test = open("covid.html", 'r')
#page = requests.get(test, headers = headers) 
#print(test)

#when debugging replace page.text with html var above
soup = BeautifulSoup(page.text, 'html.parser')

#soup = BeautifulSoup(test_html, 'html.parser')

#title = soup.find()

#print(soup.prettify())
#x = soup.find_all('li')[3].get_text()

#print(x)



for item in soup.select('p'):
	#get_text() converts html to str
	if item.get_text().startswith("Updated") and item.get_text().endswith("CDT "):
		web_timestamp = re.findall(r'\d+[-]\w+[-]\d+', item.get_text())
		web_timestamp = web_timestamp[0]
		#print(web_timestamp)	
	if item.get_text().startswith("Total approximate number of completed tests:"):
		#this does quite a bit basically grabs only the number, removes whitespace and commas, converts to int
		tot_tested = int(item.get_text().split(":")[-1].strip().replace(',', ''))
		#print(tot_tested)



for item in soup.select('li'):
	#These if statements needed more logic due to the html format
	if item.get_text().startswith("Total positive:"):
		len_list = len(item.get_text().split(":"))
		split_list = re.split(r'[:\n]\s*', item.get_text())
		if len_list > 2:
			del split_list[-1]
		tot_pos = split_list[1].strip().replace(',', '')
		#print(tot_pos)
	if item.get_text().startswith("Total deaths:"):
		len_list = len(item.get_text().split(":"))
		split_list = re.split(r'[:\n]\s*', item.get_text())
		if len_list > 2:
			del split_list[-1]
		deaths = split_list[1].strip().replace(',', '')
		#print(deaths)
	if item.get_text().startswith("Patients who no longer need to be isolated:"):
		len_list = len(item.get_text().split(":"))
		split_list = re.split(r'[:\n]\s*', item.get_text())
		if len_list > 2:
			del split_list[-1]
		recovered = split_list[1].strip().replace(',', '')
		#print("recovered = " + str(recovered))
	if item.get_text().startswith("Total cases requiring hospitalization:"):
		len_list = len(item.get_text().split(":"))
		split_list = re.split(r'[:\n]\s*', item.get_text())
		if len_list > 2:
			del split_list[-1]
		tot_hosp = split_list[1].strip().replace(',', '')
		#print(tot_hosp)
	if item.get_text().startswith("Hospitalized as of today:"):
		len_list = len(item.get_text().split(":"))
		split_list = re.split(r'[:\n]\s*', item.get_text())
		if len_list > 2:
			del split_list[-1]
		curr_hosp = split_list[1].strip().replace(',', '')
		#print(curr_hosp)
	if item.get_text().startswith("Hospitalized in ICU as of today:"):
		len_list = len(item.get_text().split(":"))
		split_list = re.split(r'[:\n]\s*', item.get_text())
		if len_list > 2:
			del split_list[-1]
		ICU = split_list[1].strip().replace(',', '')
		#print(ICU)

curr_date = (str(datetime.today())[0:10])
web_data_date = datetime.strptime(web_timestamp, '%d-%b-%Y').strftime('%Y-%m-%d')
#print(web_data_date)
#need logic gate to check date before running program

#collect last recorded timepoint
with open('mn_covid_19.txt', 'r') as csv_file:
	reader = csv.reader(csv_file, delimiter = '\t')
	rows = list(reader)
	last_row = rows[-1]
	last_rec_data = last_row[0]
	#print(last_rec_data)

#logic for data collection and user msgs
if curr_date == web_data_date and curr_date != last_rec_data and web_data_date != last_rec_data:
	with open('mn_covid_19.txt', 'a') as csv_file:
		#csv_file.write('\n')
		csv_writer = writer(csv_file, delimiter='\t')
		csv_writer.writerow([curr_date, tot_tested, tot_pos, deaths, tot_hosp, curr_hosp, recovered, ICU])
	print("Data collected on " + web_data_date +" has been appended to mn_covid_19.txt")
elif curr_date != web_data_date and last_rec_data == web_data_date:
	print("MNDPH has not updated their data or an error has occurred.  Check website to ensure this is not due to html formatting changes.")
elif curr_date == web_data_date and last_rec_data == web_data_date:
	print("Minnesota CoVID-19 data is up to date.")
#print(curr_date, web_data_date, last_rec_data)


