from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "board" RENAME COLUMN "color" TO "background_color";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "board" RENAME COLUMN "background_color" TO "color";"""
