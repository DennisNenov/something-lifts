console.log("Hello World");
console.log(weightlist);

var width=800,
height=400,
padding=20;

var xScale = d3.scale.linear()
    .domain([0,3])
    .range([padding,width-padding]);

var yScale = d3.scale.linear()
    .domain([0,500])
    .range([height-padding,padding]);

var yAxis = d3.svg.axis().scale(yScale).orient("left");

var svg = d3.select("#content").append("svg")
    .attr("width", 800)
    .attr("height", 400)
    .classed("bordered", true)
    .attr("id", "svg")

svg.selectAll(".dots")
    .data(weightlist)
    .enter()
    .append("g")
    .classed('dots',true);

svg.selectAll(".dots")
    .append("circle")
    .attr("cx",function(d,i){return xScale(i);})
    .attr("cy",function(d){return yScale(d);})
    .attr("r",10)
    .attr("fill","green");

var linef = d3.svg.line()
    .x(function(d,i){return xScale(i);})
    .y(function(d,y){return yScale(d);})
    .interpolate("cardinal");

svg.append("path")
    .attr("d",linef(weightlist))
    .attr("stroke","red")
    .attr("stroke-width",2)
    .attr("fill","none");
