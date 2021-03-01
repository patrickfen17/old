summaryrow = 0

totalvolume = 0 

openingprice = Cells(2,3.Value)

closingprice = 0



Loop through all rows in column 1 (lastrow thingy hear)

​	totalvolume = totalvolume + cellcalledvol

​	if current cell ticker different from next cell ticker then

​		**'get the current row's closing price**

​		closingprice = cell F

​		yearchange = closingprice - openingprice	

​		**'Put change over in my summary table**

​		**'and change color of cell**

​		If opening price is > 0 then

​		percentchange = yearchange / openingprice

​		else percentchange = 0

​		openingprice = Cells(i+1,3)

​		summaryrow = summaryrow + 1

​		**'This is where we update our summary table**



**'after we update need to reset totalvolume**

totalvolume = 0

​	End if

End loop



