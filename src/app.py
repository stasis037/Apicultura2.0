from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample articles data
articles = [
    {
        "id": 1,
        "title": "Introduction to Beekeeping",
        "content": "Learn the basics of beekeeping and how to get started with your first hive.",
        "image": "https://images.unsplash.com/photo-1582407947304-fd86f028f716?ixlib=rb-4.0.3"
    },
    {
        "id": 2,
        "title": "Honey Harvesting Tips",
        "content": "Essential tips for harvesting honey from your beehives safely and efficiently.",
        "image": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?ixlib=rb-4.0.3"
    }
]

@app.get("/api/articles")
async def get_articles():
    return articles
