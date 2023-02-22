# Discord
Discord Bot Auto Send is a tool that automatically sends messages to Discord servers or channels.

## • Requirement
- [Python](https://www.python.org)
- [Git](https://git-scm.com)
> *Use one of them*

## • Features
- *quote*
- *reply*
- *repost*
- *simsimi*
- *custom*

## • Bookmarks
Add bookmarks `Name` and `URL` in your browser

**Sign In**
```bash
javascript:(()=>{var t=prompt('Sign in with discord account using your token');document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token=`"${t}"`;location.href='/channels/@me'})();
```
> *Don't sign out of your account, just sign in using another token.*

**Token**
```bash
javascript:(()=>{var t=document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token.replace(/["]+/g, '');prompt('Congratulations, this is your token', t)})();
```
> *If on mobile paste URL in search bar, you must be sign in to discord, rewrite `javascript` and `:` in front of URL*

## • Installation
```console
git clone https://github.com/arisaripin/discord.git
```
```console
cd discord
```
```console
pip install -r requirements.txt
```

## • Configuration
```yaml
TOKEN:
 - token 1
 - token 2
CHANNEL:
 - channel 1
 - channel 2
MODE: quote # quote, reply, repost, simsimi, custom
LANG: en # en, ph, zh, ch, ru, id, ko, ar, fr, ja, es, de
REPLY: true # true, false
DELETE: true # true, false
DELAY: 60 # seconds
REPOST: 100 # number of messages
```

## • Usage
```console
python bot.py
```