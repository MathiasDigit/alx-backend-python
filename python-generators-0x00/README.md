# 📊 Python Generators for Streaming and Processing MySQL Data

This project uses Python **generators** to interact efficiently with a MySQL database — line by line, in batches, using lazy pagination, and for calculating statistics without loading the full dataset into memory.

---

## 🗂️ Project Structure

```
python-generators-0x00/
├── seed.py                  # Initializes the database and inserts data
├── user_data.csv            # CSV dataset to populate the user table
├── 0-stream_users.py        # Streams rows one by one using a generator
├── 1-batch_processing.py    # Processes user data in batches
├── 2-lazy_paginate.py       # Implements lazy pagination with generators
├── 3-stream_ages.py         # Calculates average age using a generator
├── 0-main.py                # Executes stream_users test
├── 1-main.py                # Executes batch processing test
├── 2-main.py                # Executes lazy pagination test
├── 3-main.py                # Executes average age calculation test
└── README.md                # Project documentation
```

---

## 🧪 Features

### ✅ 1. Stream Users One by One
- **File**: `0-stream_users.py`
- **Function**: `stream_users()`
- Uses `yield` to stream rows one at a time without consuming large memory.

### 📦 2. Batch Processing
- **File**: `1-batch_processing.py`
- **Functions**:
  - `stream_users_in_batches(batch_size)`
  - `batch_processing(batch_size)`
- Streams and filters users in batch groups — for example, filtering users older than 25.

### 📄 3. Lazy Pagination
- **File**: `2-lazy_paginate.py`
- **Functions**:
  - `paginate_users(page_size, offset)`
  - `lazy_paginate(page_size)`
- Fetches one page of results at a time using offset and limit, ideal for large datasets.

### 🧮 4. Calculate Average Age
- **File**: `3-stream_ages.py`
- **Functions**:
  - `stream_user_ages()`
  - `average_age()`
- Computes the average user age without using SQL’s AVG and without loading all rows at once.

---

## 📌 Example Output

**Sample streamed user record**:
```json
{'user_id': 'a6bc8f47-37f0-11f0-9f3b-a5bdc5a4e696', 'name': 'Ernest Frami', 'email': 'Elijah_Mante32@gmail.com', 'age': Decimal('108')}
```

**Sample average age calculation**:
```
Average age of users: 62.376
```

---

## 🛠️ Technologies Used

- Python 3.x
- MySQL 8.x or compatible
- mysql-connector-python
- python-dotenv (to load environment variables)
- Python generators (`yield`)
