# Chart emails received 
Extracting and charting activity based on email contents.

This guide is for coding beginners like myself. Please be kind to me :)
I am using this project as a practice for more scripts aimed at improving workflows and extracting data.

All emails in a specified folder are extracted into a csv file, into an input folder at .//INPUT
Each email folder (without any sub-folder) is saved as a separate csv file.
-- The above has not been pushed into the current script yet. Currently, RPA is being used to extract the emails. --
Saved files are passed through a code that generates charts based on the user's input date range (longer date ranges mean longer time taken to generate chart).
Generated charts are saved in an output folder at .//OUTPUT

List of functionalities to be added:
- Adding feature to automatically save generated charts in a specified folder (added)
- Writing VBA to automatically extract emails from a given folder on outlook (issue with ts.Writeline function; not behaving as expected - function does not write in newline but writes in the same row instead)
- VBA should include user input for the path of target email folder
- VBA will automatically reference the python script
- Considering using other automation scripts (RPA) to automate email extraction process

Running the code:
1. Ensure python is installed on device
2. Ensure that required modules have been installed (see requirements)
4. Ensure that cwd is changed to the folder where the script is at [type the following into the cli: cd "<full_path_of file>"
5. Run the file by calling "python cctv-charting.py"
6. Script output should look like the following: ![image](https://github.com/TLYiing/cctv_email_notifs_charting/assets/46553538/b12e8400-02fc-420a-b496-0532dd4d0fe1)
7. A single chart will be created for each day (example shows charts created for 2 days within the range of 08/07/2024 - 09/07/2024) - Each chart must be closed before the next chart can be seen. Each chart looks like this: ![image](https://github.com/TLYiing/cctv_email_notifs_charting/assets/46553538/9494976a-6d52-4b17-9289-56b0d4ffbf80)

Extra:
- Hypothesis testing to generate alerts for activities outside of planned activities:
