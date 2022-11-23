def openFileWithSecurePractice(file):
			# Opening file with Exception Handling
			try:
				openObj=open(file,"r")
				fileLines=openObj.readlines()
				lineCounter=1
				for lineOfFile in fileLines:
					print(lineCounter, lineOfFile)
					lineCounter=lineCounter+1
			except:
				# Enters if there are errors in code
				print("File is not accessible......")
			finally:
				# Closing object if there are errors
				openObj.close()
		#Calling Python Function
openFileWithSecurePractice("C:\\Data.txt")
