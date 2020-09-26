# Justdial-Scrapper
##### **DISCLAIMER** :: This project is strictly for learning purpose, to get practice over selenium! Data scraped might be licensed, proprietary or private. This project or inspiration in any form, should not be used for any business or promotional purposes.

##### MIT LICENCE THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 

##### THIS PROJECT, ITS OWNER OR ANY OF ITS CONTRIBUTORS WILL NOT BE LIABLE FOR ANY LEGAL / ILLEGAL ISSUES RAISED DUE TO THE USAGE OF THIS PROJECT OR THE USAGE OF THE DATA ACCUMULATED AS OUTPUT.

##### THIS PROJECT MIGHT USES REQUESTS TO THIRD PARTY SERVERS, SO ANYONE USE THIS PROJECT SHOULD AGREE THAT 1) YOU WILL NOT REDUCE THE TIME DELAYS PLACED IN THIS PROJECT IN BETWEEN REQUESTS. 2) YOU WILL NOT RUN THE SCRIPT MULTIPLE TIMES PARALLELLY AT THE SAME TIME.  

##### This Project is dated to the end of SEPTEMBER 2020, this will not guarantee you ever running platform. We tested this on the date of publish, any restructuring to the mentioned website might make this script unusable. Contributions are Welcome on that time.

Just Dial (also known as JD), is one of the prominent site, which needs some skill to scrape it down. That's Why i choose 
this platform to show you an example of how to scrape site, which creates some barriers, 


**PURPOSE:**

STRICTLY FOR EDUCATION PURPOSE.

JustDial Scrapper to scrap some of the basic data which includes their name, address, contact information, and phone number.

**HOW TO USE**
```
jd/
|---> data/
|       |---> input.txt            # Use this file to input the list of urls to scrape.
|       |---> output_.csv          # You will get the output in this file, after each running.
|       |---> output_test.csv      # sample test file.
|---> utils/
|       |---> browserhandle.py
|       |---> csvhandle.py
|       |---> extractor.py
|       |---> inputhandler.py
|       |---> parser.py
|---> .gitignore
|---> LICENSE
|---> main.py                       # script to run 'python main.py'
|---> README.md
|---> requirements.txt
```

**INPUT FORMAT:**

Place the url of the searched page in the input txt file in the format 
: `data/input.txt`
```
https://www.justdial.com/Kochi/Fabric-Retailers/nct-10890504
https://www.justdial.com/Kochi/Schools-in-Kochi/nct-10422444
https://www.justdial.com/Trivandrum/Temples/nct-10475644
```

**INSTALLATIONS:**

Currently, this script is developed using UBUNTU and
Probably will be supported over any Linux / Unix Systems. 
We Would like to get contributions to make the script cross platform.
 
We Use Selenium and Webdriver Which supports Firefox. 

Install Selenium for Python:

``` 
python -m pip install selenium 
```

INSTALL `geckodriver`
``` 
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz 
tar -xvzf geckodriver-v0.24.0-linux64.tar.gz
chmod +x geckodriver
export PATH=$PATH:$PWD
```

**DO NOT FORGET TO SET PATH**


How to Use.
1. Make sure that you have set your path, and is available at your ubuntu `terminal` session
    `echo $PATH`
2. Create a set of URL's  and update it over `data/input.txt` file.
3. Run `python main.py`
4. Collect the output from `data/output_.out`



**ADJUSTMENTS:** Since We have adopted the design of managing Endless Scrolling,  

 
