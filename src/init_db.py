from src.db import Base, engine, SessionLocal
from src.models import Category, Type, ArticleName, Article

# Create tables
Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()
    
    # Check if we already have data
    if db.query(Article).count() > 0:
        print("Database already initialized")
        return

    # Add sample categories
    categories = [
        Category(name="Beekeeping Basics"),
        Category(name="Honey Production"),
        Category(name="Bee Health")
    ]
    for category in categories:
        db.add(category)
    
    # Add sample types
    types = [
        Type(name="Guide"),
        Type(name="Tutorial"),
        Type(name="Tips")
    ]
    for type_ in types:
        db.add(type_)
    
    # Add sample article names
    article_names = [
        ArticleName(name="Getting Started"),
        ArticleName(name="Best Practices"),
        ArticleName(name="Advanced Techniques")
    ]
    for article_name in article_names:
        db.add(article_name)
    
    # Commit to get IDs
    db.commit()
    
    # Add sample articles
    articles = [
        Article(
            title="Introduction to Beekeeping",
            content="Learn the basics of beekeeping and how to get started with your first hive.",
            category_id=1,
            type_id=1,
            article_name_id=1
        ),
        Article(
            title="Honey Harvesting Tips",
            content="Essential tips for harvesting honey from your beehives safely and efficiently.",
            category_id=2,
            type_id=3,
            article_name_id=2
        ),
        Article(
            title="Maintaining Healthy Bee Colonies",
            content="Advanced guide to keeping your bee colonies healthy and productive.",
            category_id=3,
            type_id=2,
            article_name_id=3
        )
    ]
    for article in articles:
        db.add(article)
    
    db.commit()
    print("Database initialized with sample data")

if __name__ == "__main__":
    init_db()
