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

# Docker installation
You can also install and run your file with docker
+ Install docker
If you don't have Docker installed, you can download and install it from the official Docker website: [Docker Installation Guide](https://docs.docker.com/get-docker/)
+ Build the Docker Image (Navigate to `ReelsBot` First)
```bash
docker build -t your-bot-name .
```
