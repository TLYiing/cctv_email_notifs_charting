# Chart emails received 
Extracting and charting activity based on email contents.

All emails in a specified folder are extracted into a csv file, into an input folder at .//INPUT
Each email folder (without any sub-folder) is saved as a separate csv file.
Saved files are passed through a code that generates charts based on the user's input date range (longer date ranges mean longer time taken to generate chart).
Generated charts are saved in an output folder at .//OUTPUT

List of functionalities to be added:
- Adding feature to automatically save generated charts in a specified folder (added)
- Writing VBA to automatically extract emails from a given folder on outlook (issue with ts.Writeline function; not behaving as expected - function does not write in newline but writes in the same row instead)
- VBA should include user input for the path of target email folder
- VBA will automatically reference the python script
- Considering using other automation scripts (RPA) to automate email extraction process
