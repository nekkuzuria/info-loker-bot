# info-loker-bot

as someone that often share job vacancy to my friends in discord, i got an idea to create a bot to help me.

basically, this bot just gets job vacancy from linkedin and integrates it to discord using webhook.

also, big thanks to our indian tech bro for this incredible project:
https://github.com/VishwaGauravIn/linkedin-jobs-api/

<img width="940" height="756" alt="image" src="https://github.com/user-attachments/assets/09753510-8de6-4845-8bf1-0d2d226a2448" />


## how to use?

1. copy `.env.example` as `.env`

```bash
cp .env.example .env
```

2. add your openrouter api key

go to the openroute website:
https://openrouter.ai/

create an account if you don't have one, then:
`api keys → new key`

copy the API key and put it in your `.env` file.

example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

3. get ur discord webhook url.

go to ur discord server channel:
`channel settings → integrations → create webhook`

then just copy the webhook url.

4. paste ur discord webhook url in the `.env`
   example:

```env
DISCORD_WEBHOOK_URL_LIST=["your-discord-webhook-url-here"]
```

5. create virtual environment

```bash
python3 -m venv .venv
```

6. activate the venv

```bash
source .venv/bin/activate
```

7. install requirements

```bash
pip install -r requirements.txt
```

8. finally, run the script

```bash
python3 main.py
```

and u got the job updates in ur discord 


## customize

u can change the params based on ur needs in `main.py` and `crawler.py`.

for example:
- job keywords
- locations
- remote job option
- internship / entry level filter
- etc.

## contribution

this project is open for contribution.

one thing i think can be improved is making the params dynamically set from a config file, so the script can be cleaner and easier to customize.

feel free to open a pull request or contribute :) 
