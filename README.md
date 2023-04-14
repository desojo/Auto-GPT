# Auto-GPTweeter: Turning AutoGPT Into a Twitter User

# ⛔️ WARNING ⛔️
Please, for the love of god, run this in a docker container or some other VM. Make sure your home network is secure. Sandbox this as much as you can. If you don't care about what happens to your machine or network, more power to you, but you're giving randoms on the internet the ability to interact with an AutoGPT instance running on a device you control. That's literally giving them the ability to remotely execute code on your machine, so expect to restore the image frequently.

____

## ✨ Essential features Roadmap ✨

    1. ✅ Functioning post_tweet command, giving AutoGPT the ability to post to twitter and request a task ✅
    2. ❌ Functioning read_replies command, giving AutoGPT the ability to read replies to it's tweet and select a task ❌
    3. ❌ Method for tweeting out a link to each task log upon task completion, with links to any included code or photos ❌
    4. ❌ Secure storage for API keys, so mean twitter users can't talk your AutoGPT into handing out your precious GPT-4 keys ❌

## 📋 Requirements

- [Python 3.8 or later](https://www.tutorialspoint.com/how-to-install-python-in-windows)
- [OpenAI API key](https://platform.openai.com/account/api-keys)
- [PINECONE API key](https://www.pinecone.io/)
- [Twitter API Key](https://developer.twitter.com/en/apply-for-access)

## 💾 Installation

To install Auto-GPT, follow these steps:

1. Make sure you have all the **requirements** above, if not, install/get them.

_The following commands should be executed in a CMD, Bash or Powershell window. To do this, go to a folder on your computer, click in the folder path at the top and type CMD, then press enter._

2. Clone the repository:
   For this step you need Git installed, but you can just download the zip file instead by clicking the button at the top of this page ☝️

```
git clone https://github.com/Torantulino/Auto-GPT.git
```

3. Navigate to the project directory:
   _(Type this into your CMD window, you're aiming to navigate the CMD window to the repository you just downloaded)_

```
cd 'Auto-GPT'
```

4. Install the required dependencies:
   _(Again, type this into your CMD window)_

```
pip install -r requirements.txt
```

5. Rename `.env.template` to `.env` and fill in your `OPENAI_API_KEY`.

  - Obtain your OpenAI API key from: https://platform.openai.com/account/api-keys.
  - Obtain your [Pinecone API key](https://docs.pinecone.io/docs/quickstart) and fill it in
  - Obtain the following Twitter API keys from the [Twitter Developer Portal](https://developer.twitter.com/en/docs/developer-portal) and fill them in
    ```
    TWITTER_API_KEY=your-twitter-api-key
    TWITTER_API_KEY_SECRET=your-twitter-api-key-secret
    TWITTER_BEARER_TOKEN=your-twitter-bearer-token
    TWITTER_ACCESS_TOKEN=your-twitter-access-token
    TWITTER_ACCESS_TOKEN_SECRET=your-twitter-access-token-secret
    TWITTER_CLIENT_ID=your-twitter-client-id
    TWITTER_CLIENT_SECRET=your-twitter-client-secret
    ```
  - <span style="color:red">**HIGHLY RECCOMENDED**</span>**:** If you want to use GPT on an Azure instance(), set `USE_AZURE` to `True` and then:
    - Rename `azure.yaml.template` to `azure.yaml` and provide the relevant `azure_api_base`, `azure_api_version` and all of the deployment ids for the relevant models in the `azure_model_map` section:
      - `fast_llm_model_deployment_id` - your gpt-3.5-turbo or gpt-4 deployment id
      - `smart_llm_model_deployment_id` - your gpt-4 deployment id
      - `embedding_model_deployment_id` - your text-embedding-ada-002 v2 deployment id
    - Please specify all of these values as double quoted strings
    - details can be found here: https://pypi.org/project/openai/ in the `Microsoft Azure Endpoints` section and here: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/tutorials/embeddings?tabs=command-line for the embedding model.



