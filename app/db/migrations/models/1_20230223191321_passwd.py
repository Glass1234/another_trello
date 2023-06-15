from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "passwd" TYPE TEXT USING "passwd"::TEXT;
        ALTER TABLE "user" ALTER COLUMN "passwd" TYPE TEXT USING "passwd"::TEXT;
        ALTER TABLE "user" ALTER COLUMN "passwd" TYPE TEXT USING "passwd"::TEXT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "passwd" TYPE VARCHAR(256) USING "passwd"::VARCHAR(256);
        ALTER TABLE "user" ALTER COLUMN "passwd" TYPE VARCHAR(256) USING "passwd"::VARCHAR(256);
        ALTER TABLE "user" ALTER COLUMN "passwd" TYPE VARCHAR(256) USING "passwd"::VARCHAR(256);"""
