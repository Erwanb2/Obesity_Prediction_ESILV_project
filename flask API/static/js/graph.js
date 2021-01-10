$(document).ready(function() {
	$(chart1_id).highcharts({
	  chart: chart1,
	  title: title1,
	  xAxis: xAxis1,
	  yAxis: yAxis1,
	  series: series1
   });
  });
  
  $(document).ready(function() {
   $(chart2_id).highcharts({
	chart: chart2,
	title: title2,
	xAxis: xAxis2,
	yAxis: yAxis2,
	series: series2
  })});