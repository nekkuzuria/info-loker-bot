# info-loker-bot

as someone that often share job vacancy to my friends in discord, i got an idea to create a bot to help me.

basically, this bot just gets job vacancy from linkedin and integrates it to discord using webhook.

also, big thanks to indian it guy for this incredible project:
https://github.com/VishwaGauravIn/linkedin-jobs-api/

## how to use?

1. copy `.env.example` as `.env`

```bash
cp .env.example .env
```

2. get ur discord webhook url.

go to ur discord server channel:
`channel settings → integrations → create webhook`

then just copy the webhook url.

3. paste ur discord webhook url in the `.env`

4. create virtual environment

```bash
python3 -m venv .venv
```

5. activate the venv

```bash
source .venv/bin/activate
```

6. install requirements

```bash
pip install -r requirements.txt
```

7. finally, run the script

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
