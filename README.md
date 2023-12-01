# theHarvester-Automation
Automation script for email extraction using theHarvester

# Get started
1. First clone theHarvester project at your prefered location

git clone https://github.com/laramies/theHarvester.git

2. Install theHarvester

cd theHarvester
pip install .
ln -s bin/theHarvester <TO A PATH IN YOUR $PATH>

3. Now you can run the automation script

python3 src/automate.py

4. Once the extraction is done run following to organize the extracted emails

python3 src/get_email.py

Article: https://medium.com/@higgsborn/automate-email-extraction-with-theharvester-8049885b4e2c
