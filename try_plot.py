from plot import Plot

# Simple plot demo
plot = Plot()
plot.line(plot.width/2, 0, plot.width/2, plot.height/2)
plot.circle(plot.width/2, plot.height/2, 10)
plot.loop()