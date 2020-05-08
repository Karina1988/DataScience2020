startGame <- function()
{
	randNumber <- round(runif(1, 0, 100))
	guess = -1

	while (guess != randNumber) 
	{
		guess <- readInput()
		if (guess == randNumber) 
		{
			cat("Jippie, die Zahl ist korrekt!\n")
			restartGame <- readRestartGame()
			if (restartGame == "y") 
			{
				startGame()
			}
			else
			{
				cat("Ciao!\n")
			}
		}
		else if (guess < randNumber)
		{
			cat("Deine Zahl ist zu niedrig.\n")
		}
		else
		{
			cat("Deine Zahl ist zu hoch.\n")
		}
	}
}

readInput <- function()
{ 
  input <- readline(prompt="Rate die Zahl zwischen 0 und 100: ")
  return(as.integer(input))
}

readRestartGame <- function()
{
	input <- readline(prompt="Nochmal? y/n \n")
  	return(input)
}

startGame()