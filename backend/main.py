from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.models import db_helper, Base
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan,
              description="Система регистрации и авторизации для платформы ИИ-помощников. Собрана система авторизации на JWT токенах.\n "
                          "База данных sqlite. По всем вопросам обращаться в  тг: @Garanash \n",
              title='ALMAZGEOBUR AI Agent')
app.include_router(router_v1, prefix='/api_v1')

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
