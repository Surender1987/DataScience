import DataVisualization

#Initialize data
years = [1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993]
population = [5000,5100,5800,6800,6600,6700,6900,7000,7500,8000,8800,10000,10982,12000]
#Draw line chart
dataVisualization = DataVisualization.DataVisualization(years, population, "Population", "Population", "Year")
dataVisualization.BarChart()