from gtts import gTTS 
import os
import requests 


def request_joke(api_url):
    try:
        response=requests.get(api_url)
        response.raise_for_status()

        data=response.json()

        ques=data["setup"]
        ans=data["punchline"]


        textToSpeech(ques ,"out.mp3" )
        textToSpeech(ans , "out2.pm3")



    except requests.exceptions.RequestException as a :
        print(f"Error : {e}")
    except ValueError as e :
        print(f"Error prasing JSON : {e}")





def textToSpeech(text, output_file):
    output =gTTS(text=text , lang='en')
    output.save(output_file)
    
    os.system(f"xdg-open {output_file}")


   

if __name__ == "__main__":
      
     api_url="https://official-joke-api.appspot.com/random_joke"
     request_joke(api_url);
