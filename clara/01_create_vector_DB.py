# Exercise 1: Connections
## Question 0
# %%
from dotenv import load_dotenv
load_dotenv()

## Question 1
# %%
from openai import OpenAI
client_llmlab = OpenAI(
    base_url=os.environ["LLMLAB_URL"],
    api_key=os.environ["LLMLAB_API_KEY"],
)

## Question 2
# %%
models = client_llmlab.models.list()
model_list = list(models) 
for m in model_list:
    print(m.id)

## Question 3
# %%
from qdrant_client import QdrantClient
client_qdrant = QdrantClient(
    url=os.environ["QDRANT_URL"],
    api_key=os.environ["QDRANT_API_KEY"],
    port=os.environ["QDRANT_API_PORT"],
    check_compatibility=False
)
collections = client_qdrant.get_collections()
for collection in collections.collections:
    print(collection.name)

# Exercise 2
## Question 1
# %%
