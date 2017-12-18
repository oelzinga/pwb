import settings

class latexOutput():
	"""docstring for ClassName"""
	def save():
		text_file = open(str(settings.contentDir)+"/"+str(settings.testName)+"/"+"figures.tex", "w")


		gek="\n"

		for key in settings.concurrency:

			gek+="\\begin{figure}[H] \n"
			gek+="\centering \n"
			gek+="    % \setlength{\\belowcaptionskip}{-15pt} \n"
			gek+="\includegraphics[width=15cm]{img/"+str(settings.testName)+"-lineGraph-"+str(key)+".png} \n"
			gek+= "\\vspace{-2mm} \n"
			gek+= "\caption{"+str(settings.testName)+": latency met "+str(key)+" worker} \n"
			gek+= "\label{fig:"+str(settings.testName)+"-"+str(key)+"-w} \n"
			gek+= "\end{figure}\n\n"




		gek+="\\begin{figure}[H] \n"
		gek+="\centering \n"
		gek+="    % \setlength{\\belowcaptionskip}{-15pt} \n"
		gek+="\includegraphics[width=15cm]{img/"+str(settings.testName)+"-boxplot"+".png} \n"
		gek+= "\\vspace{-2mm} \n"
		gek+= "\caption{"+str(settings.testName)+": boxplot} \n"
		gek+= "\label{fig:"+str(settings.testName)+"boxplot} \n"
		gek+= "\end{figure}\n\n"

		print(gek)
		text_file.write(gek)

		text_file.close()
				

