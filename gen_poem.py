import os
import logging
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# LLM Service to interact with OpenAI model
class LLMService:
    def __init__(self, model_name='gpt-4', temperature=0.9):
        self.api_key = os.getenv(
            "OPENAI_API_KEY")
        if not self.api_key:
            logger.error("OPENAI_API_KEY not found in environment variables.")
            raise ValueError("OpenAI API key is missing!")

        self.llm = ChatOpenAI(api_key=self.api_key, model=model_name, temperature=temperature)

    def create_prompt(self):
        """Create a prompt template for generating children's poems."""
        system_message = SystemMessagePromptTemplate.from_template(
            "You are a creative and multilingual assistant that composes meaningful children's poems."
        )
        human_message = HumanMessagePromptTemplate.from_template(
            "Write a short, meaningful, rhyming children's poem about '{word}' in {language}."
        )
        return ChatPromptTemplate.from_messages([system_message, human_message])

    def generate_poem(self, word, language):
        """Generate a children's poem based on a word and language."""
        try:
            prompt = self.create_prompt()
            chain = LLMChain(llm=self.llm, prompt=prompt)
            response = chain.invoke({"word": word, "language": language})
            return response
        except Exception as e:
            logger.error(f"Error generating the poem: {e}")
            return "Sorry, I couldn't generate a poem right now."
