[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10189187&assignment_repo_type=AssignmentRepo)
# Lab 5
Clone this repo to your machine to get started!

## Team Members
- Robert Zhang
- Jiansong Li

## Lab Question Answers

Answer for Question 1: 
      dBm is unite of power measurement which can measure power in milliwatts on a log scale.
      For a good and strong WiFi signal strength, it is usually around -60 dBm or higher.
      For a wearker Wifi signal strength, the signal is around -80 dBm.
      In order to have a stable connection, the strength is usually about -67 dBm.
     
Answer for Question 2: 
	Different OS have different command-line interfaces and syntax. And more importantly, some commands can only work at certain OS. 
	In  case of our lab, we have to apply different commands to check for wifi signal strength , and sometimes the measurement are conducted differently in different OS. 
	
Answer for Question 3: 
 	subprocess.check_output is used to run certain commands and moniter the outputs and finally can retrieve these output. The output of the arguments and commands are basically the output of this method. 
        

Answer for Question 4: 
	re.search can be used to check through string object and search for the first location where the regular expression pattern produce a match, and then this method can return the corresponding match object. Else, it will return none if there is no match result. 
	 
Answer for Question 5: 
	The reasons are Windows conducting a different measurement and it uses a percentage value which could represent the signal quality of the network. A value of 100 implies an actual signal strength of -50 dBm. 
        
        
        
Answer for Question 6: 
        The standard deviation retrieve the amount of variation or dispersion of a set of data around its mean value. 
        It is useful because it enable to quantify the degree of dispersion and and variation. It is beneficial in statistics and very convenient measurement to directly express the varaibility and distribution of a set of data. 
        
Answer for Question 7: 
         
   
           
         Dataframe is an organization of two-dimensional,size-mutable,potentially hetergeneous tabular data. In dataframe structure, data is orgnaized in rows and columns and data is collected in series of objects,  and each column is a series of object data. 
         Dataframe is useful because it is powerful tool for working with organized data and more importantly, it can be used to graph and diagram plotting in our lab. Besides that, dataframe enables to do data cleaning, preprocessing, analysis, and also integrating with other python tools and methods.
         
         
Answer for Question 8: 
	Error bars are important because they display an estimated value of the uncertainty or variability of a data set. They could be used to quantify and directly show the level of how much the data deviate from the mean value. Moreover, the error bars visualize the spread of the data set and tells us the reliability of the measured data, which could be extremely useful if we need to present comparsions and contrast between different groups of data. In the case of our lab, we actually need to use the error bars to evaluate the reliability, variability, uncertainty of different group of signal strength data at different locations. 
	
Answer for Question 9: 
	I can oberserve that the signal strength variates when the locations are changed. At certain locations, the signal strength is stronger and the error bars are shorter. When I was at bedroom, the signal strength was higher. And it present less variablity and uncertainty when I was at bedroom and living room. 
	
	Therefore, I conclude that the signal strength becomes wearker, unstable, and more turbulent as I am moving away from the bedroom. When I was at bedroom, the signal strength was strongest and stable. 
	
	I think the distance could be one factor that affecting the signal strength. At my home, the wifi router is located at the bedroom. Therefore, as I am distanced and farther away from the bedroom, for example outside of the house, the siganl strength is weaker. 
	
	In addition to distance, I think interference and obsturctions are the other two factors contributed the weaker signal in certain locations. When I was at livingroom, there are other wireless deices and appliances which could produece certain level of interference to the wifi signal. Then, when I was at the staircase, the walls and floors could physically block and weaken the wifi signals.

Answer for Question 10:
	In the data graph, we noticed that the place where has higher signal strength will has higher delay.  When the message size increase, the delay will also increase.It is different from part 1 because larger messages require more time to be transmitted over the communication channel. I think it may also cause by the weather. I think the wind and rain change the delay of the message.

