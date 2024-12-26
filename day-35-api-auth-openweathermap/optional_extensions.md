# Optional Extensions to Functionality of the Weather API SMS Service

## Automate running the script

You can automate running the script by using a cron job, using <https://www.pythonanywhere.com/>

Information on how to set up a cron job on PythonAnywhere can be found [here](https://help.pythonanywhere.com/pages/ScheduledTasks/).

To fix the Connection error for Twillo see [here](https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/).

### Working with environment variables in PythonAnywhere

- Add environment variables to the PythonAnywhere environment with `export VARIABLE_NAME=value`
- Update the task scheduler to run the script with the environment variables by pasting the same export command in the command field of the task scheduler before calling the python script (separating each command by  `;`).
