<h3 align=left>
    <img align="left" src="https://www.pngmart.com/files/13/Instagram-Logo-Transparent-Images-PNG.png" width=120 />
    <h3><b>ReelsBot</b></h3>
    <p>Instagram Reels Downloader bot</p>
</h3>
<br><br>

# Installation
+ Clone the repository
```bash
git clone https://github.com/Kourva/ReelsBot
```
+ Navigate to files directory
```bash
cd ReelsBot
```
+ Give Execute permission to main file
```bash
chmod +x bot.py
```
+ Initialize token
```bash
echo 'TOKEN=Your token here' > Token.env
```
> Example: `echo 'TOKEN=1234567890:AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQR' > Token.env`                                       
> Or edit Token.env file manually!
+ Install requirements
```bash
pip install -r requirements.txt
```
+ Run the bot using python or open it direclty using `./bot.py`
```bash
python bot.py
```
#### One line command
```bash
git clone https://github.com/Kourva/ReelsBot && cd ReelsBot && chmod +x bot.py && pip install -r requirements.txt
```
> You still need to configure your **token**

<br>

# Docker installation
You can also install and run your file with docker. <br>
If you don't have Docker installed, you can download and install it from the official Docker website: [Docker Installation Guide](https://docs.docker.com/get-docker/)
+ Clone the repository
```bash
git clone https://github.com/Kourva/ReelsBot
```
+ Navigate to files directory
```bash
cd ReelsBot
``` 
+ Build the Docker Image
```bash
docker build -t your-bot-name .
```
+ Run your Docker Image
```bash
docker run your-bot-name
```
> Note: replace `your-bot-name` with your suitable name for your bot

<br>

# Usage
For the usage just send reel URL copied from instagram to bot. Note that some rells can't be downloaded.
> You can also host your bot in [pythonanywhere](https://www.pythonanywhere.com) for free.

<br><br>

# Thank You
Thank you for checking out this repository! Your interest and support are greatly appreciated. If you find this project useful or have any feedback, please feel free to open issues or contribute.
> Happy coding!

