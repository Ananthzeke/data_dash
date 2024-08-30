---
marp: true
---

# Database Types: SQL vs NoSQL

---

# SQL vs NoSQL

### SQL (Relational Databases)
- **Type**: Structured (Tables)
- **Example**: MySQL, PostgreSQL
- **Use Case**: Structured data with defined relationships

### NoSQL (Non-Relational Databases)
- **Type**: Flexible (Documents, Key-Value, etc.)
- **Example**: MongoDB, Redis
- **Use Case**: Unstructured/Semi-structured data, Scalability

---

# Relational Database Example

### MySQL Example
```sql
CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```
- **Structured Data**: Rows and Columns
- **Example**: Managing user data with strict schema

---

# NoSQL Database Example

### MongoDB Example
```json
{
    "_id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Springfield"
    }
}
```
- **Flexible Schema**: JSON-like documents
- **Example**: Storing user data with optional fields

---

# ODM vs ORM

### ODM (Object Data Mapping)
- **Maps**: Objects to NoSQL documents
- **Example**: mongoengine for MongoDB
```python
from mongoengine import Document, StringField, connect

# Connect to MongoDB
connect('user_database')

# Define the User schema
class User(Document):
    name = StringField(required=True, max_length=100)
    email = StringField(required=True, unique=True)
    street = StringField()
    city = StringField()

# Create a new user instance
new_user = User(
    name='John Doe',
    email='johndoe@example.com',
    street='123 Main St',
    city='Springfield'
)

# Save the user to the database
new_user.save()

# Querying the user
user = User.objects(name='John Doe').first()
print(user.email)  # Output: johndoe@example.com

```
---
### ORM (Object-Relational Mapping)
- **Maps**: Objects to SQL tables
- **Example**: SQLAlchemy for MySQL
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create an engine and session
engine = create_engine('mysql+pymysql://user:password@localhost/user_database')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user instance
new_user = User(name='John Doe', email='johndoe@example.com')

# Add and commit the user to the database
session.add(new_user)
session.commit()

```

---

# SQL vs NoSQL: Pros & Cons

### SQL (Relational)
- **Pros**:
    - Structured data, strong relationships
    - ACID Compliance
- **Cons**:
    - Rigid schema, harder to scale horizontally
---
### NoSQL (Non-Relational)
- **Pros**:
    - Flexible schema, easy to scale
    - High performance for large datasets
- **Cons**:
    - May lack ACID compliance
    - Complex relationships between data
---

# Same Example in SQL & NoSQL

### SQL: MySQL
```sql
CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

### NoSQL: MongoDB
```json
{
    "_id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Springfield"
    }
}
```
---

# Conclusion

- **SQL**: Best for structured, relational data.
- **NoSQL**: Best for scalability and flexible data.
- Choose based on your application needs!

