# final-project-derek-volner
This is a project I worked on for my secure programming course at northwest missouri state university that involved improving the security of a program
I achieved this by:
 - Adding Unit Tests
 - Implementing PyLint Recommendations
 - Automated Testing on each commit to check whether unit tests passed or failed.
   - Touches on the CI/CD aspect of the requirements
 - Refactored code so it was in smaller chunks of code to allow for proper testing
   - for example turned the encrypt function into two functions putter and converter.
   -  This allowed me to check if the file was placing the characters as expected with putter fuction then check the conversion with the converter function.
 - Added Try and Catch Statements to account for availability, and partly integrity as per the C.I.A. triad standard
