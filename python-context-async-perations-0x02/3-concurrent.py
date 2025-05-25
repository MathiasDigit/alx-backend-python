"""This script runs multiple database queries concurrently using asyncio and aiosqlite."""

import asyncio
import aiosqlite

# Asynchronous function to fetch all users
async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("All users:")
            for user in users:
                print(user)
            return users
        
# Asynchronous function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            olders_users = await cursor.fetchall()
            print("\nUsers older than 40:")
            for user in  olders_users:
                print(user)
            return olders_users
        
# This function runs both fetch operations concurrently
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )


# Start the asynchronous execution
asyncio.run(fetch_concurrently())