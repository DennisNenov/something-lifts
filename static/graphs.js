console.log("Hello World");
console.log(weightlist);

var width=800,
height=400,
padding=20;

var xScale = d3.scale.linear()
    .domain([0,numWorkouts])
    .range([padding,width-padding]);

var yScale = d3.scale.linear()
    .domain([0,greatestValue])
    .range([height-padding,padding]);

var yAxis = d3.svg.axis().scale(yScale).orient("left");

var xAxis = d3.svg.axis().scale(xScale).orient("bottom");

var svg = d3.select("#content").append("svg")
    .attr("width", 800)
    .attr("height", 400)
    .classed("bordered", true)
    .attr("id", "svg")
    .append("g")
    .attr("transform","translate(40,0)")
    .call(yAxis)

svg.append("g")
    .attr("transform", "translate(0, 375)")
    .call(xAxis)

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
    .attr("fill","green")
    .append("text")
    .attr("dx", function(d){return -20;})
    .text(function(){return 'hello';});

var linef = d3.svg.line()
    .x(function(d,i){return xScale(i);})
    .y(function(d,y){return yScale(d);})
    .interpolate("cardinal");

svg.append("path")
    .attr("d",linef(weightlist))
    .attr("stroke","red")
    .attr("stroke-width",2)
    .attr("fill","none");

var text = svg.selectAll("text")
    .data(weightlist)
    .enter()
    .append("text")
    .attr("text-anchor", "middle");

text.attr("x", function(d, i) { return i; })
    .attr("y", function(d) { return d; })
    .text(function (d) { return d; })
    .attr("font-family", "sans-serif")
    .attr("font-size", "20px")
    .attr("fill", "red");
