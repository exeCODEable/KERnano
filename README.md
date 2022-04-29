### KERnano
The No-install Python Pen Testing kit. (Windows & Linux)<br>
---------------------------------------------
<p> www.exeCODEable.com | www.KERnano.com | www.AshNoor.me </p>
-------------------------------------------------------------------------
</br></br>
<p>
  <b>What does "No-Install" mean?</b> </br>
  It means just that, I wanted to create a tool that is simply "Click & Play". </br>
  In this Repo you will find folder called "The_Executables" in it you will find: </br>
    1. KERnano-Windows_v-1: An executable for <b>Windows machines</b>. </br>
    2. KERnano-Linux_v1: An executable for <b>Linux machines</b>. </br>
  
  </br></br>
  
  <b>What is the benefit of this?</b> </br>
  This mean, this multi-tool is portable. </br>
  You can easily place the executable of your choice "or both" in a flash drive and go about your way. </br>
  If you ever need to use it, just plug in the USB into a machine and just "Click" the executable. </br>
  Easy Peasy.
</p>
---------------------------------------------

</br> </br>

<p>
  <b>What are the tools in KERnano?</b> </br>
  This 1st version has 10 tools, but the hope is people find this tool useful, and more tools would get added. </br>
  The tools at the moment are broken into 3 catagories, and an off-shoot tool. </br>
  Here is a quick over-view of the tools, but details of the tools will be avilable on exeCODEable's blog. (www.exeCODEable.com)
  </br></br>
  1. <b>Pen Test Tools.</b> </br>
        
    - HLPR. 
      You give it your IP and the Target's IP, and it will give you a text file with Kali/Parrot commands with your IPs already injected.
      Common commands for Nmap, GoBuster, KiteRunner, ect. .
      
    - B64. 
      A local Base64 Encoder / Decoder.
      
    - URL Checker. 
      You can give it a single URL, or a text file of URLs.
      It would check if they are "Up" (200), and if they are SSL enabled or not.
      When you use the "text file of URLs", it will give you back 2 text files:
        One for the active SSL enabled sites.
        One for the active SSL disabled sites.
        
    - Port Scanner.
      A very basic port scanning tool, using the python-nmap library.
      This gives you two options:
        Scan all the ports.
        Scan a specific range.
        
       Full Disclosure:
       This tool is a bit slow, I used Mr. David Bombel's code as the catalyst for this.
       Hope in future versions I would be able to make a faster with a bit more features.
  
  </br></br>
  2. <b>PDF Kit.</b> </br>
           
    - Text Extractor. 
      You give it a PDF, it will extract the information and give it to you in a text file.
      Currently it only works with English (ASCII) PDFs.
      I'm hoping to devlop this to work with other (Unicode) based languages.
      
    - Password Remover. 
      If you have a password protected PDF and its's password.
      This tool will create a non-password protected copy of the PDF for you.
  
  </br></br>
  3. <b>General Tools.</b> <br>
            
    - CHMODER. 
      To help you figure out the "CHMOD" code for a file.
      Through simple choices, it asks you the permissions you want each section of a file needs.
      And at the end it gives you the numeric code, and shows you what file permission would look like.
      
    - DE-1337-ER. 
      Helps you convert "L33t Sp34k" to normal text, and vice versa.
      
    - Note Maker. 
      A quick way to create a note for a CTF, to help you organize.
      It will ask you for the name of the CTF, the URL, and how many flags are in your challenge.
      Based on that, it will give you a text file with the name and url of your CTF on the top of the page.
      And pre-seperated sections for the number of flags you mentioned.
      
      I found this to be helpful when I'm working CTFs that would take me longer then one session to complete.
      A good way to keep the informaiton of the challenge, and thoughs organized.
      
  
  </br></br>
  4. <b>Wordlister.</b> </br>
    
    This tool accepts text files or PDFs, it would extract the text and provide you with a worldlist in a text file. 
    It will have no dublicate words, no numbers, and no special characters. 
    This a simple and quick way to create custom wordlists for your projects.
  
</p>
---------------------------------------------

</br></br>

<p>
  This tool is meant to be used for Ethical Hacking, please use it to help make the internet safer for everyone. </br>
  This was created for educational purposes. </br>
  This is a work in progress, just like we all are. </br>
  Do not Pentest / Hack any entity without written permissions first. </br>
  Be Smart, Be Safe, Be Super awesome. </br>
  
  Ash Noor (ryn0f1sh)</br>
  www.AshNoor.me | www.ryn0f1sh.blog
  
</p>
